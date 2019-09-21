# Blake Southwood Software Engineer
# Sept 20, 2019 Silicon Valley
# Tested with PyDev on Eclipse on Macbook pro




#####################################################
##     Power Tool Methods For Python Version 1.0   ##
#####################################################

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


def find(word,string):    #find word in string ..... returns position it starts at
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




######################
##    fizzbuzz      ##
######################
def fizzbuzz():
    fb = 1
    while fb <= 100:

        if (fb % 3 != 0) and (fb % 5 != 0):
            print
            print(fb)
            fb += 1
            continue

        elif (fb % 3 == 0) and (fb  % 5 == 0) :
            print("fizzbuzz") # the number of course
            fb += 1
            continue

        elif (fb % 5 == 0):
            print('buzz') # by 5
            fb +=1
            continue

        elif (fb % 3 == 0) :
            print('fizz') #by 3
            fb +=1
            continue









if __name__ == "__main__":
    main()
