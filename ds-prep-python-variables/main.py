first_name = 'Tiffany'
last_name = "Lin"
full_name = (first_name + " " + last_name)
print(full_name)
height_in_inches = 62
print ("height_in_inches:", height_in_inches, "type:", type(height_in_inches))
height_in_inches_float = float(height_in_inches)
print ("height_in_inches_float:", height_in_inches_float , "type:", type (height_in_inches_float))
height_in_meters = 0.0254 * height_in_inches_float
print ("height_in_meters:", height_in_meters)

eats_plants = True
eats_animals = False
is_animal = eats_animals or eats_plants
print (" is_animal: ",( is_animal))

is_omnivore = eats_animals and eats_plants
print (" is_omnivore: ", ( is_omnivore) )

is_plant = not is_animal
print (" is_plant: ", is_plant)

mean_height_in_meters = 1.7155
short_threshold_in_meters = 1.576
tall_threshold_in_meters = 1.860
is_mean_height = height_in_meters == mean_height_in_meters
is_short = height_in_meters < short_threshold_in_meters
is_tall = height_in_meters >= tall_threshold_in_meters
is_normal_height = short_threshold_in_meters <= height_in_meters < tall_threshold_in_meters
print ("is_mean_height:", is_mean_height,
       "is_short:", is_short,
       "is_tall:", is_tall,
       "is_normal_height:", is_normal_height )

nothing = None
print ("nothing:", nothing, type (nothing))
