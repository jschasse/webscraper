from bs4 import BeautifulSoup
import requests
from constants import *
import csv
import os

def parse_table_to_csv(url, output_dir="/home/jschasse/workspace/github.com/jschasse/webscraper/stat_tables", file_prefix="table"):
    
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        os.makedirs(output_dir, exist_ok=True)
        
        soup = BeautifulSoup(response.text, "lxml")
        tables = soup.find_all("table")
        
        for i, table in enumerate(tables):
            rows = []
            for tr in table.find_all("tr"):
                row = []
                for td in tr.find_all(["td", "th"]):
                    row.append(td.get_text(strip=True))
                if row:
                    rows.append(row)
        
            if rows:
                filename = f"{file_prefix}_{i + 1}.csv"
                filepath = os.path.join(output_dir, filename)
            
                with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(rows)
                
                print(f"saved table {i + 1} to {filepath} ({len(rows)} rows)")
            
    else:
        print(response.status_code)

