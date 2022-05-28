import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

res = urlopen("https://bit.ly/3jpMFRW")
soup = BeautifulSoup(res, "html.parser")
table = soup.findAll("table")[0]
rows = table.findAll("tr")

with open("Dataset.csv", 'w', newline="") as f:
    write = csv.writer(f)
    for i in rows:
        row = []
        for cell in i.findAll(["td", "th"]):
            row.append(cell.get_text())
        write.writerow(row)

with open('Dataset.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)