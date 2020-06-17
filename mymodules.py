import math
import numpy as np

def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums.sort()
    output = []
    small = 0
    high = 0
    for i in range(len(nums)):
        if nums[small] + nums[len(nums)-high-1] < target:
            small += 1
        if nums[small] + nums[len(nums)-high-1] > target:
            high += 1
        if nums[small] + nums[len(nums)-high-1] == target:
            output.append(small)
            output.append(high-1)
            return output

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
        
        x = len(search)
        
        for i in range(len(list_words)):
            list_words[i][1] = levenshtein(search, list_words[i][0][:x])
        
        list_words = Sort(list_words)
        #for e in range(len(list_words)):
            #print(list_words[e][0] + " has " + str(list_words[e][1]) + " differences!")
    
    find_closest_answers(my_list, search)

    return my_list
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
    print (matrix)
    return (matrix[size_x - 1, size_y - 1])




def readDocument(name):
    with open(r"C:\Users\owen\Desktop\Projet Python\website\{}.txt".format(name)) as f:
        content = f.readlines()

    content = [x.strip() for x in content] 
    return content













def is_square(n):   
    output = False
    
    if n >= 0:
        if (math.sqrt(n)).is_integer():
            output = True     
            
    else:    
        output == False
        
    return output 


def get_sum(a,b):
    output = a+b
    
    if a == b:
        return a
        
    else:       
        for i in range(a, b):
            output += i
        
    return output


def stray(arr):
    output = 0
    value_list = 0
    Found = False
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            value_list = arr[i]
            Found = True
            break
            
    if Found == False:
        value_list = arr[0]
        
    for e in range(len(arr)):
        if arr[e] == value_list:
            pass
        else:
            output = arr[e]
            break
    
    return output
      

def solution(number):  
    output = 0
    
    for i in range(number):
        if i % 3 == 0:
            print(i)
            output += i
            
        elif i % 5 == 0:
            print(i)
            output += i
            
    return output 


def arithmetic(a, b, operator):
    output = 0
    
    if operator == "add":
        output = a+b
        return output
    if operator == "subtract":
        output = a-b
        return output
    if operator == "multiply":
        output = a*b
        return output
    if operator == "divide":
        output = a/b
        return output
     
        
def is_valid_IP(string):
    output = False
    n_1, n_2, n_3, n_4 = False,False,False,False
    try:
        n1, n2, n3, n4 = string.split(".")
    except Exception:
        return False
    
    
    if len(n1) > 1:  
        if n1[0] == "0":
            return False
    if len(n2) > 1:  
        if n2[0] == "0":
            return False
    if len(n3) > 1:  
        if n3[0] == "0":
            return False
    if len(n4) > 1:  
        if n4[0] == "0":
            return False   
    
    
    
    if len(n1) > 1:  
        if n1[1] == " ":
            return False
        if len(n1) > 2:
            if n1[2] == " ":
                return False
                
    if len(n2) > 1:  
        if n2[1] == " ":
            return False
        if len(n2) > 2:
            if n2[2] == " ":
                return False
    if len(n3) > 1:  
        if n3[1] == " ":
            return False
        if len(n3) > 2:
            if n3[2] == " ":
                return False
    if len(n4) > 1:  
        if n4[1] == " ":
            return False
        if len(n4) > 2:
            if n4[2] == " ":
                return False
      
    
    
    
    try:
        if int(n1) >= 0 and int(n1) <= 255:
            n_1 = True
        if int(n2) >= 0 and int(n2) <= 255:
            n_2 = True
        if int(n3) >= 0 and int(n3) <= 255:
            n_3 = True
        if int(n4) >= 0 and int(n4) <= 255:
            n_4 = True
        
        if n_1 == True and n_2 == True and n_3 == True and n_4 == True:
            output = True
        
        else:
            output = False

    except Exception:
        output = False
        
    return output

def divisors(integer):
    output = []
    
    for i in range(2, integer-1):
        if integer % i == 0:
            output.append(i)
    
    
    if len(output) == 0:
        return "{} is prime".format(integer)
    return output

def number(bus_stops):
    output = 0
    
    for i in range(len(bus_stops)):
        output += bus_stops[i][0] 
        output -= bus_stops[i][1]
        
    return output
       
def min_max(lst):
  output = []
  max = lst[0]
  min = lst[0]
  for i in range(len(lst)):
      if lst[i] > max:
          max = lst[i]
      elif lst[i] < min:
          min = lst[i]
          
  output.append(min)
  output.append(max)
  
  return output


def series_sum(n):
    sum = 0
    if n == 1:
        return "1.00"
    if n == 0:
        return "0.00"
    for i in range(n):
        sum += 1/(i*3+1)
        
    
    
    print(sum)
    
    return str(sum)[:4]


def camel_case(string):
    output = ""
    
    if len(string) == 0:
        return ""

    words = string.split(" ")

    for i in range(len(words)):
        words[i] = words[i].capitalize()
        print(words[i])
        
    for i in range(len(words)):
        output += words[i]
    
    print(output)
    
    return output



def sum_digits(number):
    output = 0
    number = str(number)
    number = number.replace('-', '')
    print(str(number))
    for i in range(len(number)):
        output += int(number[i])
    
    return output


def two_large_nums(ages):
    output = []
    ages.sort()
    print(ages)
    output.append(ages[len(ages)-2])
    output.append(ages[len(ages)-1])
    return output


def is_prime(num):
    
    output = True
      
    if num < 0:
          return False
    if num == 0 or num == 1:
          return False
      
    for i in range(num):
        if i != num and i != 1 and i != 0:
            if num % i == 0:
                return False
        pass
    return output


def sort_by_length(arr):
    return sorted(arr, key=len)
        
