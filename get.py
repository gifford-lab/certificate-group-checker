#!/usr/bin/env python
import cgi
import cgitb
import os
import grp
import mimetypes
import sys

REQUIRED_GROUP = "cgs"

cgitb.enable()
mimetypes.init()

user = os.environ.get("SSL_CLIENT_S_DN_Email", "fakeuser@fakeemail").split("@")[0]
valid = False
error = True

try:
    valid = (user in grp.getgrnam(REQUIRED_GROUP).gr_mem)
except KeyError:
    pass

form = cgi.FieldStorage()

if valid and "file" in form:
    fname = form["file"].value
    if os.path.exists(fname) and os.access(fname, os.R_OK) and os.path.isfile(fname) and ".." not in fname and "/" not in fname:
        mimetype = mimetypes.guess_type(fname)[0]
	if mimetype is None:
            mimetype = "application/octet-stream"
        print "Content-type: %s\n\n" % mimetype
        sys.stdout.write(open(fname, "rb").read())
        error = False

if error:
    print """Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access that file on this server.</p>
<hr>
<address>Apache/2.2.22 (Ubuntu) Server at groups.csail.mit.edu Port 443</address>
</body></html>
"""
