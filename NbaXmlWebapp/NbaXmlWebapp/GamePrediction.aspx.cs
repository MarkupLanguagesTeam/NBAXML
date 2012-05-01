using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.IO;
using System.Xml;
using System.Text;
using System.Xml.Linq;

namespace NbaXmlWebapp
{
    public partial class GamePrediction : System.Web.UI.Page
    {
        private const int MaxGameTime = 48 * 5;

        private List<string> files;
        private List<string> Files
        {
            get
            {
                if (files == null)
                {
                    var fullLengthfiles = Directory.GetFiles(Server.MapPath("~/Xml/")).ToList();
                    files = fullLengthfiles.Select(c => c.Substring(c.LastIndexOf('\\') + 1)).ToList();
                    files.Remove("nbaxml.xsl");
                }

                return files;
            }
        }

        private List<string> teams;
        private List<string> Teams
        {
            get
            {
                if (teams == null)
                {
                    teams = new List<string>();
                   
                    foreach (var file in Files)
                    {                        
                        if(file.Contains(".xsl"))
                            continue;

                        var team1 = file.Substring(8, 3);
                        var team2 = file.Substring(11, 3);
                        if (!teams.Contains(team1))
                            teams.Add(team1);

                        if (!teams.Contains(team2))
                            teams.Add(team2);
                    }
                }

                return teams;
            }
        }
        
        protected void Page_Load(object sender, EventArgs e)
        {
            btnGo.Click += new EventHandler(btnGo_Click);
            if (!Page.IsPostBack)
                BindData();
        }

        void btnGo_Click(object sender, EventArgs e)
        {
            var team1 = "CHI";
            var team2 = teamsDdl.SelectedValue;

            var team1Scores = new int[100];
            var team2Scores = new int[200];

            var team1Wins = 0;
            var team1total = 0;
            var team2total = 0;

            for(int i = 0; i < 100; i++)
            {
                var team1score = GetGamePoints(team1);
                var team2score = GetGamePoints(team2);
                
                team1Scores[i] = team1score;
                team2Scores[i] = team2score;
                
                team1total += team1score;
                team2total += team2score;
                
                if(team1Scores[i] > team2Scores[i])
                    team1Wins++;
            }

            resultsPh.Visible = true;
            if(team1Wins > 50)
            {
                winnerLbl.Text = team1;
                confLbl.Text = team1Wins + " %";
            }
            else if(team1Wins == 50)
            {
                winnerLbl.Text = "TIE!";
                confLbl.Text = "50 %";
            }
            else
            {
                winnerLbl.Text = team2;
                confLbl.Text = (100 - team1Wins) + " %";
            }

            team1AvgLbl.Text = ((decimal)team1total / ((decimal)100.0)).ToString("#.##");
            team2AvgLbl.Text = ((decimal)team2total / ((decimal)100.0)).ToString("#.##");
        }

        private int GetGamePoints(string teamName)
        {
            decimal currentMinutes = 0;

            int points = 0;

            var allGames = Files.Where(c => c.Substring(8, 3) == teamName || c.Substring(11, 3) == teamName);

            string startsGameFileName;

            var startersGame = GetRandomGame(allGames, out startsGameFileName);

            var teamNode = GetTeamDataFromGame(startersGame, teamName, startsGameFileName);

            foreach (var playerNode in teamNode.Elements("PLAYER"))
            {
                decimal minutes = 0;
                XElement currentPlayerGame = null;
                while (currentMinutes + minutes > MaxGameTime + 2 || currentPlayerGame == null)
                {
                    var playerName = playerNode.Element("NAME").Value;
                    string fileName;
                    while (currentPlayerGame == null)
                    {
                        currentPlayerGame = GetPlayerDataForRandomGame(playerName, teamName, allGames);
                    }

                    minutes = Convert.ToDecimal(currentPlayerGame.Element("MIN").Value);
                }

                points += Convert.ToInt32(currentPlayerGame.Element("PTS").Value);
            }

            return points;
        }

        private XElement GetPlayerDataForRandomGame(string playerName, string teamName, IEnumerable<string> allGames)
        {
            string fileName;
            var newGame = GetRandomGame(allGames, out fileName);
            var data = GetTeamDataFromGame(newGame, teamName, fileName);
            

            return data.Elements("PLAYER").FirstOrDefault(c => c.Element("NAME").Value == playerName);
        }

        private XElement GetTeamDataFromGame(XDocument gameData, string teamName, string fileName)
        {
            var teamIsHome = fileName.Substring(8, 3) != teamName;

            if (teamIsHome)
                return gameData.Descendants("TEAM").First(c => !c.Value.Contains("VISITOR"));

            return gameData.Descendants("TEAM").First(c => c.Value.Contains("VISITOR"));
        }


        private XDocument GetRandomGame(IEnumerable<string> allGames, out string fileName)
        {
            var rand = new Random();

            fileName = allGames.ElementAt( rand.Next(allGames.Count()));

            XDocument returnVal = null; ;

            while (returnVal == null)
            {
                try
                {
                    returnVal = LoadXmlFromFileName(fileName);
                }
                catch
                {
                    fileName = allGames.ElementAt(rand.Next(allGames.Count()));
                    returnVal = null;
                }
            }

            return returnVal;
        }

        private XDocument LoadXmlFromFileName(string fileName)
        {
            var xdoc = new XDocument();
            MemoryStream stream = new MemoryStream(ASCIIEncoding.Default.GetBytes(File.ReadAllText(Server.MapPath("~/Xml/" + fileName))));            
            return XDocument.Load(stream);
        }

        private void BindData()
        {
            Teams.Sort((x, y) => x.CompareTo(y));
            Teams.Remove("CHI");
            foreach (var team in teams)
            {
                teamsDdl.Items.Add(new ListItem(team, team));
            }
        }
    }
}