#!/usr/bin/env python
import pycurl
import argparse
# pycurl is barebones python requests module
url = 'http://gawker.com/beached-great-white-shark-hitches-ride-to-safety-via-su-1717830090'
pycurl_connect = pycurl.Curl()
pycurl_connect.setopt(pycurl.URL, url)
# Set user agent in content renders 403 forbidden
# 403's are usually returned to prevent bots from scraping website
pycurl_connect.setopt(pycurl.HTTPHEADER, ['User-Agent: Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16',
                                          'header_name2: header_value2'])
content = pycurl_connect.perform()
print content