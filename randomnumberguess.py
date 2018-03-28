import random
def guessnumber():
    guess =0
    guess_number = random.randint(1,9)
    while(True):
        number = (raw_input("PLease enter a number or type exit if you want to quit:"))
        guess+=1
        if (number=='exit'):
            return
        elif (int(number)<guess_number):
            print "Number is too low "
        elif(int(number)>guess_number):
            print"Number is too high"
        else:
            print ("Congratulations !!! You guessed  the number in %d guesses" %guess)
            return
guessnumber()
