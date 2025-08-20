# Kubernetes BackupPolicy Operator (Python/Kopf)

A production-grade Kubernetes operator for automating backups of stateful apps using PVC snapshots or S3-compatible storage. Ships with Helm, Prometheus metrics, and CI/CD via GitHub Actions.

## Features
- CustomResourceDefinition: `BackupPolicy`
- PVC snapshot or app-specific backup job
- S3/MinIO backend support
- Prometheus metrics
- Helm chart for install
- CI: unit + e2e on Kind, image to GHCR

## Quickstart
1. Install dependencies: `poetry install`
2. Deploy MinIO (see `examples/minio`)
3. Install operator: `helm install backup-operator charts/backup-operator`
4. Apply a BackupPolicy (see `examples/`)

## Development
- Python 3.11, Kopf, kubernetes, boto3, prometheus_client
- Run locally: `poetry run python -m operator.main`

## License
MIT
