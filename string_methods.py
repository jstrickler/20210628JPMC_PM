actor = "Chris Hemsworth"

print(len(actor))

print(actor.upper(), actor.lower(), actor)

print(actor.count('h'))
print(actor.count('ris'))
print(actor.lower().count('h'))

role = " was Thor"

x = actor + role
print(x)

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))

print(actor.replace('Chris', 'Liam'))

print(actor.find('Chris'))
print(actor.find('worth'))
print(actor.find('Liam'))
# print(actor.index('Liam'))  raises error
print()

s = "    \r \r    All my exes live in Texas   \t  \n \n      "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "xxxxxxyxxxxxyxxxxxxyxxxxxxAll my exes live in Texasyyxyyyyyxyyyyyyyyyxxxxxx"
print("|" + s.lstrip('xy') + "|")
print("|" + s.rstrip('xy') + "|")
print("|" + s.strip('xy') + "|")
print()

info = "   hip hip hooray   "
words = info.split()
print(words)

record = "foo;bar;blah;baz"
fields = record.split(';')
print(fields)
new_record = '\t'.join(fields)
print(new_record)
new_record = ','.join(fields)
print(new_record)
print('<=>'.join(fields))






