import random
num= input("guess the no. uptill   ")

if num.isdigit():
        num=int(num)
        if num<=0:
            print("enter no.greater then 0 ")
            quit()
else:
               
    print("entr a no.")
    quit()
           

r=random.randint(0,num)


guesses=0
while True:
     guesses += 1
     guess=input("guess no. ")
     if guess.isdigit():
        guess=int(guess)
       
     else:
        print("enter a character")
        continue
     if guess==r:
          print("you won!")
            
          break
     else:
           if guess>r:
               print("guess a little low")
           else:
               print("guess a little high") 
         
               print("try again") 
          
     print("no. of guessear",guesses)     
  
