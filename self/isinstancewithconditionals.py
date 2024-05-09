def mean(value) :
    if isinstance(value,dict) :
        the_mean = sum(value.values())/len(value)
    else :
        the_mean = sum(value)/len(value)
    return the_mean
#list 
x= [1,2,3]
print(mean(x))
# Dictionary
y={"a":1,"b": 2,"c":3}
print(mean(y))