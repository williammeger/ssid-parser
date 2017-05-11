prefix = 'dsc.discovery.com/tv-shows'

with open('source.txt', 'r') as src:
    with open('output.txt', 'w') as dest:
       for line in src:
           dest.write('{0}{1}\n'.format(prefix, line.rstrip('\n')))
           
