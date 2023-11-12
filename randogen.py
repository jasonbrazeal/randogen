#!/usr/bin/env python

import os
import json
import random

from pprint import pprint

import requests

class RandoGen(object):
    """Simple client to interact with random.org; can generate truly random numbers."""

    API_KEY = os.environ['API_KEY']

    def fetch_randos(self, num_randos, min_rando, max_rando, replace, base, return_bytes):
        if num_randos <= 0:
            if return_bytes:
                return bytearray([])
            else:
                return []
        data = {'jsonrpc':'2.0',
                'method': 'generateIntegers',
                'params': {'apiKey': self.API_KEY,
                           'n': num_randos,
                           'min': min_rando,
                           'max': max_rando,
                           'replacement': replace,
                           'base': base},
                'id': random.randrange(0, 10000)}

        if os.getenv('LOGLEVEL') == 'DEBUG':
            pprint(data)
        r = requests.post('https://api.random.org/json-rpc/4/invoke', headers={'content-type': 'application/json'}, data=json.dumps(data))
        if os.getenv('LOGLEVEL') == 'DEBUG':
            pprint(r.json())
        randos = r.json()['result']['random']['data']
        if return_bytes:
            return bytearray(randos)
        else:
            return randos

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='''
    Welcome to randogen.py help! This module will help you generate random numbers 
    from random.org. It can be run from the command line with:
        python3 randogen.py 
    It generates and prints random integers from random.org to stdout.
    There are several options, so be sure to check the help with:
        python3 randogen.py -h
    Note: your random.org API key should be set in an env var API_KEY
        ''', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--num',
                        default=10,
                        type=int,
                        help='number of random integers to generate')
    parser.add_argument('--min',
                        default=0,
                        type=int,
                        help='minimum random integer to generate')
    parser.add_argument('--max',
                        default=10000,
                        type=int,
                        help='maximum random integer to generate')
    parser.add_argument('--noreplacement',
                        action='store_false',
                        default=True,
                        help='set to prevent generator from producing the same number more than once')
    parser.add_argument('--base',
                        default=10,
                        type=int,
                        help='base of integers to generate')
    args = parser.parse_args()

    r = RandoGen()
    print(r.fetch_randos(args.num, args.min, args.max, args.noreplacement, args.base, return_bytes=False))
