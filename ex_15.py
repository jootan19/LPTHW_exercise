from sys import argv

script, fname = argv

text = open(fname)
print 'Here\'s your file %r:' % fname
print text.read()

print 'type filename again?'
file_again = raw_input('>')
text_again = open(file_again)

print text_again.read()

