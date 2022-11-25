"""
File: boggle.py
Name: Mandy
----------------------------------------

"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

count = 0  # how many words found in dictionary
dic_list = []
word_list = []  # constructed by the words found in dictionary


def main():
    start = time.time()
    ####################
    ###Input####
    global count, dic_list
    read_dictionary()
    List = []  # save all letters as a list  [[, , , ,],[, , , ,]]
    for i in range(4):  # each row
        letters = input(str(i + 1) + " row of letters: ")
        if len(letters) != 7:
            print("Illegal input")
            break
        # letters: a,"",f,"",t,"",r
        list = []
        for j in range(4):  # index:0,2,4,6 (each element in sub_list)
            list += letters[(2 * j)].lower()
        List.append(list)
        if len(letters) != 7:
            print("Illegal input")
            break
    ###define the "search_word" and find ans_list###
    for m in range(4):
        for n in range(4):
            word = List[m][n]  # ex. word="f", f is List[m][n]
            neighbor_list = [(m, n)]  # neighbor_list stores the positions of all neighboring points
            find_word(m, n, word, neighbor_list, List)  # find neighbor_list
            neighbor_list.clear()

    ###print###
    print("There are: " + str(count) + " words in total.")

    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
    """
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
    global dic_list
    with open(FILE, "r") as f:
        for line in f:
            word = line.split()
            dic_list += word


def find_word(m, n, word, neighbor_list, List):  # recursion (m,n) as original word
    global word_list, count, dic_list
    # base case:
    if word in dic_list and len(word) > 3 and word not in word_list:
        print("Found \"" + word + "\"")
        word_list.append(word)
        count += 1

    # recursion
    if has_prefix(word) is True:  # if "f" is in dictionary, f is List[m,n]
        # Find neighboring points of List(m,n)
        for i in range(-1, 2):  # i=-1~1, one step
            for j in range(-1, 2):  # i=-1~1, one step
                if 4 > m + i >= 0 and 4 > n + j >= 0 and (m + i, n + j) not in neighbor_list:  # find  m+i, n+j
                    # Choose
                    word += List[m + i][n + j]  # ex. word="fy"
                    neighbor_list.append((m + i, n + j))
                    # Explore
                    find_word(m + i, n + j, word, neighbor_list, List)
                    # Unchoose
                    neighbor_list.pop()
                    word = word[:-1]


def has_prefix(sub_s):
    """
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
    global dic_list

    for ele in dic_list:
        if ele.startswith(sub_s):
            return True

    return False


if __name__ == '__main__':
    main()
