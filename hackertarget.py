'''

A small simple script to call the hackertarget.com API for basic IP tools.
The API can be found @ http://hackertarget.com/ip-tools/
You are limited to 100 queries a day so be aware and be kind.

'''
import argparse
import sys
import re
import urllib2

def main():
	parser = argparse.ArgumentParser()

	parser.add_argument('-d', '--dns', help='DNS Lookup')
	parser.add_argument('-g', '--geo', help='GeoIP Lookup')
	parser.add_argument('--http', help='HTTP Headers')
	parser.add_argument('-l', '--links', help='Page Links')
	parser.add_argument('-p', '--ping', help='Ping host')
	parser.add_argument('-x', '--proxy', help='Proxy input IP only (defaults to http only)')
	parser.add_argument('-r', '--reverse', help='Reverse DNS')
	parser.add_argument('-t', '--traceroute', help='Traceroute')
	parser.add_argument('-w', '--whois', help='Whois')
	parser.add_argument("-o", "--output", help="Create output file")

	# If no arguments, then pass help screen
	if len(sys.argv) <= 1:
		parser.print_usage()
		sys.exit(1)
	else:
		args = parser.parse_args()

	def checkIP(ip):
		valid_IP = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip)
		if valid_IP:
			pass
		else:
			print "%s does not appear to be a valid IP. You may have incorrect/incomplete results." % ip

	def checkHostname(hostname):
		valid_hostname = re.match("^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$", hostname)
		if valid_hostname:
			pass
		else:
			print "%s does not appear to be valid hostname.  You may have incorrect/incomplete results." % hostname

	# If we have a proxy, build a proxy 
	if args.proxy:
		proxy = urllib2.ProxyHandler({'http' : args.proxy})
		opener = urllib2.build_opener(proxy)
		urllib2.install_opener(opener)
		urlopen = urllib2.urlopen
	else:
		urlopen = urllib2.urlopen

	# Parse out query
	try:
		output = [] #Empty list to hold output values

		if args.dns:
			checkHostname(args.dns)
			query = HackerOneQuery(urlopen, args.dns)
			output.append(query.dnsLookup())

		if args.geo:
			checkIP(args.geo)
			query = HackerOneQuery(urlopen, args.geo)
			output.append(query.geoLookup())

		if args.http:
			checkHostname(args.http)
			query = HackerOneQuery(urlopen, args.http)
			output.append(query.httpHeaders())

		if args.links:
			checkHostname(args.links)
			query = HackerOneQuery(urlopen, args.links)
			output.append(query.pageLinks())

		if args.ping:
			checkIP(args.ping)
			query = HackerOneQuery(urlopen, args.ping)
			output.append(query.ping())

		if args.reverse:
			checkIP(args.reverse)
			query = HackerOneQuery(urlopen, args.reverse)
			output.append(query.reverseDNS())

		if args.traceroute:
			checkIP(args.traceroute)
			query = HackerOneQuery(urlopen, args.traceroute)
			output.append(query.traceroute())

		if args.whois:
			query = HackerOneQuery(urlopen, args.whois)
			output.append(query.whois())

	except:
		pass

	output = "\n".join(output) # Parse out the newlines from the list to a readable output

	try:
		# If output selected, then save file
		if args.output:
			with open(args.output, 'w') as file:
				file.write(output)
			file = open(args.output, 'r')
			print file.read(), file.close()
			print "File saved to", args.output
		else:
			print output
	except IOError:
		pass

class HackerOneQuery(object):
	def __init__(self, url, userinput):
		self.open = url
		self.api = 'http://api.hackertarget.com'
		self.userinput = userinput

	def dnsLookup(self):
		self.dnslookup  = self.open(self.api + '/dnslookup/?q=' + self.userinput).read()
		return self.dnslookup

	def geoUser(self):
		self.geouserinput = self.open(self.api + '/geouserinput/?q=' + self.userinput).read()
		return self.geouserinput

	def httpHeaders(self):   
		self.httpheaders = self.open(self.api + '/httpheaders/?q=' + self.userinput).read()
		return self.httpheaders

	def pageLinks(self):
		self.pagelinks = self.open(self.api + '/pagelinks/?q=' + self.userinput).read()
		return self.pagelinks

	def ping(self):
		self.ping = self.open(self.api + '/nping/?q=' + self.userinput).read()
		return self.ping

	def reverseDNS(self):
		self.reversedns = self.open(self.api + '/reversedns/?q=' + self.userinput).read()
		return self.reversedns

	def traceroute(self):
		self.traceroute = self.open(self.api + '/mtr/?q=' + self.userinput).read()
		return self.traceroute

	def whois(self):
		self.whois = self.open(self.api + '/whois/?q=' + self.userinput).read()
		return self.whois

if __name__ == "__main__":
	main()