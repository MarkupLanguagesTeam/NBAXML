import linecache
import re
textFiles = ['20101026MIABOS.txt', '20101027MIAPHI.txt', '20101031MIANJN.txt', '20101102MINMIA.txt', '20101106NJNMIA.txt', '20101109UTAMIA.txt', '20101117PHXMIA.txt', '20101120MIAMEM.txt', '20101122INDMIA.txt', '20101124MIAORL.txt', '20101126PHIMIA.txt', '20101127MIADAL.txt', '20101204ATLMIA.txt', '20101206MIAMIL.txt', '20101208MIAUTA.txt', '20101210MIAGSW.txt', '20101211MIASAC.txt', '20101217MIANYK.txt', '20101223MIAPHX.txt', '20101225MIALAL.txt', '20101229MIAHOU.txt', '20110101GSWMIA.txt', '20110103MIACHA.txt', '20110104MILMIA.txt', '20110107MIAMIL.txt', '20110109MIAPOR.txt', '20110112MIALAC.txt',  '20110115MIACHI.txt', '20110122TORMIA.txt', '20110130MIAOKC.txt', '20110131CLEMIA.txt', '20110203MIAORL.txt', '20110204MIACHA.txt', '20110208INDMIA.txt', '20110211MIADET.txt', '20110213MIABOS.txt', '20110215MIAIND.txt', '20110216MIATOR.txt', '20110224MIACHI.txt', '20110225WASMIA.txt', '20110303ORLMIA.txt', '20110304MIASAS.txt', '20110306CHIMIA.txt', '20110310LALMIA.txt', '20110312MEMMIA.txt', '20110314SASMIA.txt', '20110316OKCMIA.txt', '20110318MIAATL.txt', '20110319DENMIA.txt', '20110323MIADET.txt', '20110325PHIMIA.txt', '20110327HOUMIA.txt', '20110330MIAWAS.txt', '20110401MIAMIN.txt', '20110403MIANJN.txt', '20110410BOSMIA.txt', '20110411MIAATL.txt', '20110427PHIMIA.txt', '20110501BOSMIA.txt', '20110503BOSMIA.txt', '20110507MIABOS.txt', '20110509MIABOS.txt', '20110511BOSMIA.txt', '20110515MIACHI.txt', '20110518MIACHI.txt', '20110522CHIMIA.txt', '20110524CHIMIA.txt', '20110526MIACHI.txt', '20110605MIADAL.txt', '20110607MIADAL.txt', '20110609MIADAL.txt']
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






