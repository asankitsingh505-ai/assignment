1 )task 1

try:
    file1 = open('my_file.txt', 'r')
    reading_file = file1.read()
    print(reading_file)
except FileNotFoundError:
    print("error: the file","does not found")

2)task 2


file1=open("output.txt","w")
writing =(input("enter text to write to the file:"))
file1.write(writing+"\n")
print("data successfully return to output.txt.")
file1.close()

file1=open("output.txt","a")
appending_data=(input("\nenter text to append to the file:"))
file1.write(appending_data+"\n")
print("data successfully appended.")
file1.close()

file1=open("output.txt","r")
print("\nfinal content of output.txt:")
print(file1.read())
file1.close()

