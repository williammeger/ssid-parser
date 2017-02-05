#Windows File
import csv
import datetime

csid = "oprah.com/"
domain = csid.rsplit('/')[0]
siteSection = "SS|OWN"
siteGroup = "SG|OWN"
delimiters = {
  '/': '|',
  '-': ' '
}
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

def csidParse(source):
  # create target for source list
  target = []
  subTargetDomain = []
  subTargetSiteGroup = []
  for csid in source:
    csidOrigin = csid
    csid = csid.replace(domain, '')
    for key in delimiters:
      csid = csid.replace(key, delimiters[key]).lower()
    ss = siteSection + csid.title()
    csidAsString = str(csid)
    sg = siteGroup + toSiteGroup(csidAsString).title()
    target.extend((domain, sg, ss, csidOrigin))
  # breaks up target list into smaller lists for each csid
  # includes domain, SS, and csid
  subTargetDomain = [target[i:i + 4] for i in range(0, len(target), 4)]
  # includes SG, SS, and csid
  # subTargetSiteGroup = [target[i:i + 4] for i in range(0, len(target), 4) if i != 0]
  subTargetDomain.insert(0, colNames)
  return subTargetDomain


''' 
START
'''
# read in file contents to a source list
# windows requires a raw string to parse
with open(r"C:\Users\wmeger\Desktop\testUrls.txt") as f:
  csidList = f.readlines()
#remove whitespace characters like `\n` at EOL
csidList = [x.strip() for x in csidList]

fwData = csidParse(csidList)
print(fwData)

# build and write to target csv
with open(timeStamp('own-ssid-upload.csv'), 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(fwData)