#open and read and store contents in flag as f
f=open("flag.txt", "r")
flag = f.read()

#open and read and store contents in "key"
g = open("key.txt" , "r")
key = g.read()

#Only get the first 4 characters of the key, this will be a constraint
key = key[0:4]

"""
First is declares a list where it is going to store the result
text contains the flag string
"""
def enc(text,key):
    encrypted = []
    #It the gets the length of the flag and it divides it by 4(it makes groups of four, the same length than the key)
    #It rounds the results and enforces it as an int
    #example if the flag is 12 chars this for statement will loop from 0 to 2(range goes from 0 to the second parameter)
    for i in range(int(round(len(text)/4))):
        #takes each group of four and calls spicy() with these 3 parameters
        #the group of 4 chars of the flag the i and full key (of 4 chars too)
        shifted = spicy(text[i*4:(i+1)*4],i,key)
        encrypted.append(shifted)
    return encrypted

def spicy(text,offset,key):
    res = []
    for p in range(len(text)):
        res.append(int((ord(text[p])+offset)^ord(key[p])))
    return res
"""
in the variable 'text' we have the group of four chars of flag; in 
offset, the number of the group starting at 0 and in key; and in key, the full key.
It declares a variable “res” that is a list. There it is going to store the spicy() result.
Then, the for loop goes from 0 to the length of text minus 1. As text has 4 chars, 
it will always go from 0 to 3.
"""

"""
returns a list of sublists and for each sublist
and for each element of the sublist, the element is appended to a
flat_list that is going to be the result stored in enc.txt
"""
flat_list = []
for sublist in enc(flag,key):
    for item in sublist:
        flat_list.append(item)

f=open("enc.txt","w+")
f.write(str(flat_list))