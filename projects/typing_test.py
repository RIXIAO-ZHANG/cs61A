""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5

# BEGIN Q1
def lines_from_file(path):
# a list of strings
    the_file = open(path, mode='r')
    if readable(the_file):
        the_list = readlines(the_file)
    a=[]
    for i in range(0,len(the_list)):
        a+=[strip(strip(the_list[i]),'\n')]
    return a
# END Q2




def new_sample(path,i):
    return lines_from_file(path)[i]
# END Q1
# BEGIN Q2
def analyze(sample_paragraph,typed_string,start_time,end_time):
    """
    This function should output a list containing two values:
    words per minute and accuracy percentage.
    """
    num_chars = len(typed_string) / 5
    duration = (end_time - start_time) / 60

    typed_list = split(typed_string)
    sample_list = split(sample_paragraph)

    num_words_of_sample = len(sample_list)
    num_words_of_typed = len(typed_list)

    def calculate_accuracy():
        i, num_correct_words, the_words_used  = 0, 0, 0

        if num_words_of_typed == 0:
            return 0.0
        elif num_words_of_typed >= num_words_of_sample:
            the_words_used = num_words_of_sample
        else:
            the_words_used = num_words_of_typed

        while i < the_words_used:
            if typed_list[i] == sample_list[i]:
                num_correct_words += 1
            i += 1
        return 100 * (num_correct_words / the_words_used)
    return [num_chars / duration, calculate_accuracy()]



def analyze1(sample_paragraph,typed_string,start_time,end_time):
    time=end_time-start_time
    return [typing_speed(typed_string,time),
            accuracy_test(sample_paragraph,typed_string)]

def typing_speed1(typed_string,time):
    num_char=len(typed_string)
    num_words=num_char/5
    return num_words/(time/60)

def accuracy_test1(sample_paragraph,typed_string):
    list_typed=split(typed_string)
    list_sample=split(sample_paragraph)
    length_typed=len(list_typed)
    length_sample=len(list_sample)
    num_correct=0
    if length_typed==0:
        return 0.0
    if length_typed<length_sample:
        for i in range(0,length_typed):
            if list_typed[i]==list_sample[i]:
                num_correct+=1;
        return 100*num_correct/length_typed
    else:
        for i in range(0,length_sample):
            if list_typed[i]==list_sample[i]:
                num_correct+=1;
        return 100*num_correct/length_sample
#need to put inside-hof
# END Q2
# BEGIN Q3
def pig_latin(word):
    if word[0] in 'aeiou':
        return word+'way'
    else:
        i=0
        while i<len(word):
            if word[i] in ['a','e','i','o','u']:
                return word[i:]+word[:i]+'ay'
            i+=1
        return word+'ay'

# END Q3
# BEGIN Q4
def autocorrect(user_input,words_list,score_function):
    if user_input in words_list:
        return user_input
    else:
        return min(words_list, key = lambda x: score_function(x,user_input))

# END Q4
# BEGIN Q5
def swap_score(word1,word2):
    if word1=="" or word2=="":
        return 0
    if word1[0]==word2[0]:
        return swap_score(word1[1:],word2[1:])
    else:
        return 1+swap_score(word1[1:],word2[1:])
# END Q5
# END Q1-5
# Question 6
def score_function1(word1, word2):
    word,wordd="",""
    """A score_function that computes the edit distance between word1 and word2."""
    def remove(word1,word2):
        if word1=="":
            return add(word1,word2)
        if len(word1)==1 and word1[0]==word2[0]:
            return add(word1,word2)
        if word1[0]==word2[0] and word1[1]==word2[1]:
            if len(word1)<=len(word2):
                return add(word1,word2)
            else:
                return 1+remove(word1[:-1],word2)
        else:
            return 1+remove(word1[1:],word2)
    def add(word1,word2):
        nonlocal word
        if len(word1)==len(word2):
            return substitute(word+word1,word+word2)
        elif word1[0]==word2[0]:
            word+=word1[0]
            return add(word1[1:],word2[1:])
        else:
            word+=word2[0]
            return 1+add(word1,word2[1:])
    def substitute(word1,word2):
        nonlocal wordd
        if word1=="" and word2=="":
            return 0
        elif word1[0]==word2[0]:
            wordd+=word1[0]
            return substitute(word1[1:],word2[1:])
        else:
            return 1+substitute(word1[1:],word2[1:])
    if len(word1)==len(word2) and swap_score(word1,word2)<len(word1):
        return substitute(word1,word2)
    if len(word1)<len(word2):
        if swap_score(word1,word2)==len(word1):
            return add(word1,word2)
        else:
            a=abs(len(word1)-len(word2))+substitute(word1,word2[:len(word1)])
            c=add(word1,word2)
            return min(a,c)
    return remove(word1,word2)

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""
    if word1 == word2:
        return 0
    elif not word1 or not word2:
        return max(len(word1), len(word2))
    elif word1[0] == word2[0]:
        return score_function(word1[1: ], word2[1: ])
    else:
        add_char = 1 + score_function(word1, word2[1:])
        remove_char = 1 + score_function(word1[1: ], word2)
        substitute_char = 1 + score_function(word1[1: ], word2[1: ])
        return min(add_char, remove_char, substitute_char)

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
dic1={}
def score_function_accurate(word1,word2):
    if word1 == word2:
        return 0
    elif not word1 or not word2:
        return max(len(word1), len(word2))
    elif word1[0] == word2[0]:
        return score_function_final(word1[1:], word2[1:])
    else:
        add_char = 1 + score_function_final(word1, word2[1:])
        remove_char = 1 + score_function_final(word1[1:], word2)
        substitute_char = KEY_DISTANCES[word1[0],word2[0]] + score_function_final(word1[1: ], word2[1: ])
        return min(add_char, remove_char, substitute_char)

def score_function_final(word1,word2):
    n,m=word1+word2,word2+word1
    def memoized(n,m):
        if n not in dic1 and m not in dic1:
            dic1[n]=score_function_accurate(word1,word2)
            return dic1[n]
        if n in dic1:
            return dic1[n]
        if m in dic1:
            return dic1[m]
    return memoized(n,m)




# END Q7-8
