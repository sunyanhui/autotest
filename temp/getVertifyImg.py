import urllib
for i in range(50):
    url = 'http://www.company.com/getvalidatecode.shtml'
    print "download", i
    open("./img/%04d.gif" % i, "wb").write(urllib.urlopen(url).read())


import urllib
for i in range(50):
    url = 'http://www.XXX.com/XXX.shtml'
    open("./img/%04d.gif" % i, "wb").write(urllib.urlopen(url).read())