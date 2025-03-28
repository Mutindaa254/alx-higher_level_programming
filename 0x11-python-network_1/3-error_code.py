#!/usr/bin/python3

"""script that takes in a URL and displays the body of the response 
(decoded in utf-8)
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
