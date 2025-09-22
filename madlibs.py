"""
Name: Ace Keddie
Date: 2025-09-17
Course: ICS3U
Assignment: Madlib Project
"""

#will take inputs for place, animals, verb, number, adjective, and plural noun  
#words that have been inputted will go into the story  
 
while True: 
    print("PREVIEW\nTonight, I'm going to [place] and while there I'm going to have a [adjective] time\nI saw a [adjective] [animal] which was [number] years old\nbefore I left [place] I got to see [verb] [plural_noun]\non my way back from [place] I started [verb] uncontrollably, but I still perservered on my way home\nI made it to the final stretch, still, that is [number] meters away from home") 
 
 
    place = input("Enter a place\n>")  
    adjective = input("Enter an adjective\n>")  
    animal = input("Enter an animal\n>")  
    verb = input("Enter a verb(please have 'ing' at the end of the verb)\n>")  
    number = int(input("Enter a number\n>"))  
    plural_noun = input("Enter a plural noun\n>")  
     
    print("Tonight, I'm going to", place, "and while there I'm going to have a" ,adjective,"time")  
    print(f"I saw a {adjective} {animal} which was {number} years old")  
    print(f"before I left {place} I got to see a {verb} {plural_noun}")  
    print(f"on my way back from {place} I started {verb} uncontrollably, but I still persevered on my way home")  
    print(f"I made it to the final stretch, still, that is {number+52} meters away from home")  
    while True: 
        again = input("do you wanna run it back (yes/no)\n>") 
        if again.lower()  == 'yes': 
             break 
        elif again. lower() == 'no': 
            quit() 
        else: 
            print("Invalid input. Please answer 'yes' or 'no'.") 