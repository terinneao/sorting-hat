import random

student_list = ["Mark", "Amber", "Todd", "Anita", "Sandy", "Mike", "John", "Mary", "Stephen", "Sam",
                    "Ann", "Lisa", "Adam", "Jerrard", "Brook", "Dan", "Don", "May", "Boy", "Nat",
                    "Art", "Tom", "Judy", "Mick", "Joy", "Brad", "David", "Alex", "Tum", "Not",
                    "Big", "Jom", "Tong", "Top", "Samuel", "Sea", "Sun", "Fluke", "Max", "Patt",
                    "Peter", "Josh", "Kathy", "Golf", "Kavin", "Roy", "Yo", "Luka", "Lucy", "Beck"            
                ]

Gryffindor = []
Hufflepuff = []
Ravenclaw = []
Slytherin = []
house_list = [Gryffindor, Hufflepuff, Ravenclaw, Slytherin]
house_list2= [Gryffindor, Hufflepuff, Ravenclaw, Slytherin]
house_namelist = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
            

for student in student_list:
    house = random.choice(house_list)
    if len(house) > 12:
        house_list.remove(house)
        house = random.choice(house_list)
    else:
        pass
    house.append(student)
            
for (value1, value2) in enumerate(zip(house_namelist, house_list2)): 
    result = value2[0] +" has "+ str(len(value2[1])) +" students"
    print(value2[0] +" has "+ str(len(value2[1])) +" students")
    