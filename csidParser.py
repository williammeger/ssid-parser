import csv
import datetime

site_section = "SS|"
site_group = "SG|"
delimiters = { '/':'|', '-':' '}
col_names = ['Parent Item', 'Item Type', 'Item Name', 'Item Tag']

def to_site_group(text):
    #looks for greatest common substring beginning from the last index
    text = "|".join(text.split("|")[:-1])
    return text

def time_stamp(fname, fmt='%Y-%m-%d_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

'''
  takes the input file as source list 
  and copies into nested list for export to csv 
  data needed for Freewheel bulk ingest
  [site, SG|..., SS|..., csid]
  maps to exported csv under
  Site, SiteSection, SiteGroup, csid
'''

def swap_domain(domain_name):
    for key, value in networks.items():
        if domain_name in networks:
            domain_name = domain_name.replace(key, value)
    return domain_name

def csid_parse(source):
    # create target for source list
    target = []
    sub_target_domain = []
    sub_target_site_group = []
    for csid in source:
        csid_origin = csid
        # get csid value based on each item in list
        # remove domain name
        domain = csid.rsplit('/')[0]
        # generate network acronym based on domain in csid
        network_acronym = swap_domain(domain)
        domain_origin = domain
        csid = csid.replace(domain_origin, '')
        for key in delimiters:
            csid = csid.replace(key, delimiters[key]).lower()
        ss = site_section + network_acronym + csid.title()
        csid_as_string = str(csid)
        sg = site_group + network_acronym + to_site_group(csid_as_string).title()
        target.extend((domain_origin, sg, ss, csid_origin))
    # breaks up target list into smaller lists for each csid
    # includes domain, SS, and csid
    sub_target_domain = [target[i:i + 4] for i in range(0, len(target), 4)]
    sub_target_domain.insert(0, col_names)
    return sub_target_domain

# start 
with open('networks.csv') as f:
    networks = dict(filter(None, csv.reader(f)))

# read in file contents to a source list
with open('dsc-redesign-csids.txt') as f:
    csid_list = f.readlines()

#remove whitespace characters like `\n` at end of line
csid_list = [x.strip() for x in csid_list]

fw_data = csid_parse(csid_list)

# build and write to target csv
with open(time_stamp('ssid-upload.csv'), 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(fw_data)

