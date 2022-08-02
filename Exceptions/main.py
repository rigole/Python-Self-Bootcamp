#with open("a_file.txt") as file:
#    file.read()
 
 
#try:
#    file = open("a_file.txt")
#except:
#    file = open("a_file.txt", "w")
 

#Exercice 1

""" 
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:  
        print("fruit Pie")
    else:
        print(fruit + " pie")
make_pie(4)
"""
# exercice 2




facebook_posts = [
    {'Likes':21, 'Comments': 2},
    {'Likes' : 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares':2},
    {'Comments': 1, 'Shares':1},
    {'Likes': 19, 'Comments':3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
        total_likes += 0
        
    

print(total_likes)