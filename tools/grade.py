#!/usr/bin/env python3
"""Offline Bash practice grader. Runs only trusted local scripts in temp fixtures.

Use: python tools/grade.py --list
     python tools/grade.py B01
     python tools/grade.py --verify-references

Not a security sandbox: do not execute untrusted downloaded code.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
TASKS = json.loads((ROOT / "labs/tasks.json").read_text(encoding="utf-8"))
INDEX = {task["id"]: task for task in TASKS}


def fixture(base: Path, id: str, variant: int) -> tuple[list[str], str, int, Callable[[], bool] | None]:
    log = base / "app.log"
    log.write_text(
        "2026-11-20 INFO user=ana action=login\n"
        "2026-11-20 ERROR user=bob action=timeout\n"
        "2026-11-20 ERROR user=ana action=denied\n"
        + ("2026-11-20 ERROR user=zoe action=missing\n" if variant else ""),
        encoding="utf-8",
    )
    directory = base / "input data"
    directory.mkdir()
    (directory / "a.txt").write_bytes(b"1234")
    (directory / "space name.txt").write_bytes(b"abc")
    (directory / "nested").mkdir()
    (directory / "nested" / "b.txt").write_bytes(b"xy")
    (directory / "nested" / "c.log").write_bytes(b"z" * (2 if variant else 1))
    access = base / "access.log"
    access.write_text(
        "10.0.0.2 GET / 200\n10.0.0.1 GET /a 200\n10.0.0.2 GET /b 404\n"
        + ("10.0.0.1 GET /c 200\n" if variant else ""),
        encoding="utf-8",
    )
    lat = base / "latencies.log"
    lat.write_text(
        "latency_ms=3\nlatency_ms=5\n" if variant
        else "latency_ms=10\nlatency_ms=20\nlatency_ms=30\n",
        encoding="utf-8",
    )
    numbers = base / "numbers.txt"
    numbers.write_text(
        "1\n2\n3\n4\n5\n" if variant
        else "10\n20\n30\n40\n50\n60\n70\n80\n90\n100\n",
        encoding="utf-8",
    )
    units = base / "units.tsv"
    units.write_text(
        "api\tactive\nworker\tactive\n" if variant
        else "api\tactive\nworker\tfailed\ncache\tfailed\n",
        encoding="utf-8",
    )
    source = base / "source.txt"
    source.write_text("payload " + ("SECOND" if variant else "FIRST") + "\n", encoding="utf-8")
    original = base / "application.log"
    original.write_text("line one\n" + ("line two\n" if variant else ""), encoding="utf-8")
    manifest = base / "checksums.txt"
    (base / "checked.txt").write_text("changed" if variant else "valid", encoding="utf-8")
    sha = hashlib.sha256(b"valid").hexdigest()
    manifest.write_text(sha + "  checked.txt\n", encoding="utf-8")

    if id == "B01":
        return [str(log)], str(3 if variant else 2) + "\n", 0, None
    if id == "B02":
        return [str(log)], ("ana\nbob\nzoe\n" if variant else "ana\nbob\n"), 0, None
    if id == "B03":
        return [str(directory)], str(11 if variant else 10) + "\n", 0, None
    if id == "B04":
        return [str(directory)], "a.txt\nnested/b.txt\nspace name.txt\n", 0, None
    if id == "I01":
        return ["65536" if variant else "00080"], "INVALID\n" if variant else "VALID\n", 1 if variant else 0, None
    if id == "I02":
        return [str(access)], ("10.0.0.1 2\n10.0.0.2 2\n" if variant else "10.0.0.2 2\n10.0.0.1 1\n"), 0, None
    if id == "I03":
        return [str(lat)], "4.0\n" if variant else "20.0\n", 0, None
    if id == "I04":
        dst = base / "copy output.txt"
        return [str(source), str(dst)], "", 0, lambda: dst.read_bytes() == source.read_bytes()
    if id == "A01":
        return [str(manifest)], "FAIL\n" if variant else "OK\n", 1 if variant else 0, None
    if id == "A02":
        return [str(numbers)], "5\n" if variant else "90\n", 0, None
    if id == "A03":
        return [str(units)], "NO_FAILURES\n" if variant else "cache\nworker\n", 0, None
    if id == "A04":
        archive = base / "archived.log"
        before = original.read_bytes()
        return [str(original), str(archive)], "", 0, (
            lambda: original.exists() and original.read_bytes() == b"" and archive.read_bytes() == before
        )
    raise ValueError("Unknown fixture ID")


def grade(id: str, reference: bool = False) -> tuple[bool, str]:
    if id not in INDEX:
        raise ValueError(f"Unknown lab: {id}")
    file = ROOT / "labs" / ("reference" if reference else "starter") / INDEX[id]["script"]
    for variant in (0, 1):
        with tempfile.TemporaryDirectory(prefix="swarm-linux-lab-") as tmp:
            base = Path(tmp)
            args, expected, exit_code, verify = fixture(base, id, variant)
            env = dict(os.environ)
            env.update({"HOME": str(base), "LC_ALL": "C"})
            try:
                result = subprocess.run(
                    ["bash", str(file), *args], cwd=base, env=env,
                    capture_output=True, text=True, timeout=5, check=False,
                )
            except subprocess.TimeoutExpired:
                return False, f"{id}, fixture {variant}: timeout"
            valid = result.returncode == exit_code and result.stdout == expected
            if valid and verify is not None:
                try:
                    valid = verify()
                except OSError:
                    valid = False
            if not valid:
                return False, (
                    f"{id}, fixture {variant}: expected exit {exit_code}, stdout {expected!r}; "
                    f"got exit {result.returncode}, stdout {result.stdout!r}, "
                    f"stderr {result.stderr[-300:]!r}"
                )
    return True, f"PASS {id}: both fixtures"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("id", nargs="?", choices=sorted(INDEX))
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--verify-references", action="store_true")
    args = parser.parse_args()

    if args.list:
        for task in TASKS:
            print(f'{task["id"]} | {task["level"]:<13} | {task["title"]}')
        return 0
    if args.verify_references:
        failures = 0
        for id in sorted(INDEX):
            ok, message = grade(id, reference=True)
            print(message)
            failures += not ok
        return int(failures != 0)
    if args.id is None:
        parser.error("Provide a lab ID, --list, or --verify-references")
    ok, message = grade(args.id)
    print(message)
    return int(not ok)


if __name__ == "__main__":
    raise SystemExit(main())
