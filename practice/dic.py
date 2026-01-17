# def find_in_L(Ld, k):
#     """ L is a list of dicts
#         k is an int
#     Returns True if k is a key in any dicts of L and False otherwise """
#     # your code here
#     for i in Ld:
#         if k in i:
#             return True
        
#     return False
        

# d1 = {1:2, 3:4, 5:6}
# d2 = {2:4, 4:6}
# d3 = {1:1, 3:9, 4:16, 5:25}
# print(find_in_L([d1, d2, d3], 2))  # returns True
# print(find_in_L([d1, d2, d3], 25))  # returns False


# def find_grades(grades, students):
#     """ grades is a dict mapping student names (str) to grades (str)
#         students is a list of student names 
#     Returns a list containing the grades for students (in the same order) """
#     # your code here
#     list_grades=[]
#     for i in students:
#         grade=grades[i]
#         list_grades.append(grade)
    
#     return list_grades

  

# d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
# print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A']



# def count_matches(d):
#     """ d is a dict
#     Returns how many entries in d have the key equal to its value """
#     # your code here
#     count=0
#     for i in d:
#         if i ==d[i]:
#             count+=1
#     return count

# d = {1:2, 3:4, 5:6}
# print(count_matches(d))   # prints 0

# # d = {1:2, 'a':'a', 5:5}
# # print(count_matches(d))   # prints 2

# de_kedi=d.keys()
# print(de_kedi)


# try:
#     print(d[99])
# except:
#     d[99]="VERİ YOK"
#     print(d[99])

# my_d ={'Ana':{'mq':[10], 'ps':[10,10]}, 
#        'Fredo':{'ps':[7,8], 'mq':[8]},
#        'Eric':{'mq':[3], 'ps':[0]}      }

# def get_average(data, what):
#     """ data is a dict like my_d above
#         what is 'ps' or 'mq'
#         Returns the average of all elements in data that match 'what' """
#     all_data = []
#     for stud in data:
#         all_data+=(data[stud][what])
#     return sum(all_data)/len(all_data)

# print(get_average(my_d, 'mq') )   # prints 7.0


song = "RAH RAH AH AH AH ROM MAH RO MAH MAH"

def generate_word_dict(song):
    """ song is a string
    Returns a dictionary whose:
    * keys are song words
    * values are the frequency of each key in song
    """
    # remove special characters and convert to lowercase
    song_words = song.lower()
    words_list = song_words.split()
    word_dict = {}
    for w in words_list:
        if w in word_dict:
            # seen word again, so add one to frequency
            word_dict[w] += 1
        else:
            # first time seeing word, insert a dict entry with freq 1
            word_dict[w] = 1
    # return is a dict mapping str:int like {'word1':1, 'word2':3}
    return word_dict

word_dict = generate_word_dict(song)
print(word_dict)
    



