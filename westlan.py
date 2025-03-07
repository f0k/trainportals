#!/usr/bin/env python3
import requests
import urllib.parse
import re
import sys
import urllib.parse

verbose = any(arg in sys.argv[1:] for arg in ('-v', '--verbose'))

sess = requests.Session()
portal_html = sess.get("http://detectportal.firefox.com").text
if portal_html.startswith("success"):
    if verbose:
        print("Already online.")
    sys.exit(0)

# the URL is given in plain in an HTML comment
# if this ever stops working, the <form> contains the base URL and token.
login_url = re.search('authtarget: (.+)', portal_html).group(1)

if verbose:
    print("Logging in at", login_url)
response = sess.get(login_url)
if verbose:
    print(response.reason)
sys.exit(0 if response.status_code == 200 else 1)
