#!/usr/bin/env python

from distutils.core import setup

setup(
    name='mockldap',
    version='0.1.0',
    description=u"A simple mock implementation of python-ldap.",
    long_description=open('README').read(),
    url='http://bitbucket.org/psagers/mockldap/',
    author='Peter Sagerson',
    author_email='psagers.pypi@ignorare.net',
    license='BSD',
    packages=['mockldap'],
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['mock', 'ldap'],
    install_requires=[
    ],
)
