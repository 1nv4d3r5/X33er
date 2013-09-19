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
from libs.common import *
from libs.core.helpdesk import *
import sys

print "###########################################";
print "          | |/_// __// __//  |/  /___      "
print "          _>  < _\ \ _\ \ / /|_/ // -_)    "
print "         /_/|_|/___//___//_/  /_/ \__/     "
print ":.....::.....:..:..:..:.....::.....::.....:"
print ":::::::::::The Aut0Ma@tic XSS3r:::::::::::::"
print ":.....::.....:..:..:..:.....::.....::.....:\n"

if len(sys.argv) < 2:
    print "usage: python xsser.py --url=\"http://victim.com?parameter=value\"\nFor Help: can use python xsser.py --help for commands list and usage"
    sys.exit(0)

Doc = sys.argv[1];
if Doc == "--help":
    doc.docHelp()
    sys.exit(0)

Target = sys.argv[1];
Type = sys.argv[2];
TypeMe = Type.replace("--type=","")
urlInput = Target.replace("--url=","")
print "[ + ] Check the connection with the remote victim..."
try:
    GettingAllLinks = scan.getFromURL(urlInput);
except BaseException,e:
    print "[ !!! ] Please check again the URL or re-check your internet connection."
    sys.exit(0)

if TypeMe == "basic":
    print "[ ~ ] Analayze links on the page, it could take a moment.."
    GettingAllLinks = scan.getFromURL(urlInput);
    print "[ ~ ] Okay, we got the links... Start X33er Basic Audit.."
    for Link in GettingAllLinks:
        injector.RunAudit(urlInput)
elif TypeMe == "input":
    print "[ ~ ] Analayze links on the page, it could take a moment.."
    GettingAllLinks = scan.getFromURL(urlInput);
    print "[ ~ ] Okay, we got the links... Start X33er Input Audit.."
    for v,x in basic.Payloads.iteritems():
        print "[ ~ ] Testing " + v + "..."
        injector.RunAuditWithCustomPayload(urlInput,x,basic.PayloadsPCRE[v])
elif TypeMe == "js":
    print "[ ~ ] Analayze links on the page, it could take a moment.."
    GettingAllLinks = scan.getFromURL(urlInput);
    print "[ ~ ] Okay, we got the links... Start X33er JavaScript Audit.."
    for v,x in jsfile.Payloads.iteritems():
        print "[ ~ ] Testing " + v + "..."
        injector.RunAuditWithCustomPayload(urlInput,x,jsfile.PayloadsPCRE[v])
else:
    print "[ ~ ] Analayze links on the page, it could take a moment.."
    GettingAllLinks = scan.getFromURL(urlInput);
    print "[ ~ ] Okay, we got the links... Start X33er Basic Audit.."
    for Link in GettingAllLinks:
        injector.RunAudit(urlInput)