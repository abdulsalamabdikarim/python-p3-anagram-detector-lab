# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, list):
        anagram_match = [element for element in list if sorted(element) == sorted(self.word)]
        return anagram_match
        # for element in list:
        #     if sorted(element) == sorted(self.word):
        #         anagram_match.append(element)
        #     else:
        #         return anagram_match
        # print(anagram_match)

y = Anagram("race")
g = y.match(['enlist', 'google', "silent", 'care','reca', "reac"])
print(g)

