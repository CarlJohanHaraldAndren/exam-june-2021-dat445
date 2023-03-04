class Cooccurrences():
    def __init__(self):
        self.sentences=[]

    def addSentence(self, sentence):
        self.sentences+=[sentence]

    def get(self,word):
        cooccurences=[]
        for sentence in self.sentences:
            if word in sentence:
                for i in sentence:
                    if i != word and i not in cooccurences:
                        cooccurences.append(i)
        return cooccurences


occ = Cooccurrences()
occ.addSentence(["the", "boy", "saw", "the", "girl"])
occ.addSentence(["the", "girl", "loved", "flowers"])
print(occ.get("boy"))
# ["the", "saw", "girl"]
print(occ.get("girl"))
#["the", "boy", "saw", "loved", "flowers"]
print(occ.get("the"))
#["the", "boy", "saw", "girl", "loved", "flowers"]
occ.addSentence(["the", "cat", "likes", "the", "girl"])
print(occ.get("girl"))
#["the", "boy", "saw", "loved", "flowers", "cat", "likes"]


"""
Question 3
Implement the class Cooccurrences which must allow counting how
often a word appears together with another word in a sentence.
The class must have the following components:
1. An __init__ method which sets the initial state of the object.
2. A method:
def addSentence(sentence):
...
which adds another sentence to the state of the object. The
sentence itself is a list of words.
3. A method:
def get(word):
...
which given a word returns a list of other words that appear
together with that word. The list must contain each word only once.
The following is an example for how the class can be used:
>>> occ = Cooccurrences()
>>> occ.addSentence(["the", "boy", "saw", "the", "girl"])
>>> occ.addSentence(["the", "girl", "loved", "flowers"])
>>> print(occ.get("boy"))
["the", "saw", "girl"]
>>> print(occ.get("girl"))
["the", "boy", "saw", "loved", "flowers"]
>>> print(occ.get("the"))
["the", "boy", "saw", "girl", "loved", "flowers"]
>>> occ.addSentence(["the", "cat", "likes", "the", "girl"])
>>> print(occ.get("girl"))
["the", "boy", "saw", "loved", "flowers", "cat", "likes"]

"""