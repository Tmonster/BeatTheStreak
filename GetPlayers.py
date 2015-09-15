import readlines
import sys
numPlayerstoGet = int(float(sys.argv[1]))
players = readlines.getlines(numPlayerstoGet)
print readlines.recommendedPlayers(players)

