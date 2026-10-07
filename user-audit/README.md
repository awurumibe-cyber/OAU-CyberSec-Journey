# Linux Security Audit Tool

## Overview

A Python-based Linux security auditing tool built on Kali Linux.

The tool collects and analyzes basic system security information and generates a machine-readable JSON security report.

## Security Checks

The tool currently checks:

- User accounts and account types
- Sudo/administrative users
- Authentication failures
- Disk usage
- Listening network ports

## Technologies

- Python 3
- Linux / Kali Linux
- `/etc/passwd`
- `/etc/group`
- `journalctl`
- `ss`
- JSON

## Output

The tool produces:

- Terminal-based security findings
- `audit_report.json` containing structured audit results

## What I Learned

- Reading and parsing Linux system files
- Working with UIDs and login shells
- Identifying privileged accounts
- Using Linux commands from Python
- Processing authentication logs
- Checking disk and network information
- Creating structured JSON security reports
