# ReleaseMonitor

## Overview
**ReleaseMonitor** automatically tracks version updates, numbers, and release dates for popular middleware within microservices architectures.

## Features
- **Real-time Monitoring**: Seamlessly monitors middleware repositories for new updates.
- **Scheduled Scanning**: Configured to perform periodic scans to fetch the latest updates.
- **Data Storage**: Captures and stores release data in structured JSON format for easy usage.

## How to Use
1. Clone the repository to your local environment.
2. Ensure Python 3.x is installed on your system.
3. Run `python fetch_releases.py` from the `scripts` directory to initiate the monitoring of middleware releases.
4. Access the collected data in the `data` directory, formatted as JSON files.

## License
This project is licensed under the [Apache License 2.0](./LICENSE).