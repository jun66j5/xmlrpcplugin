#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='TracXMLRPC',
    version='1.0.3',
    license='BSD',
    author='Alec Thomas',
    author_email='alec@swapoff.org',
    url='http://trac-hacks.org/wiki/XmlRpcPlugin',
    description='XML-RPC interface to Trac',
    zip_safe=True,
    test_suite = 'tracrpc.tests.suite',
    packages=find_packages(exclude=['*.tests']),
    package_data={
        'tracrpc': ['templates/*.html']
        },
    entry_points={
        'trac.plugins': 'TracXMLRPC = tracrpc'
        },
    )
