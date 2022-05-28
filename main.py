from asyncore import read
from itertools import count
from unittest import result

def read_file_content(filename):
    with open('./story.txt', 'r')as f:
        file = f.read()
    return file
result = read_file_content('./story.txt')
print(result) 

def count_words():
    text = read_file_content("./story.txt")
    split_text = text.split()
    print(split_text)
    count={}
    for words in split_text:
        if words in count:
            count[words] +=1
        else:
            count[words] =1
    return count
print(count_words())