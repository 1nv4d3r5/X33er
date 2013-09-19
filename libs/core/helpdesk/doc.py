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

def docHelp():
    print """
###################################################################
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
###################################################################
"""
    print "Supported Audits:\n\n"
    print "[ - ] JavaScript - Will Allow you to pentest / audit any malicious\n\t\t\tjavascript that you can inject into JS file\n"
    print "[ - ] Basic - Will Allow you to pentest / audit any input in the GET\n\t\tthat could be use as input from the user"

    print "\nIn order to use each one, the usage is:\n\n\tpython xsser.py --url=\"http://victim.com\" --type=\"basic\"\n\nNOTE: The basic audit set as default if you don't choose"