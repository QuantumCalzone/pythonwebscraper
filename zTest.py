from pythonwebscraper.scrape_to_csv import *
from pythonwebscraper.web_scraper_dict_util import *

# web_scraper_dict_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTU2i_kU_8URPcwjHBbg2bLqoF1UWj-t1FuobfMyY6qWWjJhJur4ti0wfYjul_Z60EOkbE4mM4tNQNp/pub?output=csv"
# web_scraper_dict = get_web_scraper_dict(web_scraper_dict_url)
# # print(inputs_and_outputs)
# results = scrape("https://www.yelp.com/biz/pizzetta-211-san-francisco", web_scraper_dict)
# print(results)

from pythonwebscraper.scrape_to_csv import *
from pythonwebscraper.web_scraper_dict_util import *

web_scraper_dict_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRh-rxrCeGYVpmIqDXASa_z1J_lNUZ69uoZ5rg7-8nRSAt38MkI-D8_jhNZDi0AJfTB303hznNJa9Nf/pub?output=csv"
web_scraper_dict = get_web_scraper_dict(web_scraper_dict_url)
# print(inputs_and_outputs)
results = scrape("https://www.instagram.com/stories/quantumcalzone/", web_scraper_dict)
print(results)
