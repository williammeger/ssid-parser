prefix = 'dsc.discovery.com/tv-shows'

with open('source.txt', 'r') as src:
    with open('output.txt', 'w') as dest:
       for line in src:
#           dest.write('%s%s\n' % (prefix, line.rstrip('\n')))
           dest.write('{}{}\n'.format(prefix, line.rstrip('\n')))
           
