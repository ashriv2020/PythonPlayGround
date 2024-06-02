# open a file and read it line by line
# using the with statement which closes the file automatically
# when the block of code is exited
def read_file():
    with open("myfile.txt", "r") as file:
        for line in file:
            print(line, end="")

read_file()

# open a file and write a new line to it
with open("myfile.txt", "a") as file:
    file.write("\nThis is a new line!\n")

read_file()