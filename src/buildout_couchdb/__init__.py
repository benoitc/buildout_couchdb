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

"""
zc buildout recipe for Apache CouchDB server
"""
from __future__ import with_statement
import ConfigParser
import os
import os.path
import pkg_resources

import zc.recipe.cmmi
from zc.recipe.cmmi import system

config_file = pkg_resources.resource_stream(__name__, "defaults.cfg")
config = ConfigParser.ConfigParser()
config.readfp(config_file)

class Recipe(zc.recipe.cmmi.Recipe):
    """zc.buildout recipe for building an Apache CouchDB server from source.

    Configuration options:
        url
        md5sum
        extra-options
        extra-vars
        local_ini
    """

    def __init__(self, buildout, name, options):
        self.inifile = options.pop("local_ini", None)
        for key, value in config.items("couchdb"):
            options.setdefault(key, value)
        super(Recipe, self).__init__(buildout, name, options)

    def cmmi(self, dest):
        """Do the 'configure; make; make install' command sequence.

        When this is called, the current working directory is the
        source directory.  The 'dest' parameter specifies the
        installation prefix.

        This can be overridden by subclasses to support packages whose
        command sequence is different.
        """
        options = self.configure_options
        
        if options is None:
            options = '--prefix=%s' % dest
        if self.extra_options:
            options += ' %s' % self.extra_options
            
        system("%s %s" % (self.configure_cmd, options))
        system("make")
        system("make install")
            
        if self.inifile is not None:
            iniddest = os.path.join(dest, "etc/couchdb")
            inifile_dest = os.path.join(iniddest, self.inifile)
            try:
                os.makedirs(iniddest)
            except:
                pass
            if os.path.isfile(self.inifile):
                with open(self.inifile, "r") as f:
                    ft = open(inifile_dest, "w")
                    ft.write(f.read(self.inifile))
                    ft.close()
            
            