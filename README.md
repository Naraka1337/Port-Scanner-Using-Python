# NARAKA Port Scanner

## Description

The **NARAKA Port Scanner** is a Python-based tool that scans a specified target IP address for open ports. It uses multithreading to efficiently check multiple ports simultaneously, greatly reducing the time required for large-scale port scanning.

This tool is designed for educational purposes and simple network diagnostics, helping to identify open TCP ports on a target machine.

## Features

- Scans target IP for open ports.
- Multithreaded to improve performance.
- Customizable port range.
- Easy-to-use with simple command-line input.
- Handles common network errors like unresolvable hostnames and connectivity issues.

## Requirements

- Python 3.x
- Internet connection (for scanning remote targets)
- **Modules**:
  - `socket`
  - `sys`
  - `threading`
  - `datetime`

No additional third-party libraries are required.
