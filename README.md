# ReleaseMonitor

## Overview
**ReleaseMonitor** automatically tracks version updates, numbers, and release dates for popular software components used in microservices architectures.

## Features
- **Real-time Monitoring**: Seamlessly monitors software repositories for new updates.
- **Scheduled Scanning**: Configured to perform periodic scans to fetch the latest updates.
- **Data Storage**: Captures and stores release data in structured JSON format for easy usage.

## Supported Software Components
The following software components are currently supported by ReleaseMonitor:

- Elasticsearch
- KKFileView
- MinIO
- Nacos
- Nginx
- RabbitMQ Server
- Redis
- Harbor
- Docker
- Docker Compose
- Kubernetes (K8s)

## How to Use
1. Clone the repository to your local environment.
2. Ensure Python 3.x is installed on your system.
3. Run `python fetch_releases.py` from the `scripts` directory to initiate the monitoring of software releases.
4. Access the collected data in the `data` directory, formatted as JSON files.

## License
This project is licensed under the [Apache License 2.0](./LICENSE).