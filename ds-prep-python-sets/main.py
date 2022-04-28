trail_mix= {"m&ms", "peanuts", "raisins"}
print(trail_mix)

print("cashew" in trail_mix)
print("peanuts" in trail_mix)

#add-1
trail_mix.add("pretzels")
print(trail_mix)

#add-2
snack_mix={"peanuts", "banana chips", "bits of jerky"}
trail_mix.update(snack_mix)
print(trail_mix)

#remove
trail_mix.remove("m&ms")
trail_mix.discard("raisins")
trail_mix.discard("rat poison")
print(trail_mix)

nuts={"peanuts", "cashews", "almonds", "walnuts", "pecans"}
#inclues everything in "trail_mix" and "nuts"
all= trail_mix.union(nuts)
print(all)

#includes things that are both in "trail_mix" and "nuts"
both= trail_mix.intersection(nuts)
print(both)

#includes all things that are in "trail_mix" but not in "nuts"
diff= trail_mix.difference(nuts)
print(diff)

#include all things that are in "nuts" but not in "trail_mix"
diff1= nuts.difference(trail_mix)
print(diff1)
