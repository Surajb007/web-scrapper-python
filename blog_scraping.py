# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

pages = soup.select(".pagination")[0].select('.page')
url_lists = ['/blog']
for page in pages:
    a_tag = page.find("a")
    url_lists.append(a_tag["href"]) if a_tag != None else print("")

with open("blog_data.csv", "a") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])
    for url in url_lists:
        response = requests.get(f"https://www.rithmschool.com{url}")
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article")
        # print(articles)
        for article in articles:
            a_tag = article.find("a")
            title = a_tag.get_text()
            # url = a_tag.attrs['href']
            url = a_tag['href']
            date = article.find("time")["datetime"]
            csv_writer.writerow([title, url, date])