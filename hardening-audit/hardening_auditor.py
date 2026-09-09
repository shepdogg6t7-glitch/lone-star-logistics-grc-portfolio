#!/usr/bin/env python3
"""
Lone Star Logistics — System Hardening Auditor
Validates a Linux host against a subset of the CIS Ubuntu Benchmark,
mapped to the Access Control Policy (LSL-POL-AC-001).

Run with: python3 hardening_auditor.py
Some checks require sudo to read protected files — the script will
mark those "UNABLE TO VERIFY" rather than fail silently if access is denied.
"""

import subprocess
import re
import os
from dataclasses import dataclass, field


@dataclass
class CheckResult:
    check_id: str
    description: str
    status: str  # "PASS", "FAIL", "UNABLE TO VERIFY"
    detail: str = ""


results: list[CheckResult] = []


def run_cmd(cmd: str) -> tuple[int, str]:
    """Run a shell command, return (exit_code, combined_output)."""
    proc = subprocess.run(
        cmd, shell=True, capture_output=True, text=True
    )
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def read_file_safe(path: str) -> str | None:
    try:
        with open(path, "r") as f:
            return f.read()
    except PermissionError:
        return None
    except FileNotFoundError:
        return None


def check_ssh_root_login():
    content = read_file_safe("/etc/ssh/sshd_config")
    if content is None:
        results.append(CheckResult(
            "CIS-5.2.10", "SSH root login disabled", "UNABLE TO VERIFY",
            "Could not read /etc/ssh/sshd_config (permissions or file missing)"
        ))
        return
    match = re.search(r"^\s*PermitRootLogin\s+(\S+)", content, re.MULTILINE)
    if match and match.group(1).lower() in ("no",):
        results.append(CheckResult("CIS-5.2.10", "SSH root login disabled", "PASS"))
    else:
        found = match.group(1) if match else "not set (defaults may allow root login)"
        results.append(CheckResult(
            "CIS-5.2.10", "SSH root login disabled", "FAIL",
            f"PermitRootLogin is '{found}', expected 'no'"
        ))


def check_ssh_password_auth():
    content = read_file_safe("/etc/ssh/sshd_config")
    if content is None:
        results.append(CheckResult(
            "CIS-5.2.11", "SSH password authentication disabled", "UNABLE TO VERIFY",
            "Could not read /etc/ssh/sshd_config"
        ))
        return
    match = re.search(r"^\s*PasswordAuthentication\s+(\S+)", content, re.MULTILINE)
    if match and match.group(1).lower() == "no":
        results.append(CheckResult("CIS-5.2.11", "SSH password authentication disabled", "PASS"))
    else:
        found = match.group(1) if match else "not set (defaults typically allow password auth)"
        results.append(CheckResult(
            "CIS-5.2.11", "SSH password authentication disabled", "FAIL",
            f"PasswordAuthentication is '{found}', expected 'no'"
        ))


def check_ufw_active():
    code, output = run_cmd("sudo -n ufw status 2>&1")
    if "permission denied" in output.lower() or code != 0 and "sudo" in output.lower():
        results.append(CheckResult(
            "CIS-3.5.1", "UFW firewall active", "UNABLE TO VERIFY",
            "Requires sudo privileges to check ufw status"
        ))
        return
    if "Status: active" in output:
        results.append(CheckResult("CIS-3.5.1", "UFW firewall active", "PASS"))
    else:
        results.append(CheckResult(
            "CIS-3.5.1", "UFW firewall active", "FAIL",
            f"ufw status output: '{output}'"
        ))


def check_auto_updates():
    installed = os.path.exists("/etc/apt/apt.conf.d/20auto-upgrades")
    if not installed:
        results.append(CheckResult(
            "CIS-1.1.1", "Automatic security updates enabled", "FAIL",
            "unattended-upgrades config not found — package likely not installed/configured"
        ))
        return
    content = read_file_safe("/etc/apt/apt.conf.d/20auto-upgrades") or ""
    if 'Unattended-Upgrade "1"' in content:
        results.append(CheckResult("CIS-1.1.1", "Automatic security updates enabled", "PASS"))
    else:
        results.append(CheckResult(
            "CIS-1.1.1", "Automatic security updates enabled", "FAIL",
            "Config file exists but automatic upgrades are not enabled"
        ))


def check_password_min_length():
    content = read_file_safe("/etc/security/pwquality.conf")
    if content is None:
        results.append(CheckResult(
            "CIS-5.4.1", "Password minimum length >= 14", "UNABLE TO VERIFY",
            "Could not read /etc/security/pwquality.conf"
        ))
        return
    match = re.search(r"^\s*minlen\s*=\s*(\d+)", content, re.MULTILINE)
    if match and int(match.group(1)) >= 14:
        results.append(CheckResult("CIS-5.4.1", "Password minimum length >= 14", "PASS"))
    else:
        found = match.group(1) if match else "not set (default is typically weaker)"
        results.append(CheckResult(
            "CIS-5.4.1", "Password minimum length >= 14", "FAIL",
            f"minlen is '{found}', expected >= 14"
        ))


def check_no_extra_uid0():
    content = read_file_safe("/etc/passwd")
    if content is None:
        results.append(CheckResult(
            "CIS-6.2.9", "No unauthorized UID 0 accounts", "UNABLE TO VERIFY",
            "Could not read /etc/passwd"
        ))
        return
    uid0_users = [
        line.split(":")[0] for line in content.splitlines()
        if len(line.split(":")) > 2 and line.split(":")[2] == "0"
    ]
    if uid0_users == ["root"]:
        results.append(CheckResult("CIS-6.2.9", "No unauthorized UID 0 accounts", "PASS"))
    else:
        results.append(CheckResult(
            "CIS-6.2.9", "No unauthorized UID 0 accounts", "FAIL",
            f"UID 0 accounts found: {uid0_users}"
        ))


def manual_check_access_review():
    results.append(CheckResult(
        "N/A", "Quarterly access review documented (manual/process control)",
        "MANUAL — NOT AUTOMATED",
        "Verify separately against the Access Control Policy §3.4 attestation record"
    ))


def main():
    print("=" * 70)
    print("Lone Star Logistics — System Hardening Auditor")
    print("Validating against Access Control Policy (LSL-POL-AC-001)")
    print("=" * 70)

    check_ssh_root_login()
    check_ssh_password_auth()
    check_ufw_active()
    check_auto_updates()
    check_password_min_length()
    check_no_extra_uid0()
    manual_check_access_review()

    print()
    passed = failed = unable = manual = 0
    for r in results:
        symbol = {
            "PASS": "[PASS]",
            "FAIL": "[FAIL]",
            "UNABLE TO VERIFY": "[????]",
            "MANUAL — NOT AUTOMATED": "[MANL]",
        }.get(r.status, "[????]")
        print(f"{symbol} {r.check_id:<12} {r.description}")
        if r.detail:
            print(f"         -> {r.detail}")

        if r.status == "PASS":
            passed += 1
        elif r.status == "FAIL":
            failed += 1
        elif r.status == "UNABLE TO VERIFY":
            unable += 1
        else:
            manual += 1

    print()
    print("=" * 70)
    print(f"Summary: {passed} passed, {failed} failed, {unable} unable to verify, {manual} manual")
    print("=" * 70)


if __name__ == "__main__":
    main()
