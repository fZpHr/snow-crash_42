# SnowCrash

Introductory security wargame (42). Fifteen flags on a hardened Linux host,
each requiring a different weakness to move from one user to the next. A
developer-oriented tour of how simple mistakes become security issues.

Each `flagXX/` directory holds a writeup of the method used.

## Areas covered

- Credential recovery and offline password cracking (John the Ripper)
- Traffic analysis: following a TCP stream from a packet capture
- Reverse engineering small binaries to recover expected input
- Scripting languages used insecurely (PHP, Perl, Lua)
- SUID binaries and environment/`PATH` abuse
- Cron and scheduled-task abuse
- Race conditions and insecure temporary files
- Unpacking base64-wrapped binaries for analysis

## Concepts

Linux privilege escalation, setuid semantics, cron, pcap analysis, and
reversing. Tooling: gdb, objdump, Wireshark/tcpdump, John.

> Educational material. The target is an intentionally vulnerable 42 wargame.
