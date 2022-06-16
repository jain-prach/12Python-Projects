""" #string concatenation(adding strings together)
youtuber="lanelames"
#few ways to concate in python
print("1. Subscribe to "+youtuber)
print("2. Subscribe to {}".format(youtuber))
print(f"3. Subscribe to {youtuber}") #cleanest way """

""" #first madlib game
adj=input("Adjective: ")
verb1=input("Verb1: ")
verb2=input("Verb2: ")
verb3=input("Verb3: ")
famous_person=input("Famous Person: ")
madlib=f"I am in love with my future self because she is so {adj}. \
I take care of myself by doing following activities {verb1}, {verb2}, {verb3}. I am following routine of {famous_person}."
print(madlib) """ \


#using string replace method
import random
f=open('madlibs.txt','r') #open txt file
counter=0;
madliblist=f.readlines() #read file and store each line in a list
""" #counting no of lines in list
for i in madliblist:
    if i:
        counter+=1
print(counter) """
madlib=random.choice(madliblist)
print(madlib)
verb=input("verb: ")
madlib=madlib.replace("blank", verb)
print(madlib)