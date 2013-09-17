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

import urllib2
from urlparse import urlparse
import re
from config import *

def getHTMLSourceFrom(url):
    OpenStream = urllib2.urlopen(url)
    Content = OpenStream.read()
    OpenStream.close()
    return Content

def getHrefs(url,html_source):
    Target = urlparse(url)
    HrefPattrenPCRE = re.findall(bootstrap.HrefsPCRE,html_source)
    HrefsList = []
    for Href in HrefPattrenPCRE:
            if re.findall(bootstrap.NoThisList,Href):
                continue
            elif re.findall(bootstrap.LinksCDN,Href):
                continue
            elif re.findall(bootstrap.MissingProtocolForQueryString,Href):
                if Target[0] + "://" + Target[1] + Target[2] + Href in HrefsList:
                    continue
                else:
                    CurrentHostHref = str(Target[0] + "://" + Target[1] + Target[2] + Href)
                    CurrentHOST = urlparse(CurrentHostHref)
                    if (bootstrap.RemoveNotSameHost == 'yes') and (CurrentHOST[1] != Target[1]):
                        continue
                    HrefsList.append(Target[0] + "://" + Target[1] + Target[2]+ Href)
            elif re.findall(bootstrap.MissingProtocolForExternalLinks,Href):
                if Target[0] + "://" + Href in HrefsList:
                    continue
                else:
                    CurrentHostHref = str(Target[0] + "://" + Href)
                    CurrentHOST = urlparse(CurrentHostHref)
                    if (bootstrap.RemoveNotSameHost == 'yes') and (CurrentHOST[1] != Target[1]):
                        continue
                    HrefsList.append(Target[0] + "://" + Href)
            else:
                if Href in HrefsList:
                    continue
                else:
                    CurrentHostHref = str(Href)
                    CurrentHOST = urlparse(CurrentHostHref)
                    if (bootstrap.RemoveNotSameHost == 'yes') and (CurrentHOST[1] != Target[1]):
                        continue
                    HrefsList.append(Href)
    return HrefsList

def getFromURL(url):
    HoldHTML = getHTMLSourceFrom(url)
    return getHrefs(url,HoldHTML)