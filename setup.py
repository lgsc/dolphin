import os
from setuptools import find_packages
from distutils.core import setup

THIS_DIR = os.path.abspath(os.path.dirname(__file__))


def main():
    with open(os.path.join(THIS_DIR, 'requirements.txt')) as reqs:
        requirements = reqs.read().strip().split('\n')

    setup(
        version="0.0.0",
        name="dolphin",
        packages=find_packages(),
        install_requires=requirements
    )


if __name__ == "__main__":
    main()
