import os
import platform

from pip.download import PipSession
from pip.req import parse_requirements
from setuptools import setup, find_packages

basedir = os.path.dirname(__file__)


def get_dependencies():
    return [str(ir.req) for ir in parse_requirements(
            os.path.join(basedir, 'requirements.txt'), session=PipSession())]


def get_entry_points():
    return {
        'console_scripts': [
            'mro = mro.bin.api:main'
        ]
    }


setup(
    name='mro',
    version='0.0.1',
    url='https://github.com/jlopex/mro_test_project',
    description='MRO',
    packages=find_packages(exclude=['tests']),
    test_suite='tests',
    dependency_links=[],
    install_requires=get_dependencies(),
    package_data={'': ['*.json', '*.ini']},
    include_package_data=True,
    entry_points=get_entry_points()
)
