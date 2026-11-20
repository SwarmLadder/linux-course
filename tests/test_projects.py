"""Integration smoke tests for three runnable Linux course portfolio examples."""
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
BIN=ROOT/"projects/examples"

def run(name,*args):
    return subprocess.run(["bash",str(BIN/name),*map(str,args)],text=True,
                          capture_output=True,timeout=5,check=False)

class ProjectTests(unittest.TestCase):
    def test_log_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            log=Path(tmp)/"app.log"
            log.write_text("2026 INFO user=ana\n2026 ERROR user=bob\n2026 ERROR user=ana\n")
            p=run("log_summary.sh",log)
            self.assertEqual(p.returncode,0,p.stderr)
            self.assertEqual(p.stdout,"records=3\nerrors=2\nunique_users=2\n")
            log.write_text("")
            self.assertEqual(run("log_summary.sh",log).stdout,
                             "records=0\nerrors=0\nunique_users=0\n")

    def test_release_and_rollback(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            artifact=root/"artifact.bin"
            artifact.write_bytes(b"v1")
            deployed=run("release_simulator.sh",artifact,"v1",root)
            self.assertEqual(deployed.returncode,0,deployed.stderr)
            self.assertEqual((root/"current/app.txt").read_bytes(),b"v1")
            artifact.write_bytes(b"v2")
            deployed=run("release_simulator.sh",artifact,"v2",root)
            self.assertEqual(deployed.returncode,0,deployed.stderr)
            self.assertEqual((root/"current/app.txt").read_bytes(),b"v2")
            again=run("release_simulator.sh",artifact,"v2",root)
            self.assertNotEqual(again.returncode,0)
            self.assertEqual((root/"current/app.txt").read_bytes(),b"v2")
            rollback=run("rollback_release.sh",root,"v1")
            self.assertEqual(rollback.returncode,0,rollback.stderr)
            self.assertEqual((root/"current/app.txt").read_bytes(),b"v1")

    def test_reject_bad_release_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            source=root/"file.txt"
            source.write_text("ok")
            self.assertNotEqual(run("release_simulator.sh",source,"../escape",root).returncode,0)

    def test_operations_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            lat=root/"latencies.txt"
            units=root/"units.tsv"
            lat.write_text("10\n20\n30\n40\n50\n")
            units.write_text("api\tactive\nworker\tactive\n")
            ok=run("operations_report.sh",lat,units,"50")
            self.assertEqual(ok.returncode,0,ok.stderr)
            self.assertEqual(ok.stdout,"status=OK\np90_ms=50\nfailed_units=0\n")
            units.write_text("api\tactive\nworker\tfailed\n")
            bad=run("operations_report.sh",lat,units,"40")
            self.assertEqual(bad.returncode,0,bad.stderr)
            self.assertEqual(bad.stdout,"status=DEGRADED\np90_ms=50\nfailed_units=1\n")

if __name__=="__main__":
    unittest.main()
