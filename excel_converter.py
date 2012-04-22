import xlrd
import urllib2
import unicodedata
      
        
##--------------Opens Spreadsheet and Gathers Game Information----------------------------------------------
book = xlrd.open_workbook("C:\\Users\\Eric\\Documents\\Loyola Grad School\\Spring 2012\\Markup Languages\\nbaxml\\20102011NBAFullSeasonBoxScoreStatsInExcel.xls")
sheet = book.sheet_by_index(0)

gameList = []
newGameList = []
for rownum in range(2623):
    stringTeam = sheet.cell(rownum, 2).value
    if  stringTeam == "Chicago":
        if  rownum%2==0:
            link = sheet.hyperlink_map.get((rownum,40))
            url = "(No URL)" if link is None else link.url_or_path
            gameList.append(unicodedata.normalize('NFKD',url).encode('ascii','ignore'))
        else:
            link = sheet.hyperlink_map.get(((rownum+1),40))
            url = "(No URL)" if link is None else link.url_or_path
            gameList.append(unicodedata.normalize('NFKD',url).encode('ascii','ignore'))
    else:
        pass

for game in gameList:
    appendURL = game.rstrip('boxscore.html')+'gameinfo.html'
    newGameList.append(appendURL)
print newGameList

##--------------Opens Webpages and gets PDF's------------------------------------------------------------------------------
textList = []
for games in newGameList:
    print games
    gamePage = urllib2.urlopen(games)
    gameInfo = gamePage.read()
    gameInfo = gameInfo[2100:len(gameInfo)]
    PDFStr = "/data/html/nbacom/2010/gameinfo/"
    PDF_Link ="http://www.nba.com" + gameInfo[gameInfo.find(PDFStr, 60):gameInfo.find(PDFStr, 60)+60]
    openPDF = urllib2.urlopen(PDF_Link).read()
    PDF_name = games[25:33]+games[34:40]+".pdf"
    dirPath = "C:\\Users\\Eric\\Documents\\Loyola Grad School\\Spring 2012\\Markup Languages\\nbaxml\\pdfs\\"
    PDF = open(dirPath+PDF_name, 'wb')
    PDF.write(openPDF)
    PDF.close
    textList.append(games[25:33]+games[34:40]+".txt")
print textList
##--------------Run through Simpo PDF to Text------------------------------------------------------------------------------
##--------------Parse .txt and convert to XML------------------------------------------------------------------------------

    
