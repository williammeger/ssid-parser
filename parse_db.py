import os
import pandas as pd

names = {'AHC':'AHC',
        'APL':'Animal Planet',
        'DAM':'Desination America',
        'DSC':'Discovery',
        'DFC':'Discovery Family Channel',
        'DLF':'Discovery Life',
        'IDS':'Investigation Discovery',
        'SCI':'Science',
        'TLC':'TLC',
        'VEL':'Velocity'}

print('========' + '\n'
      'Networks' + '\n'
      '========' + '\n')
      
for k, v in names.items():
    print(k + '- ' + v)

network = input('\n'+ 'Choose a network to export' + '\n' +
                'or type "ALL" for complete export' + '\n').upper()

# TODO
# add functionality for user to choose source
# file to begin extraction
file_to_parse = input('\n' + 'Choose a file to parse' + '\n')

cwd = os.getcwd()
# using source file to create sub dir name
sub_dir = file_to_parse.split('.')[0]
sub_dir = os.path.join(cwd, sub_dir)
# make sub directory in cwd
if not os.path.exists(sub_dir):
    os.mkdir(sub_dir)

# os.path.join(sub_dir, filename)
all_df = pd.read_csv(file_to_parse, usecols=[4,6])

# assume we want to export everything
network_df = all_df

if network in names:
    # export csv with network and csids
    network_df = all_df.loc[all_df['network_code'] == network]

# filter all data by network code
# write each network to csv
# save each csv to subdirectory
for key in names:
    filename = key + '.csv'
    network_df = all_df.loc[all_df['network_code'] == key]
    #network_df.to_csv(filename, index=False, encoding='utf-8')
    network_df.to_csv(os.path.join(sub_dir, filename), index=False) 

# filename = '.csv'
# network_df.to_csv(filename, index=False, encoding='utf-8')

