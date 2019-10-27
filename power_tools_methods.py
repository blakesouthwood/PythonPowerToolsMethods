# Blake Southwood Software Engineer
# Sept 20, 2019 Silicon Valley
# Tested with PyDev on Eclipse on Macbook pro




#####################################################
##     Power Tool Methods For Python Version 1.0   ##
#####################################################

def swap(x,y):
    return y,x

# === list methods ===


def get_last_item(listname):
    it = eval("listname[-1]")
    return it

def get_first_item(listname):
    it = eval("listname[0]")
    return it

def add_to_end(word, listname):
    it = eval("listname.append('" + word + "')")
    return listname

def add_to_front(word, listname):
    it = eval("listname.insert(0, '" + word + "')")
    return listname

def delete_first_item(listname):
    del listname[0]
    return listname

def delete_last_item(listname):
    del listname[-1]
    return listname

def length_of_list(listname):
    return len(listname)

def sort_list(listname):
    listname.sort()
    return listname

def reverse_list(listname):
    listname.reverse()
    return listname

def get_pos_of_word(word, listname):
    mycounter = 0
    for item in listname:
        if item == word:
            return mycounter
        else:
            mycounter += 1
            continue

def tack_on_end_of_list(listname, secondlist):
    return listname.extend(secondlist)




# === string methods ===

def cap_string(string):
    word= str(string)
    return word.capitalize()

def clear_whitespaces(string):
    string = string.strip()
    newstring = string
    return newstring

def get_string_length(newstring):
    return len(newstring)

def make_lowercase(string):
    return string.lower()

def make_uppercase(string):
    return string.upper()


def find_word_in_string(word,string):    #find word in string ..... returns position it starts at
    it = eval("string.find('" + word + "')")
    print(it)


    #convert a string into a list
def string_to_list(string):
    newlist = list(string.split(" "))
    return newlist


thestring = """I like eggs on toast """

def replace_words(string1,string2):
    x = eval("thestring.replace('" + string1 + "','" + string2 +"')")
    thestring = x
    print(x)

print(replace_words("eggs","cream of wheat"))





#============ loop  ================
# still uses range() method but makes it more intuitive
# the built in method range() doesn't work as expected
# so a modified myrange(7) counts 0 - 7
# with one input argument
'''
for item in myrange(6):        #prints out 0 - 6
    print(item)
'''
#######################
##     myrange(x)
#######################
def myrange(x):
   return range(x+1)


# with 2 input arguments myrange2(1,7) counts 1 - 7
'''
for item in myrange2(1,7):       #prints out 1 - 7
    print(item)
'''
#######################
##     myrange2(x,y)
#######################
def myrange2(x,y):
   return range(x,y+1)




#===========  file methods   ==========

poem = """in the history of events
          at san jose airport
       """

# write to file
def write_to_file(name,words):
    print("writing to file...",name)
    file = eval("open('" + name + "', 'w+')")
    file.write(words)
    file.close()

write_to_file('mypoem.text',poem)


# append data to file
def append_file(name,morewords):
    file = eval("open('" + name + "', 'a+')")
    file.write(morewords)
    file.close()

morewords = "just a little something new"

append_file('mypoem.text',morewords)


#read a file
def read_file(name):
    print("reading from file.....",name)
    print("read file name =",name)
    file = eval("open('" + name + "', 'r')")
    if file.mode == 'r':
        for line in file:
            print(line)
    file.close()


read_file('mypoem.text')
#read file line by line


# ======  Dictionary Methods  ============


# enter the dictionary name and key name to get values
def get_keys_value(d,k):
    x = eval("" + d + ".get('" + k +"')")
    print(x)
    return x;

#example use
get_keys_value("fish","brand")


#get list of keys in dictionary name
def get_keys_in(dictname):
    allkeys = eval("list(" + dictname + ".keys())")
    print(allkeys)
    return allkeys

#example use entering dictionary name
get_keys_in("fish")
get_keys_in("car")





######################
##    fizzbuzz      ##
######################
def fizzbuzz():
    fb = 1
    while fb <= 100:
        if (fb % 3 != 0) and  (fb % 5 != 0):
            print(fb); fb += 1;         continue
        elif (fb % 3 == 0) and(fb % 5 == 0):
            print("fizzbuzz"); fb += 1; continue
        elif (fb % 5 == 0):
            print('buzz');fb +=1;       continue
        elif (fb % 3 == 0):
            print('fizz');fb +=1;       continue






##========================================
##          math equations
##========================================


#=======================================================
#          fibonacci series found everywhere in nature
#=======================================================

def fibonacci():
    list1 = [0,1]
    for item in range(20):               #change number in range for big numbers
        add = (list1[-1])+ (list1[-2])   #grab last 2 numbers
        list1.append(add)                #append total to next slot
        print(add);                      #show list


from math import *
#sample input data lists of x and y
listx = [4,44,95,33,61,43,55,5,48,59]
listy = [22,97,57,51,3,66,77,24,18,163]

##====== sq ==================
#============ square a number
def sq(x):
    return x * x


#===============================
#          correlation
#===============================
def correlation(listx, listy):
    print("number of pairs compared ",len(listx))
    s = len(listx); xy = list()
    x2 = list();    y2 = list()
    sum_x = sum_y = sum_xy = sum_x2 = sum_y2 = 0

    i = 0
    while i < s:  #loop through length of list of x and y
        xy.append(listx[i] * listy[i])
        x2.append(sq(listx[i]))
        y2.append(sq(listy[i]))
        i += 1
    #end while

    j = 0
    while j < s: # loop thru length of list x and y
        sum_x  += listx[j]
        sum_y  += listy[j]
        sum_xy += xy[j]
        sum_x2 += x2[j]
        sum_y2 += y2[j]
        j += 1
    #end while

    #calculations
    c1 = (s * sum_xy) - (sum_x * sum_y)
    c2 = (s * sum_x2) - sq(sum_x)
    c3 = (s * sum_y2) - sq(sum_y)
    c4 = sqrt(c2 * c3); ans = c1 / c4
    print("correlation =", ans)


correlation(listx,listy)


6



if __name__ == "__main__":
    main()
