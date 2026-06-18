from setuptools import find_packages, setup

setup(
    name="uipath-agenthack-service-recovery",
    version="0.1.0",
    description="Local provisional core for governed telecom service recovery.",
    packages=find_packages(include=["service_recovery_core*"]),
    python_requires=">=3.9",
)
