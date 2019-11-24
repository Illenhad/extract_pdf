#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import extract_pdf

setup(
    name='extract_pdf',
    version=extract_pdf.__version__,
    packages=find_packages(),
    author="Illenhad",
    author_email="pierrelegrand.pro@gmail.com",
    description="Extract PDF pages",
    long_description=open('README.md').read(),
    install_requires=["pypdf2"],
    include_package_data=True,
    url='',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Pre-Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
    entry_points={
        'console_scripts': {
            'extract-extract_pdf = extract_pdf.core:extract',
        },
    }
)
