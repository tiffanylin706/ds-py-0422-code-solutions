#if, else
day_of_week= "wednesday"
if day_of_week == "saturday":
  print ("Have a good weekend!")
if day_of_week == "sunday":
  print ("Have a good weekend!")
else:
  print ("It's a weekday!")

student_1_score= 60
pass_or_fail= "You Failed!"
if student_1_score <= 70:
  print (pass_or_fail)

#if, elif, and else
student_2_score= 88
if student_2_score < 60:
  print (student_2_score, "F")
elif 60 <= student_2_score < 70:
  print (student_2_score, "D")
elif 70 <= student_2_score <80:
  print (student_2_score, "C")
elif 80 <= student_2_score < 90:
  print (student_2_score, "B")
elif 90<= student_2_score < 100:
  print (student_2_score, "A")
else:
  print (student_2_score, "A+")

def get_season_info (season):
  if season == "summer":
   return "Statistically, it's likely to be hotter today than in 6 months from now. Don't sweat it, though."
  elif season == "spring":
    return "The flowers are blooming while it's spring, but that correlation, not causation."
  elif season == "winter":
    return "There may only be a high likelihood of it being cold today, but there's a 100 percent chance of me wanting that sweater."
  elif season == "autumn":
    return "The leaves seem to regress to warmer colors as autumn approaches its end."
  else:
    print("That's not a season. Most likely.")
print ("summer:", get_season_info("summer"))
print ("winter:", get_season_info("winter"))
print ("autumn:", get_season_info("autumn"))
print ("spring:", get_season_info("spring"))
print (get_season_info("apple"))

#Short Hand If ... Else
age = 42
print ("adult") if age >= 18 else print ("child")
