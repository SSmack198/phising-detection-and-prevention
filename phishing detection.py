import re as regex

def url_having_ip(url):
  domain=url.split("//")[-1].split("/")[0].split("www.")[-1]
  domain = domain.strip()
  #print(domain)
  if regex.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', domain) != None:
    0
  else:
    1

def url_length(url):
  length=len(url)
  if(length<54):
    return 1 #legitimate
  elif(54<=length<=75):
    return -1 #suspicious
  else:
    return 0 #phishing

def url_short(url):
  domain=url.split("//")[-1].split("/")[0].split("www.")[-1]
  shortening_services = ['bit.do','goo.gl','ow.ly','bit.ly','tinyurl'
  ,'is.gd','branch.io','buff.ly','tiny.cc','soo.gd','s2r.co','clicky.me',
  'budurl.com']
  for shortening_service in shortening_services:
    if shortening_service in domain:
      return 0
    else:
      continue
  return 1

def having_at_symbol(url): #having '@' symbol
  symbol=regex.findall(r'@',url)
  if(len(symbol)==0):
    return 1
  else:
    return 0

def doubleSlash(url):
  if len(url.split("//"))>2:
    return 0
  else:
    return 1

def prefix_suffix(url):
  domain=url.split("//")[-1].split("/")[0].split("www.")[-1]
  if(domain.count('-')):
    return 0
  else:
    return 1

def sub_domain(url):
  domain=url.split("//")[-1].split("/")[0].split("www.")[-1]
  if(domain.count('.')<=1):
    return 1
  elif(domain.count('.')<=2):
    return -1 #suspicious
  else:
    return 0

print("To Quit press 'q' as input")
url = " "
while url != "q":
  url = input('Enter URL :\n') #inputting from user

  f1 = url_having_ip(url)
  f2 = url_length(url)
  f3 = url_short(url)
  f4 = having_at_symbol(url)
  f5 = doubleSlash(url)
  f6 = prefix_suffix(url)
  f7 = sub_domain(url)

  flag = [f1, f2, f3, f4, f5, f6, f7]

  phish = 0
  susp = 0
  for i in range(0, 6):
    if(flag[i]==0):
      continue
    elif(flag[i]==1):
      phish=phish+1
    else:
      susp=susp+1

  if(phish>0 or susp>0):
    print('\nThe link may not be secure. Please avoid this link "OR" upload ENCRYPTED DATA.')
  else:
    print('The link is tested secure. Go ahead!')

