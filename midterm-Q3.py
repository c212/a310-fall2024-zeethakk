letter = "a"
words = [ "bc", "cb" ]

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)

def ben(letter, words):
    result = []
    for word in words:
        line = []
        for index in range(len(word)+1):
            line += [ word[0:index] + letter + word[index:] ]
        result += line
    return result

a = ben(letter, words)
print( a ) # [ "abc", "bac", "bca", "acb", "cab", "cba" ]

def perm(word):
    if len(word) <= 1:
        return [ word ]
    else:
        return ben(word[0], perm(word[1:]))

print(perm("hat"))
print(perm("race"))
print(len(perm("whatever")) == 40320)

assert sorted(perm("hat")) == sorted(['hat', 'aht', 'ath', 'hta', 'tha', 'tah']), "First assert fails."
assert len(perm("race")) == fact(len("race")), "Second assert fails."
assert len(perm("whatever")) == 40320, "Third assert failed."
print ("All assertions passed without a problem")

# # Function to calculate factorial
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)

# # Function to insert a letter into all positions of a word list
# def ben(letter, words):
#     result = []
#     for word in words:
#         line = []
#         for index in range(len(word)+1):
#             line += [ word[0:index] + letter + word[index:] ]
#         result += line
#     return result

# # Function to calculate all permutations of a given word
# def perm(word):
#     if len(word) <= 1:
#         return [ word ]
#     else:
#         return ben(word[0], perm(word[1:]))

# # Testing the perm function with the given cases
# assert sorted(perm("hat")) == sorted(['hat', 'aht', 'ath', 'hta', 'tha', 'tah']), "First assert fails."
# assert len(perm("race")) == fact(len("race")), "Second assert fails."
# assert len(perm("whatever")) == 40320, "Third assert failed."

# print("All assertions passed without a problem")
