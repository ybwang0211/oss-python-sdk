#!/usr/bin/env python


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md', 'rb') as f:
    readme = f.read().decode('utf-8')

setup(
    name='oss-python-sdk',
    version='1.0.0',
    description='OSS Python SDK',
    author='OSS Cloud',
    author_email='',
    long_description=readme,
    packages=['oss'],
    install_requires=['requests!=2.9.0', 'crcmod>=1.7'],
    include_package_data=True,
    url='https://cloud.oss.com/'
)
