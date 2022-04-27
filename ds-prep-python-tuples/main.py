passenger=(12, True, "Bonnell, Miss. Elizabeth", "female", 58)
print (passenger)
name= print ("name:",(passenger[2]))
age= print("age:", (passenger[-1]))
survived_and_name= passenger[1:3]
gender_and_age= passenger[3:]
print ("survived_and_name:", survived_and_name, "gender_and_age:", gender_and_age)

is_female= "female" in passenger
print ("is_female:",is_female )
is_male= "male" in passenger
print ("is_male:", is_male)


(id, survived, name, gender, age)= passenger
new_passenger = (age, gender, survived)
def get_survival_info (passenger):
  return (new_passenger)
print (get_survival_info (passenger))

passenger_1= (11, True, "Sandstrom, Miss. Marguerite Rut", "female", 4)
passenger_2= (28, False, "Fortune, Mr. Charles Alexander", "male", 19)
passenger_3= (51, False, "Panula, Master. Juha Niilo", "male", 7)

print (get_survival_info (passenger)+ passenger_1+ passenger_2+ passenger_3)
