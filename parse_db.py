import pandas as pd

names = {'AHC':'AHC',
        'APL':'Animal Planet',
        'DAM':'Desination America',
        'DSC':'Discovery',
        'DFC':'Discovery Family Channel',
        'DLF':'Discovery Life',
        'IDS':'Investigation Discovery',
        'SCI':'Science',
        'TlC':'TLC',
        'VEL':'Velocity'}

print('========' + '\n'
      'Networks' + '\n'
      '========' + '\n')
      
for k, v in names.items():
    print(k)

network = input('\n'+ 'Choose a network to export' + '\n' +
                'or type "All" for complete export')

data = pd.read_csv('shows.csv', usecols=[4,6])
if network == 'ALL':
    network_df = data
else:
    network_df = data.loc[data['network_code'] == network]
filename = 'network_db_extract.csv'
network_df.to_csv(filename, index=False, encoding='utf-8')
