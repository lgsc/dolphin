import os
from setuptools import find_packages
from distutils.core import setup

THIS_DIR = os.path.abspath(os.path.dirname(__file__))


def main():
    with open(os.path.join(THIS_DIR, 'requirements.txt')) as reqs:
        requirements = reqs.read().strip().split('\n')

    setup(
        name="dolphin",
        version='0.1.0',
        py_modules=['find_blocks'],
        packages=find_packages(),
        install_requires=requirements,
        entry_points='''
            [console_scripts]
            findBlocks=dolphin.find_blocks:main
        '''
    )


if __name__ == "__main__":
    main()
