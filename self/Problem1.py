# userinput = input("Say something: ")
# if userinput != "How are you" :
#     break
#     print(userinput)

# #print(userinput)
# while True:
#     if userinput != "How are you" :
#         break
#     else :
#         continue

#     if userinput == "\end" :
#         print(userinput)

#First we will create a function sentance maker:

def sentancemaker(phrase):
    intro =("how","why","when")
    capitalized = phrase.capitalize()
    if phrase.startswith(intro) :
        return "{}?".format(capitalized)
    else :
        return "{}.".format(capitalized)

#print(sentancemaker("how is things here"))

result = []

#import pdb; pdb.set_trace()
while True :
    user_input = input("Say something: ")
    
    if user_input == "\end" :
        break
    else :
        result.append(sentancemaker(user_input))
print(" ".join(result))
