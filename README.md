# hackertarget.py

Quickly query [hackertarget.com API](https://hackertarget.com/ip-tools/) from the command line with python.

*** Please note that you are limited to 100 API requests a day***

```sh
usage: hackertarget.py [-h] [-d DNS] [-g GEO] [--http HTTP] [-l LINKS]
                       [-p PING] [-x PROXY] [-r REVERSE] [-t TRACEROUTE]
                       [-w WHOIS] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -d DNS, --dns DNS     DNS Lookup
  -g GEO, --geo GEO     GeoIP Lookup
  --http HTTP           HTTP Headers
  -l LINKS, --links LINKS
                        Page Links
  -p PING, --ping PING  Ping host
  -x PROXY, --proxy PROXY
                        Proxy input IP only (defaults to http only)
  -r REVERSE, --reverse REVERSE
                        Reverse DNS
  -t TRACEROUTE, --traceroute TRACEROUTE
                        Traceroute
  -w WHOIS, --whois WHOIS
                        Whois
  -o OUTPUT, --output OUTPUT
                        Create output file
```
#Examples
### Ping
```sh
python hackertarget.py -p 8.8.8.8
```
### Whois
```sh
python hackertarget.py -w 8.8.8.8
```
### Output reverse DNS and GeoIP to text file
```sh
python hackertarget.py -r 8.8.8.8 -g 8.8.8.8 -o output.txt
```