'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    key= "th"
#    count = 0
#    for i in range(len(word)):
#        if key in word:
#            count +=1
#            return count
    
    if word == "": #if empty return nothing because you can't have th in 0 string
        return 0
    if key in word[0:2]:
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])