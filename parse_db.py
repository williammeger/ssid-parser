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

all_df = pd.read_csv('shows.csv', usecols=[4,6])

# assume we want to export everything
network_df = all_df

if network in names:
    # export csv with network and csids
    network_df = all_df.loc[all_df['network_code'] == network]

for key in names:
    filename = key + '.csv'
    network_df = all_df.loc[all_df['network_code'] == key]
    network_df.to_csv(filename, index=False, encoding='utf-8')

# filename = '.csv'
# network_df.to_csv(filename, index=False, encoding='utf-8')
