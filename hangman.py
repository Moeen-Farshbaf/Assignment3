import random
true_ch = []
joon = 10
words = ["Book" , "Tree" , "Python" , "Bag" , "Umbrella" , "Dog" , "Clock" , "Engineer" , "Toothpast" , "Shir moz"]
word = random.choice(words)
word = word.lower()
print ("_ " * len(word) , ":")
while joon > 0:
    user_charater = input()
    if user_charater in word :
        true_ch.append(user_charater)
        print("_ " * len(word) ,  )
    else:
        print("no" , joon)
        joon = joon - 1
    test = 0
    for i in range(len(true_ch)):
            test = test + 1
    if test == len(word):
        print(word , "_ you win _")
        break
    if joon == 0:
        print("youre lose" , word)
        break
    for i in range(len(word)):
        if word[i] in true_ch:
            print(word[i],end="") 
        else:
            print("_ ",end="")