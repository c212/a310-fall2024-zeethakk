# regex pig latin
# https://web.ics.purdue.edu/~morelanj/RAO/prepare2.html

'''
1. If a word starts with a consonant and a vowel, put the first letter of the word at the end of the word and add "ay".
2. If a word starts with two consonants (consonants block), move the two consonants to the end of the word and add 'ay.'
3. If a word starts with a vowel, add the word 'way' at the end of the word.

'''
import re

sentence = 'I love pig latin and regular expression! This will be fun! tywwwrrriooooer'

new_sentence = []

for word in sentence.split(' '):
    new = ''
    pattern1 = r'(^[^aeiouAEIOU])([aeiouAEIOU])(\w*)'
    pattern2 = r'(^[^aeiouAEIOU]{2,})(\w*)'
    pattern3 = r'(^[aeiouAEIOU])(\w*)'

    if re.match(pattern1, word):       
        new = re.sub(pattern1, r'\2\3\1'+'ay', word) # + 'ay'  //ay will be added after punctuation.
    elif re.match(pattern2, word):
        new = re.sub(pattern2, r'\2\1'+ 'ay', word)        
    else:
        new = re.sub(pattern3, r'\1\2'+ 'way', word)
    new_sentence.append(new)

print(new_sentence)
new_sentence = ' '.join(new_sentence)
print(sentence)
print(new_sentence)
    # match
    # substitube
    # append to list