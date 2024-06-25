import time
import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

urls = []
titles = []
cnt = 1016
for i in range(20,71):
    driver.get("https://www.codechef.com/practice?page="+str(i)+"&limit=50&sort_by=difficulty_rating&sort_order=asc&search=&start_rating=0&end_rating=5000&topic=&tags=&group=all")
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    all_ques_div = soup.findAll("tr",{"class":"MuiTableRow-root"})

    all_ques=[]

    for ques in all_ques_div:
        question=ques.find("a",{"class":"PracticePage_m-link__xLfvv"})
        if(question==None):
            continue
        all_ques.append(question)




    for ques in all_ques:
        urls.append(ques['href'])
        titles.append(str(ques.text.encode("utf-8")))

# with open("cc_problem_urls_test.txt", "w+") as f:
#        f.write('\n'.join(urls))
#     # with open("cc_problem_urls.txt", "w+") as f:
#     #    f.write('\n'.join(urls))
#
#     # with open("cc_problem_titles.txt", "w+") as f:
#     #    f.write('\n'.join(titles))
# with open("cc_problem_titles_test.txt", "w+") as f:
#        f.write('\n'.join(titles))

for url in urls:

    driver.get(url)

    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    main_text = soup.find('div', {"id": "problem-statement"}).get_text()
    # main_text=problem_text.findAll('p').get_text()
    main_text = main_text.encode("utf-8")
    main_text = str(main_text)
    cnt+= 1
    with open("cc_problem" + str(cnt) + ".txt", "w+") as f:
        f.write(main_text)