#!/usr/bin/env python3

import requests

def main():
    """Run time"""
    r = requests.get("http://ip-api.com/json/24.48.0.1")
    r2 = requests.get("http://ip-api.com/json/72.55.2.1")

    print("ip address:")
    print(r.json().get("query"))
    print("location:")
    print(r.json().get("country"))
    print(r.json().get("regionName"))
    print(r.json().get("city"))

    print("\n")

    print("ip address:")
    print(r2.json().get("query"))
    print("location:")
    print(r2.json().get("country"))
    print(r2.json().get("regionName"))
    print(r2.json().get("city"))
    

main()
