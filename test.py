#example of multi-line printing, where you can print wysiwyg style

print ('''

==========
|        |
| A Box  |
|        |
==========

''')

for i in range (2,5):
    print (i)

x = 'silent'
print (x[2] + x[1] + x[0] + x[5] + x[3] + x[4])
# this prints the word listen, not string starts at 0, so letter 1 is i etc..


