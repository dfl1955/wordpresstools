#!/usr/bin/python

import sys, os, time

print str(sys.argv[1])
file=str(sys.argv[1])

#file="/kunden/homepages/19/d106342642/htdocs/bin/test.txt"
secsday=86400

st=os.stat(file)
age=(time.time() - st.st_ctime)
diff=int(age/secsday)

#if diff = 1 DAYS = day
DAYS="days"
print "The file is %s %s old" % (diff, DAYS)
# therfore age/sescsday should give the age since the file was last modified.




