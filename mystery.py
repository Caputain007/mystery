import re

def word_Sort(wordString):
    word = wordString.split(" ")
    wordArray = []

    for wordString in word:
        #Strip special chars.
        wordStringUpdated = re.sub("[.!?]", "", wordString)
        wordArray.append(wordStringUpdated)

    wordDictionary = {}
    #Dict wordDictionary based on word len
    for index in wordArray:
        if len(index) in wordDictionary: 
            wordDictionary[len(index)] = wordDictionary[len(index)] + [index]
        else:
            wordDictionary[len(index)]=[index]

    wordDictionaryOdd = {}
    #Dict a w/ modulo operator is checking if odd from wordDictionary dictionary.
    for index in wordDictionary:
        for wordString in wordDictionary[index]:
            if len(wordString) % 2 == 1:
                wordDictionaryOdd[index] = wordDictionary[index]
        else:
            continue
        
    return wordDictionaryOdd




# Tests
assert(word_Sort("This is a sentence. And yet another one!") == {1: ['a'], 3: ['And', 'yet', 'one'], 7: ['another']})
assert(word_Sort("Miscollated alphabetic superimposition") == {11: ['Miscollated'], 15: ['superimposition']})
assert(word_Sort("a a a a bb bb bb ccc ccc") == {1: ['a', 'a', 'a', 'a'], 3: ['ccc', 'ccc']})