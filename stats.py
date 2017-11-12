import requests, json, api, csv


with open('config.json', 'r') as f:
    config = json.load(f)
    APIURL = config['APIURL']
    APIKEY = config['APIKEY']
    summonerIds = config['summonerIds']
    matchIds = config['matchIds']
    playerIDList = config['playerIDList']

def createPersonalJSON(summonerName, timelineNode, statsNode):
    personalJSON = {
        "01 Summoner": str(summonerName),
        "02 Victorious": str(api.getVictorious(statsNode)),
        "03 Kills": str(api.getKills(statsNode)),
        "04 Deaths": str(api.getDeaths(statsNode)),
        "05 Assists": str(api.getAssists(statsNode)),
        "06 Creep Score": str(api.getMinionsKilled(statsNode)),
        "07 CS Diff": str(api.getCreepDifferential(timelineNode)),
        "08 Double": str(api.getDoubleKills(statsNode)),
        "09 Triple": str(api.getTripleKills(statsNode)),
        "10 Quadra": str(api.getQuadraKills(statsNode)),
        "11 Penta": str(api.getPentaKills(statsNode)),
        "12 Damage To Champs": str("{:,}".format(api.getTotalDamageToChamps(statsNode))),
        "13 Damage Taken": str("{:,}".format(api.getTotalDamageTaken(statsNode))),
        "14 Killing Spree": str(api.getLargestKillingSpree(statsNode)),
        "15 Multi Kill": str(api.getLargestMultiKill(statsNode)),
        "16 Wards Placed": str(api.getWardsPlaced(statsNode)),
        "17 First Blood": str(api.getFirstBlood(statsNode))}
    return personalJSON

def createCSV(jsonNode):
    f = csv.writer(open("test.csv", "wb+"))
    f.writerow(["Summoner", "Victorious", "Kills", "Deaths", "Assists",
                "Creep Score", "CS Diff", "Double", "Triple", "Quadra",
                "Penta", "Damage To Champs", "Damage Taken",
                "Killing Spree", "Multi Kill", "Wards Placed", "First Blood"])
    for personalStats in jsonNode:
        f.writerow([personalStats['01 Summoner'],
                    personalStats['02 Victorious'],
                    personalStats['03 Kills'],
                    personalStats['04 Deaths'],
                    personalStats['05 Assists'],
                    personalStats['06 Creep Score'],
                    personalStats['07 CS Diff'],
                    personalStats['08 Double'],
                    personalStats['09 Triple'],
                    personalStats['10 Quadra'],
                    personalStats['11 Penta'],
                    personalStats['12 Damage To Champs'],
                    personalStats['13 Damage Taken'],
                    personalStats['14 Killing Spree'],
                    personalStats['15 Multi Kill'],
                    personalStats['16 Wards Placed'],
                    personalStats['17 First Blood']
        ])

def main():
    gameNumber = 0
    setArray = []
    for id in matchIds:
        matchArray = []
        requestURL = APIURL + str(id) + '?api_key=' + APIKEY
        matchResponse =  requests.get(requestURL).json()
        playerNumber = 0
        for participant in matchResponse['participants']:
            personalJSON = createPersonalJSON(summonerIds[playerIDList[gameNumber][playerNumber]], participant['timeline'],participant['stats'])
            matchArray.append(personalJSON)
            playerNumber += 1
        setArray.append(json.dumps(matchArray, sort_keys=True))
        gameNumber += 1
    for match in setArray:
        variables = json.loads(match)
        createCSV(variables)

        

if __name__ == "__main__":
    main()
