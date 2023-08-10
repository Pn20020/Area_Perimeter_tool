# functions go here 

# checks users enter an integer to a given question 
def max_min(question):

  while True:

    try:
        response =  int(input(question))
        return response 

    except ValueError:
        print("Please enter an integer.")


# Main routine goes here 
 

while True: 

  measurements = max_min("measurements: ")

  if 2 <= measurements <= 100:
      pass
  elif measurements < 2:
      print("Sorry we dont do measurements under 2mm")
      continue 
  else:
      print("Sorry we dont do measurements over 100mm ") 
      continue

 



