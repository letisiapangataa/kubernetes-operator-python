import kopf
import logging
from . import crd
from . import s3
from . import snapshots
from . import metrics

# Kopf event handlers will be added here

if __name__ == "__main__":
    kopf.run()
