from bs4 import BeautifulSoup
import requests

_verbose = False


def scrape(url, inputs_and_outputs):
    if _verbose:
        print(f"scrape ( url: {url}, inputs_and_outputs: {inputs_and_outputs} )")

    request = requests.get(url)
    beautiful_soup = BeautifulSoup(request.content, "html.parser")

    results = {}

    for inputs_and_output in inputs_and_outputs:
        scrape_output = inputs_and_output["output"]

        scrape_output_found = False

        for scrape_input in inputs_and_output["inputs"]:

            if scrape_output in results:
                break

            find_result = beautiful_soup.find(scrape_input["type"], scrape_input["value"])
            if find_result is not None:
                results[scrape_output] = find_result.text
                scrape_output_found = True

        if scrape_output_found is False:
            results[scrape_output] = "?"

    request.close()

    return results
