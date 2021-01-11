from setuptools import setup

setup(
    name="reda-2021-workflow-audit-tracker",
    version="0.1.0",
    description="Traceability utilities for pipeline runs, parameters, and audit checkpoints.",
    author="Red@",
    packages=["workflow_audit_tracker"],
    package_dir={"": "src"},
)
