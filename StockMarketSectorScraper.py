import requests
from bs4 import BeautifulSoup

def fidelity_sector_report():
    result = {}
    result['results'] = {}
    response = requests.get("https://eresearch.fidelity.com/eresearch/goto/markets_sectors/landing.jhtml")
    results_page = BeautifulSoup(response.content, 'lxml')
    results = results_page.findAll("a", class_="heading1")
    for sector in results:
        link = "https://eresearch.fidelity.com" + sector['href']
        response = requests.get(link)
        results_page = BeautifulSoup(response.content, 'lxml')
        sector_name = results_page.find("div", class_="page-title").find("h1").getText()
        #print(sector_name)
        result['results'][sector_name] = {}
        enterprise_value = results_page.find("div", class_="sec-fundamentals").findAll("tr")[3].find("td").getText().strip()[:-1][1:]
        #print(enterprise_value)
        result['results'][sector_name]['enterprise_value'] = enterprise_value
        return_on_equity = results_page.find("div", class_="sec-fundamentals").findAll("tr")[7].find("td").getText().strip()[:-1]
        #print(return_on_equity)
        result['results'][sector_name]['return_on_equity'] = return_on_equity
        dividend_yield = results_page.find("div", class_="sec-fundamentals").findAll("tr")[10].find("td").getText().strip()[:-1]
        #print(return_on_equity)
        result['results'][sector_name]['dividend_yield'] = dividend_yield
    return result
print(fidelity_sector_report())
