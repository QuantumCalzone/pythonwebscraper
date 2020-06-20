from lxml import etree
from urllib.request import urlopen

_verbose = True


def scrape(url, web_scraper_dict):
    if _verbose:
        print(f"scrape ( url: {url}, web_scraper_dict: {web_scraper_dict} )")

    results = {}
    response = urlopen(url)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)

    # if _verbose:
    #     root = tree.getroot()
    #     print(f"root: {root}")
    #     tree_print = etree.tostring(root, pretty_print=True, method="html")
    #     print(f"tree_print: {tree_print}")

    for names_and_xpaths in web_scraper_dict:
        name = names_and_xpaths["name"]
        xpaths = names_and_xpaths["xpaths"]

        if _verbose:
            print(f"name: {name} xpaths: {xpaths}")

        for xpath in xpaths:

            result = tree.xpath(xpath)

            if _verbose:
                print(f"result: {result}")

            if len(result) == 0:
                break

            result = result[0]
            if result is not None:
                # print(result.text)
                results[name] = result
                break

    return results
