import shlex

text = 'this text has "quoted parts" inside it.'

print("original: ", repr(text))
print()

print("TOKENS")
print(shlex.split(text))
