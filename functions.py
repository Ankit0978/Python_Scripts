my_list =[1,3,4,5,6,7,8]
from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)
    return(my_list)

result = shuffle_list(["","o",""])
print(result)

def player_guess():
    guess=" "
    while guess not in ["0","1","2"]:
       guess = input("Pick a number between:0, 1 and 2")
    return int(guess)

player_guess()
index_count= player_guess()
print(index_count)



