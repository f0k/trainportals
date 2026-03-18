#!/usr/bin/env python3

# Standalone script that does not interface with Gnome NetworkManager

import re
import requests
import sys

verbose = any(arg in sys.argv[1:] for arg in ('-v', '--verbose'))

sess = requests.Session()
portal_html = sess.get("http://detectportal.firefox.com").text
if portal_html.startswith("success"):
    if verbose:
        print("Already online.")
    sys.exit(0)


postdata = dict(re.findall(r'<input name="([^"]+)" type="hidden" value="([^"]+)">', portal_html))
action_url = next(re.finditer(r'<form method="POST" action="([^"]+)"', portal_html))[1]
if verbose:
    print("Logging in as",
          ", ".join(k + "=" + v for k, v in postdata.items()))
response = sess.post(action_url, data=postdata)
if verbose:
    print(response.reason)
sys.exit(0 if response.status_code == 200 else 1)
