myfile = open("pythonlearning.txt") 
content=myfile.read()
#print(myfile.read()) # We will get empty string as cursor is at last line of file when ran first time
print(content)
print(content) # Now it will print two times
