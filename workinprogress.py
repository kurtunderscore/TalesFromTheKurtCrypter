#!/bin/python3
# authored by KRT_,kurtunderscore, KRT_c0c4!N3

f=open("those_letters.txt", "r")
letters=f.read()
f.close()

AddKey = int(input("Enter your desired numerical key: "))
thecryptkeeper = ''

obituary = input('Type your message away: ')

for deadbod in obituary:
 if deadbod in letters:
    coffin = letters.find(deadbod)
    newCoffin = (coffin + AddKey) % len(letters)
    newDeadBod = letters[newCoffin]
    thecryptkeeper += newDeadBod
 else:
  	thecryptkeeper += deadbod
    
print ('Sending to all kiddies: ', thecryptkeeper)



