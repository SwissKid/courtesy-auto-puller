#!/usr/bin/env python2
# Example URL http://www.courtesyparts.com/images/s13/s13_200-1.gif
import urllib2

baseurl="http://www.courtesyparts.com/images/s13/s13_"

regionfail = False
while regionfail == False:
    for region in range(200,300):
	subfail = False
	subimage = 1
	while subfail == False:
	    req = urllib2.Request(baseurl + str(region) + "-" + str(subimage) + ".gif")
	    try:
		resp = urllib2.urlopen(req)
	    except urllib2.URLError, e:
		    if e.code == 404:
			if subimage == 1:
			    regionfail = True
			subfail = True
		    else:
			print "DIFFERENT ERROR " + e.code
	    else:
		data = resp.read()
		f = open(str(region) + "-" + str(subimage) + ".gif", "a")
		f.write(data)
		f.close
		subimage += 1

	
