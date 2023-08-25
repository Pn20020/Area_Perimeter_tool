import math 
def radius(question):
  if shapes_list == "cirlce":


# functions go here 

# checks users enter an float to a given question 

  
    while True:

      try:
        response = float(input(question))
        if response <= 2:
          print("Please choose a number over 2mm")
        else:
          return response 
      except ValueError:
        print("Please enter an a valid raidus.")


# Main routine goes here 
shape_raidus = 1
raidus_asked = 0



# ensures that there is a minimum and maximum 


while True: 
  shape_raidus = radius("Please enter the width for your shape ")

  if shape_raidus == raidus_asked:
    break

    if 2 <= shape_raidus <= 100:
      pass
    elif shape_raidus < 2:
      print("Sorry we dont do measurements under 2mm")
      continue 
  else:
      print("Sorry we dont do measurements over 100mm ") 
      continue

  raidus_asked += 1
