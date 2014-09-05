import urllib
for i in range(50):
    url = 'http://www.company.com/getvalidatecode.shtml'
    print "download", i
    open("./img/%04d.gif" % i, "wb").write(urllib.urlopen(url).read())