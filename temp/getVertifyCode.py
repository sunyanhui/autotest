import urllib2
import json
import re


def getvertifycode(towho):

    getidurl = 'https://api.mailinator.com/api/inbox?to='+towho+'&token=a65b978467f54e559c028dff740c9621'
    s = json.loads(str(urllib2.urlopen(getidurl).read()))
    mailurl = 'https://www.mailinator.com/rendermail.jsp?msgid='+s['messages'][0]['id']+'&time='+'1409663495288'
    mail = urllib2.urlopen(mailurl)
    print mail.read()
    return  re.compile(r'\d{6}').search(mail.read()).group() 




if __name__ == '__main__':
	mailid = raw_input('Please input mail id:')
	print getvertifycode(mailid)
	raw_input()
