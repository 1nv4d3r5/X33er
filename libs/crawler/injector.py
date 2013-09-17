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

from urlparse import urlparse
from urllib2 import HTTPError
import re
import sys
from libs.crawler import scan
from config import *

def RunAudit(URL):
    PayloadsURL = {}
    URLtoReplaceIn = str(URL);
    onlyQueryString = urlparse(URL).query
    SepertedParams = onlyQueryString.split("&")
    for Query in SepertedParams:
        SplitParams = Query.split("=")
        NameParam = SplitParams[0]
        if len(SplitParams) < 2:
            MissingValue = "?" + NameParam + "=" + bootstrap.Payload
            PayloadsURL[NameParam] = URLtoReplaceIn.replace("?" + NameParam,MissingValue)
        else:
            ValueParam = SplitParams[1]
            PayloadsURL[NameParam] = URLtoReplaceIn.replace(ValueParam,bootstrap.Payload)
    for Payload in PayloadsURL:
        try:
            data = scan.getHTMLSourceFrom(PayloadsURL[Payload])
            regex = re.search(bootstrap.PCREPayload,data)
            if regex:
                print "[ + ] Ohhh yes !! We FOUND vulnerability in " + Payload + " ! \n The URL is: " + PayloadsURL[Payload]
                sys.exit(0);
            else:
                print '[ + ] Try to Inject in ' + PayloadsURL[Payload] + '..'
        except HTTPError, e:
            print '[ -] Sorry in ' + PayloadsURL[Payload] + ' we can\'t reach the page';
        finally:
            print '[ + ] Operation for ' + PayloadsURL[Payload] + ' has been done.. '