import time  #time built in module is used here for sleep method.

while True:
    with open("pythonlearning.txt") as myfile: #with context manager will close the file implicitly
        print(myfile.read())
        time.sleep(3)