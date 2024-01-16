country = input("Country name: ")
visits = int(input("Number of visits: "))
list_of_cities = eval(input("List of cities visited: "))

travel_log = [
    {
        "country":  "France",
        "visits": 2,
        "cities": [
            "Paris",
            "Lille", 
            "Dijon",
        ]
    }
]

def add_new_country(country_name, visits_made, list_of_cities_visiteds):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = visits_made
    new_country["cities"] = list_of_cities_visiteds
    travel_log.append(new_country)
    # travel_log.append(
    #     {
    #         "country": country_name,
    #         "visits": visits_made,
    #         "cities": list_of_cities_visiteds,
    #     }
    # )

add_new_country(country_name=country, visits_made=visits, list_of_cities_visiteds=list_of_cities)

print(travel_log)
print("")
print(f"I've been to {travel_log[1]['country']} {travel_log[1]['visits']} times")
print(f"My favourite city was {travel_log[1]["cities"][0]}.")
