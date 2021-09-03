# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000, "B": 1000000000}
# Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded"
# test function by updating damages
def converted_damages(damages):
  updated_damages = []
  for damage in damages:
    if damage[-1] == "M":
      updated_damages.append(float(damage.strip("M"))*conversion["M"])
    elif damage[-1] == "B":
      updated_damages.append(float(damage.strip("B"))*conversion["B"])
    else:
      updated_damages.append('Damages not recorded')
  return updated_damages
updated_damages = converted_damages(damages)
print(updated_damages)
print("\n")
# 2 
# Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane
# Create a Table
def create_hurricane_dict(names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths):
  hurricane_records = {}
  index = 0
  for name in names:
    hurricane_records[name] = {"Name": names[index],
     "Month": months[index],
     "Year": years[index],
     "Max Sustained Wind": max_sustained_winds[index],
     "Areas Affected": areas_affected[index],
     "Damage": updated_damages[index],
     "Deaths": deaths[index]}
    index += 1
  return hurricane_records

# Create and view the hurricanes dictionary
hurricane_records = create_hurricane_dict(names,months, years,max_sustained_winds,areas_affected,updated_damages,deaths)
print(hurricane_records)
print("\n")
# 3
# Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.
# Organizing by Year
def Organizing_by_year(hurricane_records):
  hurricane_by_years = {}
  for record in hurricane_records:
    years=hurricane_records[record]["Year"]
    hurricane_details = hurricane_records[record]
    if years not in hurricane_by_years:
      hurricane_by_years[years] = [hurricane_details]
    else:
      hurricane_by_years[years].append(hurricane_details)
  return hurricane_by_years

# create a new dictionary of hurricanes with year and key
hurricane_by_years = Organizing_by_year(hurricane_records)
print(hurricane_by_years)
print("\n")
# 4
# Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected.
# Counting Damaged Areas
def count_damaged_areas(hurricane_records):
  affected_areas_frequency = {}
  for record in hurricane_records:
    for area in hurricane_records[record]['Areas Affected']:
      if area not in affected_areas_frequency:
        affected_areas_frequency[area] = 1
      else:
        affected_areas_frequency[area] += 1
  return affected_areas_frequency

# create dictionary of areas to store the number of hurricanes involved in
affected_areas_frequency = count_damaged_areas(hurricane_records)
print(affected_areas_frequency)
print("\n")

# 5 
# Write a function that finds the area affected by the most hurricanes, and how often it was hit.
# Calculating Maximum Hurricane Count
def max_hurricane_count(affected_areas_frequency):
  max_value = None
  for area in affected_areas_frequency:
    if max_value is None or max_value < affected_areas_frequency[area]:
      max_value = affected_areas_frequency[area]
      max_area = area
  return max_area, max_value

# find most frequently affected area and the number of hurricanes involved in
area_affected_by_most_cane = max_hurricane_count(affected_areas_frequency)
print(area_affected_by_most_cane)
print("\n")

# 6
# Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.
# Calculating the Deadliest Hurricane
def deadliest_cane(hurricane_records):
  max_deaths = None
  for record in hurricane_records:
    if max_deaths is None or max_deaths < hurricane_records[record]["Deaths"]:
      max_deaths =  hurricane_records[record]["Deaths"]
      max_cane = record
  return max_cane, max_deaths

# find highest mortality hurricane and the number of deaths
highest_mortality_cane = deadliest_cane(hurricane_records)
print(highest_mortality_cane)
print("\n")

# 7
# Store the hurricanes in a new dictionary where the keys are mortality ratings and the values are lists containing a dictionary for each hurricane that falls into that mortality rating.
# Rating Hurricanes by Mortality
def hurricane_rating(hurricane_records):
 mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
 hurricane_by_ratings = {0:[],1:[],2:[],3:[],4:[],5:[]}
 for record in hurricane_records:
   if hurricane_records[record]["Deaths"] <= mortality_scale[0]:
     hurricane_by_ratings[0].append(hurricane_records[record])
   elif hurricane_records[record]["Deaths"] <= mortality_scale[1]:
     hurricane_by_ratings[1].append(hurricane_records[record])
   elif hurricane_records[record]["Deaths"] <= mortality_scale[2]:
     hurricane_by_ratings[2].append(hurricane_records[record])
   elif hurricane_records[record]["Deaths"] <= mortality_scale[3]:
     hurricane_by_ratings[3].append(hurricane_records[record])
   elif hurricane_records[record]["Deaths"] <= mortality_scale[4]:
     hurricane_by_ratings[4].append(hurricane_records[record])
   elif hurricane_records[record]["Deaths"] > mortality_scale[4]:
     hurricane_by_ratings[5].append(hurricane_records[record])
 return hurricane_by_ratings

# categorize hurricanes in new dictionary with mortality severity as key
hurricane_by_ratings = hurricane_rating(hurricane_records)
print(hurricane_by_ratings)
print("\n")

# 8 Calculating Hurricane Maximum Damage
# Write a function that finds the hurricane that caused the greatest damage, and how costly it was.
def max_damage(hurricane_records):
  max_damage = None
  for record in hurricane_records:
    if hurricane_records[record]["Damage"] == "Damages not recorded":
      continue
    if max_damage is None or max_damage < hurricane_records[record]["Damage"]:
      max_damage = hurricane_records[record]["Damage"]
      max_cane = record
  return max_cane, max_damage


# find highest damage inducing hurricane and its total cost
highest_damage_cane = max_damage(hurricane_records)
print(highest_damage_cane)
print("\n")
# 9 
#Store the hurricanes in a new dictionary where the keys are damage ratings and the values are lists containing a dictionary for each hurricane that falls into that damage rating.
# Rating Hurricanes by Damage
def cane_damage_rating(hurricane_records):
  damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
  damage_rating = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for record in hurricane_records:
    if hurricane_records[record]["Damage"] == "Damages not recorded":
      continue
    if hurricane_records[record]["Damage"] <= damage_scale[0]:
      damage_rating[0].append(hurricane_records[record])
    elif hurricane_records[record]["Damage"] <= damage_scale[1]:
      damage_rating[1].append(hurricane_records[record])
    elif hurricane_records[record]["Damage"] <= damage_scale[2]:
      damage_rating[2].append(hurricane_records[record])
    elif hurricane_records[record]["Damage"] <= damage_scale[3]:
      damage_rating[3].append(hurricane_records[record])
    elif hurricane_records[record]["Damage"] <= damage_scale[4]:
      damage_rating[4].append(hurricane_records[record])
    elif hurricane_records[record]["Damage"] > damage_scale[4]:
      damage_rating[5].append(hurricane_records[record])

  return damage_rating 
# categorize hurricanes in new dictionary with damage severity as key
damage_rating_severity = cane_damage_rating(hurricane_records)
print(damage_rating_severity)








