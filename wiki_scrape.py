from bs4 import BeautifulSoup
import requests
import pandas as p
import json


# page = requests.get("https://en.wikipedia.org/wiki/The_Eras_Tour")

# soup = BeautifulSoup(page.content, 'html.parser')

# list(soup.children)


# print(soup.findAll('t'))


# print('\n\n')


# print(soup.find_all('td')[12].get_text())
def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file

        data (dict)/(list): the data to be encoded as JSON and written to
        the file

        encoding (str): name of encoding used to encode the file

        indent (int): number of "pretty printed" indention spaces applied to
        encoded JSON

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)

wikiurl = "https://en.wikipedia.org/wiki/The_Eras_Tour"

table_class = "wikitable plainrowheaders"
response = requests.get(wikiurl)
# print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
erastourtable = soup.findAll('table', {'class': "wikitable plainrowheaders"})


df = p.read_html(str(erastourtable))[1]
print(df)



df = p.DataFrame(df)


data = df.drop(['Country', 'Attendance', 'Revenue'], axis=1)

print(data)

erastourdict = {}

for i, row in data.iterrows():
    date = row['Date']
    city = row['City']
    venue = row['Venue']
    openers = row['Opening acts']
    erastourdict[date] = {'city':city, 'venue':venue, 'openers':[openers]}


# for date in erastourdict:
#     openers = erastourdict[date]["openers"][0]
#     openers_list = []
#     for opener in openers:
#         for opener_name in opener.split():
#             openers_list.append(opener_name)
#             openers = openers_list

openers_list = erastourdict['March 17, 2023']['openers'][0].split()
erastourdict['March 17, 2023']["openers"] = openers_list

openers_list = erastourdict['March 18, 2023']['openers'][0].split()
erastourdict['March 18, 2023']["openers"] = openers_list

openers_list = erastourdict['March 24, 2023']['openers'][0].split()
erastourdict['March 24, 2023']["openers"] = openers_list

openers_list = erastourdict['March 25, 2023']['openers'][0].split()
erastourdict['March 25, 2023']["openers"] = openers_list

openers_list = erastourdict['March 31, 2023']['openers'][0].split()
erastourdict['March 31, 2023']["openers"] = openers_list

openers_list = erastourdict['April 1, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['April 1, 2023']["openers"] = openers_list

openers_list = erastourdict['April 2, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['April 2, 2023']["openers"] = openers_list

openers_list = erastourdict['April 13, 2023']['openers'][0].split()
erastourdict['April 13, 2023']["openers"] = openers_list

openers_list = erastourdict['April 14, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['April 14, 2023']["openers"] = openers_list

openers_list = erastourdict['April 15, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['April 15, 2023']["openers"] = openers_list

openers_list = erastourdict['April 21, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['April 21, 2023']["openers"] = openers_list

openers_list = erastourdict['April 22, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['April 22, 2023']["openers"] = openers_list

openers_list = erastourdict['April 23, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['April 23, 2023']["openers"] = openers_list

openers_list = erastourdict['April 28, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['April 28, 2023']["openers"] = openers_list

openers_list = erastourdict['April 29, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['April 29, 2023']["openers"] = openers_list

openers_list = erastourdict['April 30, 2023']['openers'][0].split()
erastourdict['April 30, 2023']["openers"] = openers_list

openers_list = erastourdict['May 5, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1]
openers_list.pop(1)
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['May 5, 2023']["openers"] = openers_list

openers_list = erastourdict['May 6, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1]
openers_list.pop(1)
erastourdict['May 6, 2023']["openers"] = openers_list

openers_list = erastourdict['May 7, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1]
openers_list.pop(1)
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['May 7, 2023']["openers"] = openers_list

openers_list = erastourdict['May 12, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1]
openers_list.pop(1)
erastourdict['May 12, 2023']["openers"] = openers_list

openers_list = erastourdict['May 13, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1]
openers_list.pop(1)
erastourdict['May 13, 2023']["openers"] = openers_list

openers_list = erastourdict['May 14, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1]
openers_list.pop(1)
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['May 14, 2023']["openers"] = openers_list

openers_list = erastourdict['May 19, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1]
openers_list.pop(1)
erastourdict['May 19, 2023']["openers"] = openers_list

openers_list = erastourdict['May 20, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1]
openers_list.pop(1)
erastourdict['May 20, 2023']["openers"] = openers_list

openers_list = erastourdict['May 21, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1]
openers_list.pop(1)
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['May 21, 2023']["openers"] = openers_list

openers_list = erastourdict['May 26, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1]
openers_list.pop(1)
erastourdict['May 26, 2023']["openers"] = openers_list

openers_list = erastourdict['May 27, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1]
openers_list.pop(1)
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['May 27, 2023']["openers"] = openers_list

openers_list = erastourdict['May 28, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1]
openers_list.pop(1)
erastourdict['May 28, 2023']["openers"] = openers_list

openers_list = erastourdict['June 2, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1] + " " + openers_list[2]
openers_list.pop(1)
openers_list.pop(1)
erastourdict['June 2, 2023']["openers"] = openers_list

openers_list = erastourdict['June 3, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1] + " " + openers_list[2]
openers_list.pop(1)
openers_list.pop(1)
erastourdict['June 3, 2023']["openers"] = openers_list

openers_list = erastourdict['June 4, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[1]
openers_list.pop(2)
erastourdict['June 4, 2023']["openers"] = openers_list

openers_list = erastourdict['June 9, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1] + " " + openers_list[2]
openers_list.pop(1)
openers_list.pop(1)
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['June 9, 2023']["openers"] = openers_list

openers_list = erastourdict['June 10, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1] + " " + openers_list[2]
openers_list.pop(1)
openers_list.pop(1)
erastourdict['June 10, 2023']["openers"] = openers_list

openers_list = erastourdict['June 16, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1] + " " + openers_list[2]
openers_list.pop(1)
openers_list.pop(1)
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['June 16, 2023']["openers"] = openers_list

openers_list = erastourdict['June 17, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1] + " " + openers_list[2]
openers_list.pop(1)
openers_list.pop(1)
erastourdict['June 17, 2023']["openers"] = openers_list

openers_list = erastourdict['June 23, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1] + " " + openers_list[2]
openers_list.pop(1)
openers_list.pop(1)
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['June 23, 2023']["openers"] = openers_list

openers_list = erastourdict['June 24, 2023']['openers'][0].split()
openers_list[0] = openers_list[0] + " " + openers_list[1] + " " + openers_list[2]
openers_list.pop(1)
openers_list.pop(1)
erastourdict['June 24, 2023']["openers"] = openers_list

openers_list = erastourdict['June 30, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['June 30, 2023']["openers"] = openers_list

openers_list = erastourdict['July 1, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['July 1, 2023']["openers"] = openers_list

openers_list = erastourdict['July 7, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['July 7, 2023']["openers"] = openers_list

openers_list = erastourdict['July 8, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['July 8, 2023']["openers"] = openers_list

openers_list = erastourdict['July 14, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['July 14, 2023']["openers"] = openers_list

openers_list = erastourdict['July 15, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['July 15, 2023']["openers"] = openers_list

openers_list = erastourdict['July 22, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['July 22, 2023']["openers"] = openers_list

openers_list = erastourdict['July 23, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['July 23, 2023']["openers"] = openers_list

openers_list = erastourdict['July 28, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['July 28, 2023']["openers"] = openers_list

openers_list = erastourdict['July 29, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['July 29, 2023']["openers"] = openers_list

openers_list = erastourdict['August 3, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['August 3, 2023']["openers"] = openers_list

openers_list = erastourdict['August 4, 2023']['openers'][0].split()
erastourdict['August 4, 2023']["openers"] = openers_list

openers_list = erastourdict['August 5, 2023']['openers'][0].split()
erastourdict['August 5, 2023']["openers"] = openers_list

openers_list = erastourdict['August 8, 2023']['openers'][0].split()
openers_list[1] = openers_list[1] + " " + openers_list[2]
openers_list.pop(2)
erastourdict['August 8, 2023']["openers"] = openers_list

openers_list = erastourdict['August 9, 2023']['openers'][0].split()
erastourdict['August 9, 2023']["openers"] = openers_list

del erastourdict["Total"]


write_json('ErasTourDict.json', erastourdict)
