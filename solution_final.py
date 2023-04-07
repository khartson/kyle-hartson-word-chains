# solution_final.py

# Kyle Hartson

# This code is a recreation of a solution I came to after consulting 
# external resources. All comments are my own. 



# Queue for BFS
from queue import Queue

# File i/o to create word list 
f = open('dictionary.txt', 'r')
words = set(line.strip() for line in f)

# Word Chain 
def word_chains(start, end):
    # if the start or end word is not in the dictionary,
    # we cannot form a chain between them
    if start not in words or end not in words:
        return None
    
    # form a dictionary of each word in the BFS's parent (ie: words formed)
    # from our current iteration
    parents = { start: None }

    # Queue for BFS. If a child of a word exists in the dictionary and is`` not 
    # the end word AND has not been explored, we will add it to the queue to 
    # be explored
    queue = Queue()
    queue.put(start)

    # Perform BFS while all graph nodes have not been visited
    while not queue.empty():
        # Grab the current word in the queue
        word = queue.get()

        # For each letter of the current word, iterate A-Z over its indices and
        # check if the newly formed word exists in the word dictionary. 
        for i in range(len(word)):
            # We are forming 25 new words per index of the current word
            for j in range(26):
                new_word = word[:i] + chr(ord('a') + j) + word[i+1:]

                # for each word, check if it is in the dictionary, and not in 
                # parents (in which case it has been iterated over)
                if new_word in words and new_word not in parents:
                    # if so, add the original word as a 'parent' of the new word
                    parents[new_word] = word
                    # if the new word is the ending word
                    if new_word == end:
                        # start the word chain at the end word 
                        chain = [end]
                        # grab its parent, which has been kept in the dictionary
                        parent = parents[end]
                        # backtrace the parent of each consecutive word until 
                        # we reach the first word of the 'parent' dictyionary,
                        # which will be the starting word 
                        while parent is not None:
                            chain.append(parent)
                            parent = parents[parent]
                        chain.reverse()
                        return chain
                    # in the event that the word is in the dictionary, unexpl-
                    # ored, but not the end word, add the new word to the queue
                    # to continue BFS for
                    queue.put(new_word)
    
    return None

def prompt_user():
    # prompt user to enter start and ending words for
    # the chain  
    start = input('Enter starting word or 0 to exit: ')
    if start == '0':
        exit()
    end   = input('Enter ending word: ')
    if (len(start) != len(end)):
        print('Start and end word must be of same length')
        exit()
    else:
        chain = word_chains(start.lower(), end.lower())
        if chain != None:
            print(' => '.join(chain))
        else: 
            print('No chain found')

if __name__ == '__main__':
    while True:
        prompt_user()