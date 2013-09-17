#!/usr/bin/env python

"""
Copyright (c) 2013 X33er Project
X33er is free software: you can redistribute it and / or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

X33er is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
@for more information see <http://www.gnu.org/licenses/>
"""

from libs.crawler import scan
from libs.crawler import injector
import sys

print "###########################################";
print "          | |/_// __// __//  |/  /___      "
print "          _>  < _\ \ _\ \ / /|_/ // -_)    "
print "         /_/|_|/___//___//_/  /_/ \__/     "
print ":.....::.....:..:..:..:.....::.....::.....:"
print ":::::::::::The Aut0Ma@tic XSS3r:::::::::::::"
print ":.....::.....:..:..:..:.....::.....::.....:\n"

if len(sys.argv) < 2:
    print "usage: python xsser.py --target=\"http://victim.com?parameter=value\""
    sys.exit(0)

userLink = sys.argv[1];
GettingAllLinks = scan.getFromURL(userLink.replace("--target=",""));
for Link in GettingAllLinks:
    injector.RunAudit(Link)
