from sys import argv

script, fname = argv

print 'we are going to erase %r' %fname
print """to abort mission, hit CTRL-C
or else hit RETURN"""


raw_input('??')


print 'Opening file'
targ  = open(fname,'w')

print 'truncating file? (huh? how did we get here?) truncating anyways'
targ.truncate()

print 'tell me the 3 lines that you want'

line1 = raw_input('Line 1: ')
line2 = raw_input('Line 2: ')
line3 = raw_input('Line 3: ')

print 'ok ima write these into the file'

targ.write(line1)
targ.write('\n')

targ.write(line2)
targ.write('\n')

targ.write(line3)
targ.write('\n')

print 'ok written, closing file'

targ.close()


