import re

word = "12345"

def nuf(a, b):
    return int(a) + int(b)

def fun(match): # , eggplant):
    a = nuf(match.group(1), match.group(2))
    print(match)
    return str(a) # match.group(2) + match.group(1)

result = re.sub('(\d)(\d)', fun, word)

print(result)

text = ['this is nice', 'how nice', 'not nice', 'very bad']

mark = map(lambda num : num + 1, [8, 1, 2, 3, 2, 5])

print(list(mark))

def meh(one):
    return (True, one) if 'nice' in one else (False, one)

mark = map(meh, text)

print(list(mark))

word = "I am so happy right now."

result1 = re.sub('(\w)', r'(\1)', word)
result2 = re.sub('(\w)', '(\\1)', word)

print(result1)
print(result2)

# --