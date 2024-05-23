#!/usr/bin/env python

import pathlib
import re

import setuptools
import toml

author_name_and_email_regex = r"([^\<]*)\<(.+)\>"


def _setup():
    setup_data = {}
    pyproject = toml.loads(pathlib.Path("pyproject.toml").read_text())
    author = re.match(
        author_name_and_email_regex, pyproject["tool"]["poetry"]["authors"][0]
    )
    setup_data["author"] = author[1]
    setup_data["author_email"] = author[2]
    setup_data["python_requires"] = ">=3.10"
    setup_data["install_requires"] = [
        f"{key}{value.replace('^', '>=')}"
        for key, value in pyproject["tool"]["poetry"]["dependencies"].items()
        if key != "importlib_metadata"
    ]
    setup_data["name"] = pyproject["tool"]["poetry"]["name"]
    setup_data["version"] = pyproject["tool"]["poetry"]["version"]
    setup_data["description"] = pyproject["tool"]["poetry"]["description"]
    setup_data["long_description"] = pyproject["tool"]["poetry"]["readme"]
    setup_data["license"] = pyproject["tool"]["poetry"]["license"]
    setup_data["url"] = pyproject["tool"]["poetry"]["homepage"]
    setup_data["keywords"] = pyproject["tool"]["poetry"]["homepage"]
    setup_data["classifiers"] = pyproject["tool"]["poetry"]["classifiers"]
    setup_data["url"] = pyproject["tool"]["poetry"]["homepage"]
    setup_data["packages"] = parse_package_name(pyproject["tool"]["poetry"]["packages"])
    setuptools.setup(**setup_data)


def parse_package_name(packages):
    _packages = []
    for package in packages:
        if isinstance(package, dict):
            package = package["include"]
        _packages.append(package)
    return _packages


if __name__ == "__main__":
    _setup()
