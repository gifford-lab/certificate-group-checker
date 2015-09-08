# certificate_group_checker

An example `.htaccess` file and a simple Python CGI script that uses
SSL client certificates with a specified group membership to return
files in a local directory.

If you put these files in a directory served by Apache (and Apache is
configured with the correct CSAIL server certificate and allows
`.htaccess` overrides), you can use `get.py` as a secure way to get
files in that directory.

### Example:

Files in `/afs/csail/group/cgs/www/data/` are served at
[https://groups.csail.mit.edu/cgs/](https://groups.csail.mit.edu/cgs/)
by TIG (update: and now also at
[http://cgs.csail.mit.edu](http://cgs.csail.mit.edu) as our main group
site).

Access to files in the `slides` subdirectory is done by using
`get.py`, for instance:

[https://groups.csail.mit.edu/cgs/slides/get.py?file=matted_computing_3_2015.pdf](https://groups.csail.mit.edu/cgs/slides/get.py?file=matted_computing_3_2015.pdf)

Remember to lock down AFS so that other users can't see the files.
You need to have permissions for a group to write there (`cgs` for us)
and for the web server to read the directory (`www` in CSAIL).  As a
reference:

    groups2014:/afs/csail/group/cgs/www/data/slides$ fs la
     Access list for . is
     Normal rights:
       cgs rlidwk
       cgs-admin rlidwka
       www rl

