#!/usr/bin/python
from ghost import Ghost
import argparse
# ghost is a webclient
ghost = Ghost()
ghost.open('http://duckduckgo.com/') 
ghost.wait_for_selector('input[name=q]')
ghost.fill("#search_form_homepage", {'q': 'beer'})
ghost.fire_on("#search_form_homepage",
              "submit",
              expect_loading=True) 
ghost.wait_for_selector('#r1-0')
result, _resources = ghost.evaluate(
    "document.getElementById('r1-0').innerHTML;")
print result