print("Hello World")
counties=["Arapahoe","Denver","Jefferson"]
if counties[1]=='Denver':
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties or "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

#get keys of a dictionary
counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)

#get values of a dictionary
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))

#get key value pairs of a dictionary 
for county,voters in counties_dict.items():
    print(county,voters)

for county,voters in counties_dict.items():
    print(county,"county has",voters,"registered voters.")

#get each dictionary in a list of dictionaries
voting_data = [{"county":"Arapahoe","registered_voters":422829},
                {"county":"Denver","registered_voters":463353},
                {"county":"Jefferson","registered_voters":432438}]
for county_dict in voting_data:
    print(county_dict)

#nested loop to get the values from each dictionary in a list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#skill drill 1: printing each countya dn registered voter from the dictionary
counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
for county in counties_dict.keys():
    print (county)
for voters in counties_dict.values():
    print(voters)
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#skill drill 2: printing each county and registered voter from the dictionary 

