# randogen

A simple client for random.org that can generate true random numbers.

# usage

`python3 randogen.py [-h] [--num NUM] [--min MIN] [--max MAX] [--noreplacement] [--base BASE]`

    Welcome to randogen.py help! This module will help you generate random numbers
    from random.org. It can be run from the command line with:
        python3 randogen.py
    It generates and prints random integers from random.org to stdout.
    Note: your random.org API key should be set in the environment variable API_KEY

```
optional arguments:
  -h, --help       show this help message and exit
  --num NUM        number of random integers to generate
  --min MIN        minimum random integer to generate
  --max MAX        maximum random integer to generate
  --noreplacement  set to prevent generator from producing the same number more than once
  --base BASE      base of integers to generate
```
