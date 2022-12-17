import requests
from bs4 import BeautifulSoup as bss4


url = requests.get("https://www.amazon.eg/deal/8be6a66c?ref=dlx_18022_sh_dcl_img_0_8be6a66c_dt_mese4_65")
soup = bss4(url.text , 'html.parser')
product_name = soup.findAll('a', {'class': 'a-size-base a-color-base a-link-normal a-text-normal'})

product_price = soup.findAll('span', {'class': 'a-price-whole'})
for i in range(len(product_price)):
    print(product_name[i].text)
    print(product_price[i].text)



