import linecache
import re
textFiles = ['20101030DETCHI.txt', '20101101PORCHI.txt', '20101105CHIBOS.txt', '20101108DENCHI.txt', '20101111GSWCHI.txt', '20101113WASCHI.txt', '20101119CHIDAL.txt', '20101123CHILAL.txt', '20101126CHIDEN.txt', '20101127CHISAC.txt', '20101201ORLCHI.txt', '20101203CHIBOS.txt', '20101204HOUCHI.txt', '20101206OKCCHI.txt', '20101208CHICLE.txt', '20101210LALCHI.txt', '20101211MINCHI.txt', '20101213INDCHI.txt', '20101215CHITOR.txt', '20101221PHICHI.txt', '20101222CHIWAS.txt',  '20101226CHIDET.txt', '20110104TORCHI.txt', '20110105CHINJN.txt', '20110107CHIPHI.txt', '20110108BOSCHI.txt', '20110110DETCHI.txt', '20110112CHICHA.txt', '20110114CHIIND.txt', '20110117CHIMEM.txt', '20110118CHACHI.txt', '20110120DALCHI.txt', '20110122CLECHI.txt', '20110124MILCHI.txt', '20110128ORLCHI.txt', '20110205CHIGSW.txt',  '20110209CHIUTA.txt',  '20110217SASCHI.txt', '20110223CHITOR.txt', '20110228CHIWAS.txt', '20110302CHIATL.txt', '20110304CHIORL.txt', '20110306CHIMIA.txt', '20110309CHICHA.txt', '20110311ATLCHI.txt', '20110312UTACHI.txt', '20110315WASCHI.txt', '20110317CHINJN.txt', '20110318CHIIND.txt', '20110322CHIATL.txt', '20110326CHIMIL.txt', '20110328PHICHI.txt', '20110330CHIMIN.txt', '20110401CHIDET.txt', '20110402TORCHI.txt', '20110405PHXCHI.txt', '20110407BOSCHI.txt', '20110408CHICLE.txt', '20110410CHIORL.txt', '20110412CHINYK.txt', '20110418INDCHI.txt', '20110421CHIIND.txt', '20110423CHIIND.txt', '20110426INDCHI.txt', '20110504ATLCHI.txt', '20110510ATLCHI.txt', '20110512CHIATL.txt']
for files in textFiles:
    textFile = 'C:\\Users\\Eric\\Documents\\PDF2Text Output\\'+files
    filename = "C:\\Users\\Eric\\Documents\\Loyola Grad School\\Spring 2012\\Markup Languages\\nbaxml\\"+files[0:14]+".xml"
    print filename
    file = open(filename, "w")
    file.write("<?xml version='1.0' encoding='us-ascii'?>\n<?xml-stylesheet type='text/xsl' href='nbaxml.xsl'?>\n <GAME>\n")

    team1 = linecache.getline(textFile, 7)
    file.write("\t<TEAM><TEAMNAME>"+team1+"</TEAMNAME>\n")

    team1Lineup = []
    for player in range (9, 21):
        playerData = linecache.getline(textFile, player)
        ID = re.findall(r'\w+', playerData)
        if len(ID)<21 and len(ID)>7:
            ID.insert(3, 'NS')
        elif len(ID) == 21:
            ID[3]='S'
        else:
            ID[3] = 'NS'
            for stats in range (4, 7):
                ID[stats] = '0'
            for stats in range (7, 21):
                ID.append('0')
        file.write("\t\t<PLAYER><NAME>"+ID[1]+","+ID[2]+"</NAME>\n \t\t\t<MIN>"+ID[4]+"."+ID[5]+"</MIN>\n\t\t\t<PTS>"+ID[20]+"</PTS>\n\t\t\t<REB>"+ID[14]+"</REB>\n\t\t\t<STL>"+ID[17]+"</STL>\n\t\t\t<BLK>"+ID[19]+"</BLK>\n\t\t</PLAYER>\n")
    file.write("\t\t</TEAM>\n")
            
    team2 = linecache.getline(textFile, 24)
    file.write("\t<TEAM><TEAMNAME>"+team2+"</TEAMNAME>\n")

    team2Lineup = []
    for player in range (26, 37):
        playerData = linecache.getline(textFile, player)
        ID = re.findall(r'\w+', playerData)
        if len(ID)<21 and len(ID)>7:
            ID.insert(3, 'NS')
        elif len(ID) == 21:
            ID[3]='S'
        else:
            ID[3] = 'NS'
            for stats in range (4, 7):
                ID[stats] = '0'
            for stats in range (7, 21):
                ID.append('0')
        file.write("\t\t<PLAYER><NAME>"+ID[1]+","+ID[2]+"</NAME>\n \t\t\t<MIN>"+ID[4]+"."+ID[5]+"</MIN>\n\t\t\t<PTS>"+ID[20]+"</PTS>\n\t\t\t<REB>"+ID[14]+"</REB>\n\t\t\t<STL>"+ID[17]+"</STL>\n\t\t\t<BLK>"+ID[19]+"</BLK>\n\t\t</PLAYER>")
    file.write("\t\t</TEAM>\n</GAME>")
    file.close()






