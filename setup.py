#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os.path import dirname, join

from setuptools import find_packages, setup


def read_file(file):
    with open(file, "rt") as f:
        return f.read()


with open(join(dirname(__file__), 'python_templ/VERSION.txt'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
    name='python_templ',
    version=version,
    description='python_templ',
    packages=find_packages(exclude=[]),
    author='Test',
    author_email='*****@**.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='https://github.com/..',  # url of github
    install_requires=read_file("requirements.txt").strip(),  # The required python package
    zip_safe=False,
    # entry_points={
    #     #'console_scripts': [
    #     #    'poinneer-download-data = poinneer.cmd.download:main',
    #     #],
    # },
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)