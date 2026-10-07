import subprocess
import shutil
import json

print("User Audit Tool")
print("================")
print("Checking user account ...")

audit_report = {}

# =========================
# USER ACCOUNT AUDIT
# =========================

users = []

with open("/etc/passwd", "r") as file:
    for line in file:
        fields = line.strip().split(":")

        username = fields[0]
        uid = int(fields[2])
        shell = fields[6]

        if uid == 0:
            account_type = "PRIVILEGED"
        elif shell in ["/usr/sbin/nologin", "/bin/false"]:
            account_type = "SYSTEM ACCOUNT"
        elif uid >= 1000:
            account_type = "LIKELY HUMAN USER"
        else:
            account_type = "SYSTEM ACCOUNT"

        users.append({
            "username": username,
            "uid": uid,
            "account_type": account_type,
            "shell": shell
        })

        print(f"{username:<18} UID: {uid:<5} {account_type}")

audit_report["users"] = users


# =========================
# SUDO GROUP AUDIT
# =========================

print()
print("SUDO GROUP MEMBERS")
print("==================")

sudo_users = []

with open("/etc/group", "r") as file:
    for line in file:
        if line.startswith("sudo:"):
            fields = line.strip().split(":")
            members = fields[3]

            if members:
                print(f"{members} — ADMINISTRATIVE ACCESS")
                sudo_users.extend(members.split(","))

audit_report["sudo_users"] = sudo_users


# =========================
# AUTHENTICATION AUDIT
# =========================

print()
print("AUTHENTICATION FAILURES")
print("=======================")

failed_attempts = 0

result = subprocess.run(
    ["journalctl", "--no-pager"],
    capture_output=True,
    text=True
)

for line in result.stdout.splitlines():
    if "authentication failure" in line.lower():
        failed_attempts += 1

print(f"Failed authentication attempts: {failed_attempts}")

audit_report["authentication_failures"] = failed_attempts


# =========================
# DISK SPACE AUDIT
# =========================

print()
print("DISK SPACE")
print("==========")

total, used, free = shutil.disk_usage("/")

used_percent = (used / total) * 100

print(f"Total: {total / (1024**3):.2f} GB")
print(f"Used: {used / (1024**3):.2f} GB")
print(f"Free: {free / (1024**3):.2f} GB")
print(f"Usage: {used_percent:.1f}%")

audit_report["disk_space"] = {
    "total_gb": round(total / (1024**3), 2),
    "used_gb": round(used / (1024**3), 2),
    "free_gb": round(free / (1024**3), 2),
    "usage_percent": round(used_percent, 1)
}


# =========================
# OPEN PORT AUDIT
# =========================

print()
print("OPEN PORTS")
print("==========")

result = subprocess.run(
    ["ss", "-tuln"],
    capture_output=True,
    text=True
)

lines = result.stdout.splitlines()

open_ports = []

for line in lines[1:]:
    if line.strip():
        print(line)
        open_ports.append(line.strip())

audit_report["open_ports"] = open_ports


# =========================
# SAVE JSON REPORT
# =========================

with open("audit_report.json", "w") as file:
    json.dump(audit_report, file, indent=4)

print()
print("REPORT SAVED")
print("============")
print("audit_report.json created successfully")
