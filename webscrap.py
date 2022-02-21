from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np
import urllib.request
import urllib.parse

results = []
product_names = []
prices = []
rating_review_count = []
relative_urls = []
product_details = []

root_url = "https://www.flipkart.com/"
url_combined = []

for i in range(1,14):
    url = "https://www.flipkart.com/search?q=realme+mobile&sort=relevance&page="+str(i)

    response = requests.get(url)
    # print(response.status_code)
    soup = BeautifulSoup(response.content, 'lxml')
    soup.prettify()
# result
    results = soup.find_all('div', {'class': '_13oc-S'})
    print(len(results))
    for result in results:
        # name
        try:
         product_names.append(result.find(
             'div', {'class': "_4rR01T"}).get_text())
        except:
           product_names.append("n/a")

        # price

        try:
            prices.append(result.find(
                'div', {'class': '_30jeq3 _1_WHN1'}).get_text())
        except:
           prices.append("n/a")

    # reviews_count

        try:
            rating_review_count.append(result.find('span', {'class': '_2_R_DZ'}).get_text().replace('\xa0',' '))
        except:
           rating_review_count.append("n/a")
     
    # relative_urls

        try:
            relative_urls.append(result.find( 'a', {'class': '_1fQZEK'}).get('href'))
        except:
            relative_urls.append("n/a")
    
    # product_details
        try:
            product_details.append(result.find('ul', {'class': '_1xgFaf'}).get_text())

        except:
            product_details.append("n/a")

# url_combined
try:
    for link in relative_urls:
        url_combined.append(urllib.parse.urljoin(root_url,link))
except:
       url_combined.append("n/a")
print(len(relative_urls))             
#print(len(url_combined))
#print(rating_review_count)

a={'PRODUCT_NAME': product_names,'PRODUCT_PRICE':prices,'PRODUCT ALL FEATURES':product_details,'RATING AND REVIEWS':rating_review_count,'LINK TO THE PRODUCT':url_combined}
df = pd.DataFrame.from_dict(a, orient='index')
product_overview = df.transpose()
product_overview.to_excel("product_overview.xlsx",index=True)
#print(df)





