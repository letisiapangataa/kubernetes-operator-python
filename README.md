# ❄️ Kubernetes BackupPolicy Operator – Python/Kopf (Applied Lab Project)  

A **proof-of-concept Kubernetes operator** built to explore custom resource development and automation.  
The operator manages backups for stateful applications using PVC snapshots or S3-compatible storage.  
Includes a Helm chart for testing, basic Prometheus metrics, and a simple CI/CD pipeline with GitHub Actions.

For a lab overview : https://letisiapangataa.github.io/posts/kubernetes-backup-operator-python/

---

## Features  
- Custom Resource Definition: `BackupPolicy`  
- Automates PVC snapshots or app-specific backup jobs  
- Supports S3/MinIO storage backends  
- Exposes basic Prometheus metrics  
- Helm chart for easier installation and testing  
- CI: unit tests and Kind-based e2e runs, image published to GHCR  

---

## Quickstart  
1. Install dependencies:  
   ```bash
   poetry install
   ```

2. Deploy MinIO (see `examples/minio`)
3. Install the operator:

   ```bash
   helm install backup-operator charts/backup-operator
   ```
4. Apply a BackupPolicy (see `examples/`)

---

## Development

* Python 3.11
* Kopf (Kubernetes Operator Framework)
* kubernetes (Python client)
* boto3
* prometheus\_client

Run locally:

```bash
poetry run python -m operator.main
```

---

## 📄 License

MIT
