#!/usr/bin/env python3
import requests
import re
import sys

LOGIN_URL = 'https://login.wifionice.de/en/?url='

verbose = any(arg in sys.argv[1:] for arg in ('-v', '--verbose'))

sess = requests.Session()
response = sess.head("http://detectportal.firefox.com")
if response.status_code == 200 and response.headers['Content-Length'] == "8":
    if verbose:
        print("Already online.")
    sys.exit(0)

# retrieve login URL from redirect location, use hardcoded URL as fallback
login_url = response.headers.get('Location', LOGIN_URL)
portal_html = sess.get(login_url).text
if '<title>CNA</title>' in portal_html:
    # new javascript-based portal
    login_url = 'https://login.wifionice.de/cna/logon'
    login_data = {}
else:
    # old HTML-based portal
    if 'csrf' in sess.cookies:
        csrf = sess.cookies['csrf']
    else:
        csrf = re.search('name="CSRFToken" value="([^"]+)"', portal_html).group(1)
    login_data = {
        "login": "true",
        "CSRFToken": csrf}

if verbose:
    print("Logging in as",
          ", ".join(k + "=" + v for k, v in login_data.items()))
response = sess.post(login_url, data=login_data)
if verbose:
    print(response.reason)
sys.exit(0 if response.status_code == 200 else 1)
