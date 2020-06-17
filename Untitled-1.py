import numpy as np
def find_closest_words(my_list, search):
    def levenshtein(seq1, seq2):
        size_x = len(seq1) + 1
        size_y = len(seq2) + 1
        matrix = np.zeros ((size_x, size_y))
        for x in range(size_x):
            matrix [x, 0] = x
        for y in range(size_y):
            matrix [0, y] = y

        for x in range(1, size_x):
            for y in range(1, size_y):
                if seq1[x-1] == seq2[y-1]:
                    matrix [x,y] = min(
                        matrix[x-1, y] + 1,
                        matrix[x-1, y-1],
                        matrix[x, y-1] + 1
                    )
                else:
                    matrix [x,y] = min(
                        matrix[x-1,y] + 1,
                        matrix[x-1,y-1] + 1,
                        matrix[x,y-1] + 1
                    )

        return (matrix[size_x - 1, size_y - 1])


    def Sort(sub_li): 
        l = len(sub_li) 
        for i in range(0, l): 
            for j in range(0, l-i-1): 
                if (sub_li[j][1] > sub_li[j + 1][1]): 
                    tempo = sub_li[j] 
                    sub_li[j]= sub_li[j + 1] 
                    sub_li[j + 1]= tempo 
        return sub_li 


    def find_closest_answers(list_words, search):
        
        x = len(list_words)
        
        for i in range(len(list_words)):
            list_words[i][1] = levenshtein(search, list_words[i][0][:5])
        
        list_words = Sort(list_words)
        #for e in range(len(list_words)):
            #print(list_words[e][0] + " has " + str(list_words[e][1]) + " differences!")
    
    find_closest_answers(my_list, search)

    return my_list



my_list = [["train", 0], ["keyboard", 0], ["television", 0], ["controller", 0], ["amazon", 0], ["smartphone", 0], ["screen", 0], ["ps4", 0], ["xbox", 0], ["rocket League", 0], ["python", 0], ["montage", 0], ["javascript", 0], ["bluestacks", 0], ["nokia", 0]]


import random
import string

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


for i in range(500):
    temp_list = []
    temp_list.append(randomString())
    temp_list.append(0)    
    my_list.append(temp_list)


find_closest_words(my_list, input("What word: "))
