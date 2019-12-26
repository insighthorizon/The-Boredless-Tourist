# data to test the functionality
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ["Erin Wilkes", 'Shanghai, China', ['historical site', 'art']]

# functions to find index of destination, traveler's location ...
def get_destination_index(str_destination):
  destination_index = destinations.index(str_destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

#print(get_destination_index("Los Angeles, USA"))
#print(get_destination_index("Paris, France"))
#print(get_destination_index("Hyderabad, India"))

test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

#define attracitons as list of lists, ordered by destinations
attractions = [[] for destination in destinations]
#print(attractions)

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return
  except ValueError:
    print("The destination doesn't exist!")
    return
  
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  
  for possible_attraction in attractions_in_city:
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
        break
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ['art'])
#print(la_arts)
#print(find_attractions(test_traveler[1], test_traveler[2]))

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  
  interest_string = "Hi "
  interest_string += traveler[0]
  interest_string += ", we think you'll like the places around " + traveler_destination + ":"
  for attraction in traveler_attractions[:-1]:
    interest_string += " " + attraction + ","
  interest_string += " " + traveler_attractions[-1] + "."
  
  return interest_string


smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]) 
print(smills_france)

print(get_attractions_for_traveler(test_traveler))


  