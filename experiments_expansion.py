from modules.expansion import imagino.AIExpansion

expansion = imagino.AIExpansion()

text = 'a handsome man'

for i in range(64):
    print(expansion(text, seed=i))
