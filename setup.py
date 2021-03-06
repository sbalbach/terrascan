#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'terraform-validate==3.1.16',
]

setup(
    name='terrascan',
    version='2.1.7',
    description="Best practices tests for terraform",
    long_description=readme,
    author="Cesar Rodriguez",
    author_email='therasec@gmail.com',
    url='https://github.com/cesar-rodriguez/terrascan',
    download_url='https://github.com/cesar-rodriguez/terrascan' +
    '/archive/v0.1.1.tar.gz',
    packages=find_packages(where='.'),
    entry_points={
        'console_scripts': [
            'terrascan = terrascan.__main__:main',
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='terrascan',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
    tests_require=requirements,
    setup_requires=requirements,
)
