from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(
    name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

highest_upvote_index = article_upvotes.index(max(article_upvotes))

print("Most popular news is: ")
print(article_texts[highest_upvote_index])
print(article_links[highest_upvote_index])
print(article_upvotes[highest_upvote_index])


# # import lxml
# # "day25\\50_states.csv"
# with open("day45 Web Scraping\\website.html", encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.find_all(name="a")

# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")

# print(heading)

# section_heading = soup.find(name="h3", class_="heading")

# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)
