# Creat a New flie and Writing something mode "w"

with open("C:/Users/vaibh/OneDrive/Desktop/VaibhavQB/File IO/Demo.txt", 'w') as f :
    
    f.write("This is a New File")

# Reading from the file and printing what's in the file

with open('C:/Users/vaibh/OneDrive/Desktop/VaibhavQB/File IO/Demo.txt', 'r') as f:
    print(f.read())

# Appending in the created file mode = 'a'

with open('C:/Users/vaibh/OneDrive/Desktop/VaibhavQB/File IO/Demo.txt', 'a') as f:
    f.write("\nAppending in the File")

# Reading again from the file and to check the appended message
with open('C:/Users/vaibh/OneDrive/Desktop/VaibhavQB/File IO/Demo.txt', 'r') as f:
    print(f.read())