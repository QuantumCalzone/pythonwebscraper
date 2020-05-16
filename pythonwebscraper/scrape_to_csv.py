from lxml import etree
from urllib.request import urlopen

_verbose = False


def scrape(url, web_scraper_dict):
    if _verbose:
        print(f"scrape ( url: {url}, web_scraper_dict: {web_scraper_dict} )")

    results = {}
    response = urlopen(url)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    for names_and_xpaths in web_scraper_dict:
        name = names_and_xpaths["name"]
        xpaths = names_and_xpaths["xpaths"]
        # print(f"name: {name} xpaths: {xpaths}")
        for xpath in xpaths:
            result = tree.xpath(xpath)

            if len(result) == 0:
                return None

            result = result[0]
            if result is not None:
                # print(result.text)
                results[name] = result
                break

    return results
