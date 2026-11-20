# Project 3 — Backend incident operations report

**Goal:** Produce a small, reproducible health report from synthetic latency numbers and service-unit statuses.

## Contract

Input: a file of integer latencies (milliseconds), a TSV list of NAME/STATUS, and a positive integer latency threshold. Output status=OK/DEGRADED, p90_ms and failed_units.

## Deliverables

1. Validate paths and numeric threshold before reading input.
2. Implement nearest-rank p90; explicitly define the behavior of empty data.
3. Count exactly the units whose status is failed.
4. Report DEGRADED when p90 exceeds the threshold or any service has failed.
5. Add tests for missing files, empty samples, malformed records, and the threshold boundary.

## Try the reference

```bash
work=$(mktemp -d)
printf '10\n20\n30\n50\n100\n' > "$work/latencies.txt"
printf 'api\tactive\nworker\tfailed\n' > "$work/units.tsv"
bash projects/examples/operations_report.sh "$work/latencies.txt" "$work/units.tsv" 80
```

**Expected:** status=DEGRADED, p90_ms=100, failed_units=1.

**Extensions:** add sustained error-rate windows, clear alert policies, structured JSON and a one-page incident runbook.

**Interview:** Explain why a sample's p90 alone cannot establish production SLO health.
