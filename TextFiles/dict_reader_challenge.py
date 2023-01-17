import csv

input_filename = 'country_info.txt'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    sample = ""
    for line in range(3):
        sample += country_file.read()
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    country_file.seek(0)
    reader = csv.DictReader(country_file, dialect=country_dialect)
    for row in reader:
        country_dict = row
        print(country_dict)

    countries[country_dict['Country']] = country_dict

print(countries)

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['Capital']}")
    elif chosen_country == 'quit':
        break
