import argparse
import json

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data['data']
    except FileNotFoundError:
        print("Error: Data file not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the data file.")
        exit(1)

def lookup_country_name(country_code, data):
    if country_code in data:
        return data[country_code]['name']
    else:
        return "Country code not found"

def main():
    parser = argparse.ArgumentParser(description="Lookup country names by country code")
    parser.add_argument("--countryCode", nargs='+', help="One or more country codes to look up")
    args = parser.parse_args()

    data = load_data("data.json")

    if args.countryCode:
        for code in args.countryCode:
            country_name = lookup_country_name(code.upper(), data)
            print(f"{code}: {country_name}")

if __name__ == "__main__":
    main()
