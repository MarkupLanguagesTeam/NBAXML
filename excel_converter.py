import xlrd
import sgmllib
import urllib2
import unicodedata
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            print tag
        else:
            pass
    def handle_endtag(self, tag):
        if tag == 'table':
            print tag
        else:
            pass
    def handle_data(self, data):
        if data !='':
            print "ENCOUNTERED SOME DATA:", data
        else:
            pass
            
        
##--------------Opens Spreadsheet and Gathers Game Information----------------------------------------------
book = xlrd.open_workbook("C:\Users\Eric\Desktop\MarkupLanguagesTeam-NBAXML-c70d77d/20102011NBAFullSeasonBoxScoreStatsInExcel.xls")
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
    print appendURL

##--------------Opens Webpages------------------------------------------------------------------------------

##for games in newGameList:
gamePage = urllib2.urlopen('http://www.nba.com/games/20110526/MIACHI/gameinfo.html')
gameInfo = gamePage.read()
print gameInfo
parser = MyHTMLParser()
parser.feed(gameInfo)

    
    
    
   
   
