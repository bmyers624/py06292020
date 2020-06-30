#!/usr/bin/env python3

import requests

def main():
    """Run time code"""
    # r is request object
    r = requests.get("http://api.open-notify.org/iss-now.json")

    # print value from text
    print(r.json())
main()
