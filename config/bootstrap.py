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

###################################
# XS33er CONFIGURATION             #
###################################

######### Injection Flaws #######
# This setting will allow you decide what the payloads
# you are about to use during you audit
# You need to provide a PCRE for this setting.
# for PCRE doc information see:
# http://docs.python.org/2/library/re.html
######################################
# Here you set the payload
Payload = "'><\""
# Here you set the same payload but in PCRE for the engine
PCREPayload = '\'\>\<\"'

######### Non-Same HOST #######
# This setting will allow you to exclude links
# that doesn't have the same HOST in the victim
# that's good if you want to remove any 3rd links
# for example: www.example.com != www.google.com
# @defaultSetting = no
# @Settings:
#  [+] no - Scan ALL kinds of links
#  [+] yes - Ignore in Scan a different hosts
######################################
RemoveNotSameHost = 'no'

######### Detection Links Engine #######
# In This setting you will decide how the XS33er should
# looking for an a external links in the source code
# You need to provide a PCRE for this setting.
# for PCRE doc information see:
# http://docs.python.org/2/library/re.html
######################################
HrefsPCRE = 'href=\"(.*?)\"'

######### Explict Links #######
# What types of links the XSS3er will skip and
# didn't take in account during the audit?
# You can provide in PCRE list of explict links.
# for PCRE information see:
# http://docs.python.org/2/library/re.html
######################################
NoThisList = r'\.css|\.js|\.png|\.jpeg|\.jpg|\.gif|\.ico|\.xml'

######### NO CDN Links #######
# The scanning will IGNORE any links of external CDN
# such as GoogleAPI, JQuery CDN and etc.
# for PCRE information see:
# http://docs.python.org/2/library/re.html
######################################
LinksCDN = '^\/\/[a-zA-z]+'

######### Missing HTTP Protocol #######
# The scanning will add any links with missing HTTP
# like in the code <a href='index.php'>ILink</a>
# that's conclude External and Internal links
#
# In addition,the first scanning will add any links of any rewrite links
# Because in the biggest system it could be a pattern like:
# http://victim.com/user/update/21
# Or even in Folders such as:
# http://victim.com/content/pageNotExsit
# for PCRE information see:
# http://docs.python.org/2/library/re.html
######################################
MissingProtocolForQueryString = '(?<![http|https])\?.*'
MissingProtocolForExternalLinks = '^[a-zA-z0-9_-]+\.[a-zA-z]{1,3}'