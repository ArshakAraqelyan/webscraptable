from django.http import HttpResponse
from django.http import JsonResponse
import requests
import bs4
import json
def webtablebs4(request):
    page=requests.get("https://www.worldometers.info/coronavirus/")

    soup= bs4.BeautifulSoup(page.text,'lxml')

    table=soup.find('table', id="main_table_countries_today")

    headers=[ heading.text for heading in table.find_all('th')]

    table_rows=[ row for row in table.find_all('tr')]

    results=[{headers[index]:cell.text for index,cell in enumerate(row.find_all("td")) }for row in table_rows]
    return JsonResponse({'results': results})


    # print(json.dumps(results))

    # for i in results:
    #     if "Country" in i:
    #         if i["Country"]=="India":
    #             print(i)
