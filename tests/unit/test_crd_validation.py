import pytest
import yaml
from operator import crd

def test_crd_schema_keys():
    schema = crd.BACKUP_POLICY_CRD
    assert schema["apiVersion"] == "apiextensions.k8s.io/v1"
    assert schema["kind"] == "CustomResourceDefinition"
    assert "spec" in schema
    assert "group" in schema["spec"]
    assert "versions" in schema["spec"]
