def getCreepDifferential(node):
    differentialArray = node['csDiffPerMinDeltas'].values()
    return reduce(lambda x, y: x + y, differentialArray) / len(differentialArray)

def getKills(node):
    return node['kills']

def getDeaths(node):
    return node['deaths']

def getAssists(node):
    return node['assists']

def getDoubleKills(node):
    return node['doubleKills']

def getTripleKills(node):
    return node['tripleKills']

def getQuadraKills(node):
    return node['quadraKills']

def getPentaKills(node):
    return node['pentaKills']

def getTotalDamageToChamps(node):
    return node['totalDamageDealtToChampions']

def getTotalDamageTaken(node):
    return node['totalDamageTaken']

def getLargestKillingSpree(node):
    return node['largestKillingSpree']

def getLargestMultiKill(node):
    return node['largestMultiKill']

def getMinionsKilled(node):
    return node['minionsKilled']

def getWardsPlaced(node):
    return node['wardsPlaced']

def getFirstBlood(node):
    return node['firstBloodKill']

def getVictorious(node):
    return node['winner']
