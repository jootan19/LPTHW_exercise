from os.path import exists
from sys import argv

script, frm_file, to_file = argv

print 'copying %s to %s' % (frm_file, to_file)

in_file = open(frm_file)
indata = in_file.read()

# alternate
# indata = open(frm_file,'r').read()


print 'input is %i bytes long' % len(indata)

print 'does output file exist? %r' % exists(to_file)

print 'to abort mission do Ctrl+C otherwise hit RETURN'

raw_input('>>')

out_file = open(to_file, 'w')
out_file.write(indata)

# alternate:
# open(to_file,'w').write(indata)

print 'finally done...zomg'

# comment out below when using alternatives...
out_file.close()
in_file.close()

'''or just forget lines 6 - 33 and use below:'''
# from shutil import copyfile
# copyfile(frm_file, to_file)



