person = {
  "first_name": "Tiffany",
  "last_name": "Lin",
  "hobby": "Cooking"
}
print ("person:",(person))

first_name = person ["first_name"]
last_name = person .get ("last_name")
middle_name = person .get ("middle_name")
print ("first_name:", (first_name),
       "last_name:", (last_name),
       "middle_name:", (middle_name))

person["job"]= "Data Operation Specialist"
print ("job:", person["job"])

person["hobby"]= "Dancing"
print ("change hobby:", person["hobby"])

person.pop("last_name")
print ("delete last name:",(person))
