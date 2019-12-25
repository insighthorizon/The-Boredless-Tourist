# data to test the functionality
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulso, Brazil", "Cairo, Egypt"]
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
print(test_destination_index)
