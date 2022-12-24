# What does it do?

A simple, interactive python script to get a user ID and the account data API URL.

# Usage

```bash
usage: main.py [-h] [-s SERVER] [-u USER] [-t TOKEN]

Get the API request URL to fetch a fediverse accounts data by searching for an account.

options:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        The address of the server that's API you want to use (e.g. mastodon.social)
  -u USER, --user USER  The user that you are searching
  -t TOKEN, --token TOKEN
                        Authorization token (optional)

Each account has a unique ID on any server where it is known. So you can not simply replace https://chaos.social/api/v1/accounts/107277650350084474
with https://mastodon.social/api/v1/accounts/107277650350084474

```


# Example

``` bash
python main.py -s mastodon.social -u moanos
```
