""" #string concatenation(adding strings together)
youtuber="lanelames"
#few ways to concate in python
print("1. Subscribe to "+youtuber)
print("2. Subscribe to {}".format(youtuber))
print(f"3. Subscribe to {youtuber}") #cleanest way """

adj=input("Adjective: ")
verb1=input("Verb1: ")
verb2=input("Verb2: ")
verb3=input("Verb3: ")
famous_person=input("Famous Person: ")
madlib=f"I am in love with my future self because she is so {adj}. \
I take care of myself by doing following activities {verb1}, {verb2}, {verb3}. I am following routine of {famous_person}."
print(madlib)

#random_madlibs
""" from sample_madlibs import hp, code, zombie, hungergames
import random
if __name__=="__main__":
    m=random.choice([hp,code,zombie,hungergames])
    m.madlib() """
