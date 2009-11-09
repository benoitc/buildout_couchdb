# Copyright (c) 2007-2009 Thomas Lotze
# See also LICENSE.txt

"""Test suite for buildout_couchdb
"""

import re
import unittest

import zope.testing.doctest
import zope.testing.renormalizing
import zc.buildout.testing


flags = (zope.testing.doctest.NORMALIZE_WHITESPACE |
         zope.testing.doctest.ELLIPSIS |
         zope.testing.doctest.REPORT_NDIFF)


def setUp(test):
    import zc.recipe.cmmi
    import buildout_couchdb
    zc.buildout.testing.buildoutSetUp(test)
    zc.buildout.testing.install_develop("zc.recipe.cmmi", test)
    zc.buildout.testing.install_develop("buildout_couchdb", test)


# XXX patch normalize_path to cope with --prefix=/sample-buildout/...
regex, _normalize_path = zc.buildout.testing.normalize_path
pattern = regex.pattern[:2] + '=' + regex.pattern[2:]
normalize_path = (re.compile(pattern), _normalize_path)


checker = zope.testing.renormalizing.RENormalizing([
    normalize_path,
    ])


def test_suite():
    return unittest.TestSuite((
        zope.testing.doctest.DocFileSuite(
        "couchdb.txt",
        setUp=setUp,
        tearDown=zc.buildout.testing.buildoutTearDown,
        package="buildout_couchdb",
        optionflags=flags,
        checker=checker,
        ),
        ))


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')