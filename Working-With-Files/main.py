#with  open("C:\\Users\\Plass\\Desktop\\Python Self-Bootcamp\\Working-With-Files\\my_file.txt") as contents:
    #print(contents.read())
    #contents.close()
#print(contents)

with  open("C:\\Users\\Plass\\Desktop\\Python Self-Bootcamp\\Working-With-Files\\my_file.txt", mode="a") as contents:
    contents.write("New Text added.")