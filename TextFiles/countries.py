def capital_fun() -> None:
    """Display capital of the country."""
    while True:
        your_country = input("Name a country or a code: ")
        country_key = your_country.casefold()
        if country_key in countries:
            your_capital = countries[country_key]['capital']
            print(f"The capital of {your_country} is {your_capital}")
        elif country_key == 'q':
            break
        else:
            print(f"{your_country} doesn't exist.")


input_filename = 'country_info.txt'

countries = {}
with open(input_filename, encoding='utf-8') as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict

# print(countries)
capital_fun()
