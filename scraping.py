# from requests import get
# from bs4 import BeautifulSoup
#
# URL = "https://www.amazon.in/Canon-1500D-24-1MP-Digital-55-250mm/dp/B07BRR59DT/ref=bmx_4/257-7494594-7287510?_encoding=UTF8&pd_rd_i=B07BRR59DT&pd_rd_r=768617e6-65e5-499f-bd98-b4952b98763e&pd_rd_w=0PoEQ&pd_rd_wg=ElpVj&pf_rd_p=08abe11d-4ee5-46ca-8471-7bf18c53fc91&pf_rd_r=5ZF6D4K9PY4H205YRBCH&psc=1&refRID=5ZF6D4K9PY4H205YRBCH"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
# response = get(URL,headers=headers)
# soup = BeautifulSoup(response.content, "lxml")
#
# # try:
# c = soup.find(id='priceblock_ourprice')
#
# print(c)
import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("db.sqlite3")
df = pd.read_sql_query('''SELECT name FROM sqlite_master WHERE type='table';''', con)
df1=pd.read_sql_query("SELECT * FROM core_order ", con)

# Verify that result of SQL query is stored in the dataframe
print(df1)