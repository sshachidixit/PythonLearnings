def weather_condition(temp) :
    if temp > 7 :
        return "warm"
    else : 
        return "cold"
    
user_input = float(input("Enter temperature "))
print(weather_condition(user_input))