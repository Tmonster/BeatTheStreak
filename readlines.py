
import urllib2
import csv
import sys
import datetime
def main():
	print recommendedPlayers(getlines(sys.argv[1]))

def getlines(i):
	players = []
	d = datetime.date.today()
	print d.month
	print d.day
	url = 'http://dailybaseballdata.com/cgi-bin/dailyhit.pl?date='+str(d.month)+str(d.day)+'&xyear=0&pa=0&showdfs=&sort=ops&r40=0&scsv=2&nohead=1'
	response = urllib2.urlopen(url)
	stats = csv.reader(response)
	j = 0
	isheaders = True
	for row in stats:
		#signals end of stats in csv
		if '</pre>' in row:
			isheaders = True
		if not isheaders:
			#print row
			players.append(row)
			j = j + 1
			if j >= i:
				break
		#signals start of stats in csv
		if 'MLB_ID' in row:
			isheaders = False
		if j >= i:
			break
	return players

def recommendedPlayers(players):
	recommendations = []
	for player in players:
		name = player[3]
		team = player[4]
		if player[5] == 'H':
			home = True
		else:
			home = False
		#Bats right or left handed
		bats = player[6] #Switch 'S', Right 'R', Left 'L'
		active = player[7]
		numberOfPitches = int(player[16])
		plateAppearances = float(player[17])
		atBats = int(player[18])
		hits = float(player[19])
		RBI = int(player[24])
		strikeOuts = int(player[27])
		average = float(player[31])
		opposingPitcher = player[39]
		pitcherThrowingArm = player[41]
		stadium = player[43]
		pitchingTeam = player[40]

		chooseAverage = 0.300
		chooseNumberOfPitches = 30
		choosePlateApearances = 5
		chooseHits = 4
		choosestrikeOuts = 3

		if average > chooseAverage:
			if numberOfPitches > chooseNumberOfPitches:
				if plateAppearances > choosePlateApearances:
					if bats != pitcherThrowingArm:
						if float(hits/plateAppearances) > 0.4:
							if strikeOuts <= choosestrikeOuts:
								#Add player, and team against 
								recommendations.append([name,team, "Against " + pitchingTeam])
	return recommendations



























