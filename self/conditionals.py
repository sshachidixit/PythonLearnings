# If a function is not working for dictionary and only working for list type 
#then we will use conditionals

# If-conditionals
def mean(listdict) :
    if type(listdict) == dict:
        the_mean = sum(listdict.values())/len(listdict)
        
    else:
        the_mean = sum(listdict)/len(listdict)
    return the_mean
    
#x=[1,2,3]
#print(mean(x))
y={"a":1,"b":2,"c":3}
print(mean(y))