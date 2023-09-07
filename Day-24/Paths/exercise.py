# Moved the new_file.txt to the desktop folder.

# Absolute Path
with open("/Users/laptop/Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)


# Relative Path
with open("../../../../Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)