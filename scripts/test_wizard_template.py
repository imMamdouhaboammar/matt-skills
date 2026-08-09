#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
template = ROOT / "skills" / "wizard" / "template.sh"
lines = template.read_text().splitlines()
marker = next(i for i, line in enumerate(lines) if "STAGES — author this section" in line)
library = "\n".join(lines[: marker - 1]) + "\n"

with tempfile.TemporaryDirectory() as td:
    env_file = Path(td) / ".env"
    harness = Path(td) / "harness.sh"
    harness.write_text(
        library
        + """
ENV_FILE="$1"
write_env GOOD "alpha=beta"
if write_env BAD $'one\\nINJECTED=1'; then exit 41; fi
if write_env BADCR $'one\\rtwo'; then exit 42; fi
if write_env 'BAD-NAME' "value"; then exit 43; fi
PATH=/definitely-not-a-real-bin open_url "https://example.invalid"
"""
    )
    result = subprocess.run(["bash", str(harness), str(env_file)], text=True, capture_output=True)
    if result.returncode != 0:
        raise SystemExit(result.stdout + result.stderr)
    actual = env_file.read_text()
    assert actual == "GOOD=alpha=beta\n", actual
    combined = result.stdout + result.stderr
    assert "refusing multiline value for BAD" in combined
    assert "refusing multiline value for BADCR" in combined
    assert "invalid environment key: BAD-NAME" in combined
    assert "couldn't open a browser" in combined
print("wizard template safety: PASS")
