from setuptools import find_packages, setup

setup(
    name="gbif_data",
    packages=find_packages(exclude=["gbif_data_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
