import os
from bs4 import BeautifulSoup

def get_main_quests(file_name):
    curr_path = os.getcwd()
    file_path = os.path.join(curr_path, file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        contents = file.read()

    soup = BeautifulSoup(contents, "html.parser")

    text = soup.get_text()

    # note the quests that start in wizard city listed in the wiki are not counted 
    lines_with_numbers = [line[line.index(" ")+ 1: line.index("(")].strip().lower() for line in text.splitlines() if line.strip() and line[0].isdigit()]

    # print("Extracted Text:", lines_with_numbers)
    return lines_with_numbers

def get_all_quests(file_name):
    curr_path = os.getcwd()
    file_path = os.path.join(curr_path, file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        contents = file.read()

    soup = BeautifulSoup(contents, "html.parser")

    # start of area that lists all the quests
    h2_tag = soup.find("h2", string=lambda text: "Polaris Quests" in text)

    quest_container = h2_tag.find_next("div", class_="mw-category")

    
    quests = []
    for li in quest_container.find_all("li"):
        quest_name = li.get_text()
        quests.append(quest_name[quest_name.index(":") + 1:].lower())

    return quests




if __name__ == "__main__":
    main_quests = set(get_main_quests("polaris_main_quest_line.html"))
    all_quests = set(get_all_quests("polaris_quests.html"))


    difference = all_quests - main_quests
    intersection = all_quests & main_quests

    # not sure why but there are items listed in main quest that arent in all_quests
    # its not even the instance stuff either, some quests that are just like (talk) are in all quests while others are not
    # EX: the quest: ancient insights ( just a talk to ppl quest )
        # it is in the final bastion quest tree
        # not in the polaris quest wiki page

    # EX: the quest: saving the sky anchor ( also just in the talk to ppl quest )
        # exists in both the final bastion quest tree and in the wiki page

    alphabetical = sorted(list(difference))
    for i in alphabetical:
        print(i)
    


