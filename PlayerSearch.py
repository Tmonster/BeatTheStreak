import readlines
import sys

def searchFor(player):
	players = readlines.getlines(500)
	Fname = str(sys.argv[1])
	MyPlayer = []
	fullName = player
	for player in players:
		if fullName == player[3]:
			MyPlayer.append(player[3])
			MyPlayer.append(player[4])
			MyPlayer.append(player[5])
			MyPlayer.append(player[6])
			MyPlayer.append(player[7])
			MyPlayer.append("NP " + player[16])
			MyPlayer.append("PA " + player[17])
			MyPlayer.append("AB " + player[18])
			MyPlayer.append("Hits " + player[19])
			MyPlayer.append("RBI " + player[24])
			MyPlayer.append("SO " + player[27])
			MyPlayer.append("AVG " + player[31])
			break
	print MyPlayer

searchFor("rgufid")