passenger=(12, True, "Bonnell, Miss. Elizabeth", "female", 58)
print (passenger)
name= (passenger[2])
print ("name:",(name))
age= (passenger[-1])
print("age:", age)
survived_and_name= passenger[1:3]
gender_and_age= passenger[3:]
print ("survived_and_name:", survived_and_name, "gender_and_age:", gender_and_age)

is_female= "female" in passenger
print ("is_female:",is_female )
is_male= "male" in passenger
print ("is_male:", is_male)


def get_survival_info (passenger):
  (id, survived, name, gender, age)= passenger
  passenger = (age, gender, survived)
  return (passenger)
print (get_survival_info (passenger))

passenger = (11, True, "Sandstrom, Miss. Marguerite Rut", "female", 4)
print(get_survival_info(passenger))

passenger = (28, False, "Fortune, Mr. Charles Alexander", "male", 19)
print(get_survival_info(passenger))

passenger = (51, False, "Panula, Master. Juha Niilo", "male", 7)
print(get_survival_info(passenger))