from pyrsistent import b

bool_to_int = lambda value: int(value)
print(bool_to_int(True))
print(bool_to_int(False))

get_smaller = lambda a,b: min (a,b)
print ("get smaller:", (get_smaller(16,31)))
print ("get smaller:", (get_smaller(253,223)))

def cube (base):
  return (base**3)
print  (cube(3))
print  (cube(5))

def absolute_difference (a,b) :
  return abs ( a-b )
print ("absolute difference:", absolute_difference (14,11))
print ("absolue difference:", absolute_difference (13,40))

def squared_difference (a, b):
  return ((abs (a-b))**2)
print ("square_difference:", squared_difference (14,11))

def hours_to_minutes (hours):
  return (hours*60)
print ("hours_to_minutes:", hours_to_minutes ( hours = 3.5))
print ("hours_to_minutes:", hours_to_minutes ( hours = 12))

def get_circumference (radius):
  return (radius* 6.283185307179586)
print ("get_circumference:", get_circumference (radius = 9.2))

def linear_transform (x, slope, intercept):
  return (x*slope)+intercept
print ("linear_transform:", linear_transform (x=5.0, slope=3.0, intercept=-8.5))
print ("linear_transform:", linear_transform (x=2.5, slope=-2.1, intercept=17.0))

def standardize (x, x_center, scale_size):
  return ((x-x_center)/ scale_size)
print ("standardize:", standardize (x=8.2, x_center=13.8, scale_size=4.83))
print ("standardize:", standardize (scale_size=24.63, x=2.89, x_center=-72.813))
