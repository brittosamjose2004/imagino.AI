from modules.expansion import fooocusExpansion

expansion = fooocusExpansion()

text = 'a handsome man'

for i in range(64):
    print(expansion(text, seed=i))
