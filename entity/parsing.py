import requests
from bs4 import BeautifulSoup
from entity.olympiad import Olympiad

olympiads = ()
def get_name(olympiad_soup):
    try:
        return olympiad_soup.find("h1").text
    except AttributeError:
        return None

def get_dates(olympiad_soup):
    pass

def get_classes(olympiad_soup):
    try:
        return (olympiad_soup.find("span", class_="classes_types_a").text)
    except AttributeError:
        return None

def get_subjects(olympiad_soup):
    try:
        subjects = []
        for span in olympiad_soup.find_all("span", class_="subject_tag"):
            if span.parent.get("class") == ["subject_tags_full"]:
                subject = ""
                for i in span.text:
                    for j in i:
                        if(j not in "\xa0"): subject += j
                        else: subject += " "
                subject = subject[1:len(subject)]
                subjects.append(subject)
        return subjects
    except AttributeError:
        return None

def get_level(olympiad_soup):
    content = olympiad_soup.find_all("div", class_="right")
    levels = []
    for tag in content:
        tag.find_all("div", id="features", class_="block_with_margin_bottom")
        for div in tag:
            try:
                for span in div.find_all("span"):
                    if("уровень" in span.parent.text):
                        words = span.parent.text.split()
                        for i in range(len(words)):
                            if("уровень" in words[i]):
                                for j in range(i + 1, len(words)):
                                    for k in words[j]:
                                        if k in "123" and k not in levels:
                                            levels.append(k)
                                        elif k == "П":
                                            return levels
            except AttributeError:
                pass

def get_ref_to_full_information(olympiad_soup):
    pass

def get_ref_to_registration(olympiad_soup):
    pass

url = "https://olimpiada.ru/article/1045"
html = requests.get(url)
soup = BeautifulSoup(html.text)
# subject_names = [p.find("strong") for p in soup.select("div > p")]
# for i in range(len(subject_names) - 1, -1, -1):
#     if(subject_names[i] == None):
#         del subject_names[i]
#     else:
#         subject_names[i] = subject_names[i].text
# print(subject_names)
olympiads_urls = [p.find("a", class_="slim_dec") for p in soup.select("td > p")]
for i in range(len(olympiads_urls) - 1, -1, -1):
    if olympiads_urls[i] == None :
        del olympiads_urls[i]
    else:
        olympiads_urls[i] = "https://olimpiada.ru" + olympiads_urls[i].get("href")
for olympiad_url in olympiads_urls:
    olympiad_html = requests.get(olympiad_url)
    olympiad_soup = BeautifulSoup(olympiad_html.text)
    levels = get_level(olympiad_soup)
    print("\n", get_name(olympiad_soup),
          "\n Subjects : ", get_subjects(olympiad_soup),
          "\n Classes : ", get_classes(olympiad_soup),
          "\n Level : ", get_level(olympiad_soup),
          "\n Full information : ", olympiad_url, "\n")

print(olympiad_soup)
print(olympiads)

