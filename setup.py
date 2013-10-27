#!/usr/bin/env python
# Copyright (C) 2009 Mat Booth <mat@matbooth.co.uk>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from setuptools import setup

setup(
    name='VisualWorkflow',
    version='0.0.1',
    author='Mat Booth',
    author_email='mat@matbooth.co.uk',
    url='https://github.com/mbooth101/trac-visualworkflow',
    license='BSD',
    description='Visual Trac workflow editor',
    long_description='Adds a visual workflow editor to the admin module.',
    packages=['visualworkflow'],
    package_data={
        'visualworkflow' : [
            'htdocs/css/*.css',
            'htdocs/js/*.js',
            'templates/*.html',
            ]
        },
    entry_points={
        'trac.plugins': [
           'visualworkflow.admin = visualworkflow.admin',
           'visualworkflow.graph = visualworkflow.graph',
           ]
        },
    install_requires = [])
