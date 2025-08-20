# Prometheus metrics exporter
from prometheus_client import start_http_server, Counter, Summary

backup_success = Counter('backup_success_total', 'Number of successful backups')
backup_failure = Counter('backup_failure_total', 'Number of failed backups')
backup_duration = Summary('backup_duration_seconds', 'Time spent on backups')

def start_metrics_server(port=8000):
    start_http_server(port)
