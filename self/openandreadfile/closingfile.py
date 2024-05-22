myfile = open("pythonlearning.txt", "r")
content = myfile.read()
print(content)
myfile.close()
#content = myfile.read() // if we will give read statement after closing the file it will through error
