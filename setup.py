#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path
import re, io

def _readme():
    with open('README.rst') as readme_file:
        return readme_file.read().replace(":copyright:", "(c)")

def _requirements():
    root_dir = path.abspath(path.dirname(__file__))
    return [name.rstrip() for name in open(path.join(root_dir, 'requirements.txt')).readlines()]

def _get_version():
    version = re.search(
        r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
        io.open('jamorasep/__init__.py', encoding='utf_8_sig').read()
        ).group(1)
    return version

requirements = _requirements()
setup_requirements = [ ]
test_requirements = _requirements()

setup(
    author="Hideyuki Tachibana",
    author_email='h_tachibana@pkshatec.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Japanese',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        ],
    description="Japanese mora separator",
    install_requires=requirements,
    license='MIT',
    long_description=_readme(),
    include_package_data=True,
    keywords='jpyomi',
    name='morasep',
    packages=find_packages(include=['jamorasep', 'jamorasep.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tachi-hi/jamorasep',
    version=_get_version(),
    zip_safe=False,
)
