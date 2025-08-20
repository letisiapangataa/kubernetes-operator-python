#!/bin/bash
set -e
# E2E test: deploy chart, create BackupPolicy, check resources
helm install backup-operator ../../charts/backup-operator
kubectl apply -f ../../examples/backuppolicy-snapshots.yaml
sleep 10
kubectl get backuppolicies.backup.dev
