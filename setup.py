# -*- coding: utf-8 -
# Copyright (c) 2009 Benoit Chesneau <benoitc@e-engura.com> 
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
import os.path
import glob


from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages



project_path = lambda *names: os.path.join(os.path.dirname(__file__), *names)

setup(
    name = "buildout_couchdb",
    version = "0.1",
    description = "ZC buildout recipe for Apache CouchDB server",
    long_description = "ZC buildout recipe for Apache CouchDB server",
    author = 'Benoit Chesneau',
    author_email = 'benoitc@e-engura.com',
    license = 'Apache License 2',
    url = "http://github.com/benoitc/buildout_couchdb",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Software Distribution',
    ],
    package_dir = {'':'src'},
    packages = find_packages('src'),
    include_package_data = True,
    entry_points = {'zc.buildout': ['default = buildout_couchdb:Recipe']},
    install_requires = [
        "distribute",
        "zc.buildout",
        "zc.recipe.cmmi"
    ],
    zip_safe=True,
    )