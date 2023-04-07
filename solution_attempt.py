# solution.py
# Kyle Hartson
# This is my own first attempt at solving the Word Chains problem witbout
# the use of any external resources


# open word dictionary
f = open('dictionary.txt', 'r')

# create a set containing all words in the dictionary
dic = set(line.strip() for line in f)

# similar_word
# given a word and a word list, find the words in the wordlist that
# differ by the current word from only one letter. this is done by 
# iterating over each letter of the word and matching the words in 
# the word list that match this criteria. This function will build 
# a list of words for each word in the dictionary that are 
# 'similar to the given word, and we can iterate through these to form a
# path through our dictionary to the target word

def similar_word(word, wordlist):
    # for letter in word
    # split on the current letter
    
        # for word in word list
        # if word split and joined on current index == word also split 
        # at that index, add it to the adjacency list
        similar_words = []
        for index in range(len(word)):
            for entry in wordlist:
                if (len(word) != len(entry)):
                     continue
                elif ''.join(word.split(word[index])) == ''.join(entry.split(entry[index])) and entry != word:
                     similar_words.append(entry)
        # word_graph[word] = similar_words
        return similar_words


# build_graph
# starting from the target word, build an adjacency list for each 
# child/neighbor of this word this will create the full graph of 
# possible transformation paths that can be performed from the starting
# word, based on dictionary entries. From here, you can run BFS on the graph, 
# return the route taken to get to the target/end word
def build_graph(word):
    word_graph = {}
    visited    = {}
    word_graph[word] = similar_word(word, dic)
    # for word in wordList:
        # word_graph[word] = similar_word(word, wordList)
    print(word_graph)

     
     

if __name__ == '__main__':
    build_graph('cat')