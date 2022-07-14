import re
largest_cities = open('largest_cities_germany.txt','r')
largest_cities_list = largest_cities.readlines()
cities = re.compile('\s[\w\s]+\s+')
city_names = []
for city_data in largest_cities_list:
    city_name = cities.findall(city_data)[0]
    city_names.append(city_name.strip())
postal_code = open('postal_codes_germany.txt','r')
cities_postal_data=postal_code.read()
city_dict = {}
for city in city_names:
    city_matches =  (re.findall('\s'+city+'\s[\d]+\s',cities_postal_data)[0:3])
    city_matches_str = "".join(city_matches)
    city_dict[city] = re.findall(r'[0-9]+', city_matches_str)
print (city_dict)
largest_cities.close()
postal_code.close()