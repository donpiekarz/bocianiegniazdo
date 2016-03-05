#!/usr/bin/env python

import os

from setuptools import setup

from applicationer import VERSION

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), 'rU') as f:
    long_description = f.read()

required = [
    'scapy',
    'scapy-ssl_tls'
]

extras = {

}

setup(
    name='bocianiegniazdo',
    version=VERSION,
    packages=['applicationer'],
    url='https://github.com/donpiekarz/bocianiegniazdo',
    download_url='https://github.com/donpiekarz/bocianiegniazdo/tarball/' + VERSION,
    license='BSD',
    author='Bartlomiej Piekarski',
    author_email='bartlomiej.piekarski@gmail.com',
    description='realtime auditor of SSL/TLS connections',
    long_description=long_description,
    entry_points={
        'console_scripts': ['bocianiegniazdo = applicationer.application:main']
    },
    install_requires=required,
    extras_require=extras,
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)
