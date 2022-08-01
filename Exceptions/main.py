#with open("a_file.txt") as file:
#    file.read()
 
 
#try:
#    file = open("a_file.txt")
#except:
#    file = open("a_file.txt", "w")
 

#Exercice 1
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:  
        print("fruit Pie")
    else:
        print(fruit + " pie")
make_pie(4)