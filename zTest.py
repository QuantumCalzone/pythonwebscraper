from pythonwebscraper.scrape_to_csv import *
import requests
import csv

web_scraper_dict_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTU2i_kU_8URPcwjHBbg2bLqoF1UWj-t1FuobfMyY6qWWjJhJur4ti0wfYjul_Z60EOkbE4mM4tNQNp/pub?output=csv"
web_scraper_dict_data = requests.get(url=web_scraper_dict_url)
web_scraper_dict = web_scraper_dict_data.content
print(web_scraper_dict)
web_scraper_dict = str(web_scraper_dict)

web_scraper_dict = web_scraper_dict[2:]  # remove first two chars
web_scraper_dict = web_scraper_dict[:-1]  # remove last char

web_scraper_dict = web_scraper_dict.split("\\r")
csv_file = csv.reader(web_scraper_dict, delimiter=',')
header_dict = {}
inputs_and_outputs_dict = {}
for row in csv_file:
    row[0] = row[0].replace("\\n", "")

    if len(header_dict) == 0:
        index = 0
        for entry in row:
            header_dict[entry] = index
            index += 1
    else:
        output = row[0]
        # print(f"output: {output}")

        if output not in inputs_and_outputs_dict:
            inputs_and_outputs_dict[output] = {
                "output": output,
                "inputs": []
            }

        inputs_and_output_type = row[header_dict["Type"]]
        inputs_and_output_value_type = row[header_dict["Value Type"]]
        inputs_and_output_value = row[header_dict["Value"]]

        inputs_and_output_key = {
            "type": inputs_and_output_type,
            "value": {
                inputs_and_output_value_type: inputs_and_output_value
            }
        }

        inputs_and_outputs_dict[output]["inputs"].append(inputs_and_output_key)
        # print(f"inputs_and_output: {inputs_and_output}")
        # print(f"inputs_and_output[output]: {inputs_and_outputs_dict[output]}")

web_scraper_dict_data.close()
# print(inputs_and_outputs_dict)

inputs_and_outputs = []
for inputs_and_output_key in inputs_and_outputs_dict:
    inputs_and_outputs.append(inputs_and_outputs_dict[inputs_and_output_key])

results = scrape("https://www.yelp.com/biz/pizzetta-211-san-francisco", inputs_and_outputs)
print(results)
