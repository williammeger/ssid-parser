import csv
import datetime

siteSection = "SS|"
siteGroup = "SG|"
delimiters = { '/':'|', '-':' '}
colNames = ['Parent Item', 'Item Type', 'Item Name', 'Item Tag']

def toSiteGroup(text):
  #looks for greatest common substring beginning from the last index
  text = "|".join(text.split("|")[:-1])
  return text

def timeStamp(fname, fmt='%Y-%m-%d_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

'''
  takes the input file as source list 
  and copies into nested list for export to csv 
  data needed for Freewheel bulk ingest
  [site, SG|..., SS|..., csid]
  maps to exported csv under
  Site, SiteSection, SiteGroup, csid
'''

def swapDomain(domainName):
  for key, value in networks.items():
    if domainName in networks:
      domainName = domainName.replace(key, value)
  return domainName

def csidParse(source):
  # create target for source list
  target = []
  subTargetDomain = []
  subTargetSiteGroup = []
  for csid in source:
    csidOrigin = csid
    # get csid value based on each item in list
    # remove domain name
    domain = csid.rsplit('/')[0]
    # generate network acronym based on domain in csid
    networkAbv = swapDomain(domain)
    domainOrigin = domain
    csid = csid.replace(domainOrigin, '')
    for key in delimiters:
      csid = csid.replace(key, delimiters[key]).lower()
    ss = siteSection + networkAbv + csid.title()
    csidAsString = str(csid)
    sg = siteGroup + networkAbv + toSiteGroup(csidAsString).title()
    target.extend((domainOrigin, sg, ss, csidOrigin))
  # breaks up target list into smaller lists for each csid
  # includes domain, SS, and csid
  subTargetDomain = [target[i:i + 4] for i in range(0, len(target), 4)]
  subTargetDomain.insert(0, colNames)
  return subTargetDomain

# start 

with open('networks.csv') as f:
  networks = dict(filter(None, csv.reader(f)))

# read in file contents to a source list
with open('testUrls.txt') as f:
  csidList = f.readlines()
#remove whitespace characters like `\n` at end of line
csidList = [x.strip() for x in csidList]

fwData = csidParse(csidList)
print(fwData)

# build and write to target csv
with open(timeStamp('ssid-upload.csv'), 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(fwData)