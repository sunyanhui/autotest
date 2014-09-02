import urllib2
import json
from urlparse import urljoin


def getvertifycode(towho):

    getidurl = 'https://api.mailinator.com/api/inbox?to='+towho+'&token=a65b978467f54e559c028dff740c9621'
    s1 = json.loads(str(urllib2.urlopen(getidurl).read()))
    getmailurl = 'https://api.mailinator.com/api/email?msgid='+s1['messages'][0]['id']+'&token=a65b978467f54e559c028dff740c9621'
    mailfp = urllib2.urlopen(getmailurl)
    print mailfp.info()
    s2 = json.loads(str(mailfp.read()))
    print s2
    if 'error' in s2.keys():
    	return None
    else:
    	return s2[0]['body']




print getvertifycode('hgbac123')