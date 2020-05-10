import csv
import requests

_verbose = False


def get_web_scraper_dict(web_scraper_dict_url):
    if _verbose:
        print(f"get_web_scraper_dict ( web_scraper_dict_url: {web_scraper_dict_url} )")

    web_scraper_dict_data = requests.get(url=web_scraper_dict_url)
    web_scraper_dict = web_scraper_dict_data.content
    # print(web_scraper_dict)
    web_scraper_dict = str(web_scraper_dict)

    web_scraper_dict = web_scraper_dict[2:]  # remove first two chars
    web_scraper_dict = web_scraper_dict[:-1]  # remove last char

    web_scraper_dict = web_scraper_dict.split("\\r")
    csv_file = csv.reader(web_scraper_dict, delimiter=',')

    header_dict = {}
    names_and_xpaths_dict = {}

    for row in csv_file:
        row[0] = row[0].replace("\\n", "")

        if len(header_dict) == 0:
            index = 0
            for entry in row:
                header_dict[entry] = index
                index += 1
        else:
            name = row[0]
            xpath = row[1]
            # print(f"name: {name} , xpath: {xpath}")

            if name not in names_and_xpaths_dict:
                names_and_xpaths_dict[name] = {
                    "name": name,
                    "xpaths": []
                }

            names_and_xpaths_dict[name]["xpaths"].append(xpath)

    web_scraper_dict_data.close()
    # print(inputs_and_outputs_dict)

    names_and_xpaths = []
    # print(names_and_xpaths_dict)
    for name_and_xpaths_key in names_and_xpaths_dict:
        # print(f"name_and_xpaths_key: {name_and_xpaths_key}")
        name_and_xpaths = names_and_xpaths_dict[name_and_xpaths_key]
        # print(f"name_and_xpaths: {name_and_xpaths}")
        names_and_xpaths.append(name_and_xpaths)

    return names_and_xpaths
