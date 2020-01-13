import requests
from bs4 import BeautifulSoup

class SightseeingParser:
    def __init__(self, town):
        self.town = town

    def get_sightseeing_info(self):
        sights = []
        names = []
        reitings = []
        diskriptions = []
        response = requests.get("https://www.google.com/travel/things-to-do/see-all?g2lb=2502405%2C2502548%2C4208993%2C4254308%2C4258168%2C4260007%2C4270442%2C4274032%2C4285990%2C4289525%2C4291318%2C4301054%2C4305595%2C4308216%2C4308227%2C4313006%2C4314846%2C4315873%2C4317816%2C4317915%2C4324289%2C4324292%2C4326405%2C4328159%2C4329288%2C4329496%2C4333189%2C4338438%2C4270859%2C4284970%2C4291517%2C4292955%2C4316256%2C4333108&hl=ru&gl=ru&un=1&otf=1&dest_mid=%2Fm%2F06pr6&dest_src=ts&dest_state_type=sattd&sa=X&cshid=1576011517826791#ttdm=59.883733_30.133536_10&ttdmf=%252Fg%252F120l360g")
        content = response.content.decode("utf-8", errors='ignore')
        soup = BeautifulSoup(content, 'lxml')
        soup.html
        blocks = soup.select('.Ld2paf')
        for inf in blocks:
            now_dict = {"Name": "", "Reiting": "", "Diskription": ""}
            name_div = inf.select('.GwjAi')
            for more_inf in name_div:
                for more_inf_name in more_inf.select('.rbj0Ud'):
                    for name in more_inf_name.select('.skFvHc'):
                        now_dict["Name"] = name.text
            reiting_div = inf.select('.tP34jb ')
            for reit in reiting_div:
                span = reit.find(("span", {"class":"oz2bpb bVUOpb"}))
                now_dict["Reiting"] = span.get('aria-label')

            diskription_div = inf.select('.nFoFM')
            for diskription in diskription_div:
                now_dict["Diskription"] = diskription.text
            sights.append(now_dict)
            now_dict = {"Name": "", "Reiting": "", "Diskription": ""}
        #for sight in range(len(names)):
         #   sights.append({"Название": names[sight], "Оценка": reitings[sight], "Описание": diskriptions[sight]})
        return sights
