import re

def word_Sort(wordString):
    word_string_updated = re.sub("[.!?]", "", wordString)
    word_list = word_string_updated.split(" ")

    wordDictionary = {}
    #Dict wordDictionary based on word length.
    for word in word_list:
        if len(word) in wordDictionary: 
            wordDictionary[len(word)] = wordDictionary[len(word)] + [word]
            print(wordDictionary)
        else:
            wordDictionary[len(word)] = [word]

    wordDictionaryOdd = {}
    #Dict a w/ modulo operator is checking if odd from wordDictionary dictionary.
    for word in wordDictionary:
        for wordString in wordDictionary[word]:
            if len(wordString) % 2 == 1:
                wordDictionaryOdd[word] = wordDictionary[word]
        else:
            continue

    return wordDictionaryOdd



word_Sort("This is a sentence. And yet another one!")
# Tests
#assert(word_Sort("This is a sentence. And yet another one!") == {1: ['a'], 3: ['And', 'yet', 'one'], 7: ['another']})
#assert(word_Sort("Miscollated alphabetic superimposition") == {11: ['Miscollated'], 15: ['superimposition']})
#assert(word_Sort("a a a a bb bb bb ccc ccc") == {1: ['a', 'a', 'a', 'a'], 3: ['ccc', 'ccc']})