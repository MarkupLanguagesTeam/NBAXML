using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.IO;

namespace NbaXmlWebapp
{
    public partial class _Default : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!Page.IsPostBack)
                BindData();
        }

        private void BindData()
        {
            var games = new List<Game>();
            var files = Directory.GetFiles(Server.MapPath("~/Xml/"));
            foreach (var file in files)
            {
                var gameId = file.Substring(file.LastIndexOf('\\') + 1).Replace(".xml", "");
                if (gameId.Contains("(") || gameId.EndsWith("xsl"))
                    continue;

                var year = int.Parse(gameId.Substring(0, 4));
                var month = int.Parse(gameId.Substring(4, 2));
                var day = int.Parse(gameId.Substring(6, 2));

                var team1 = gameId.Substring(8, 3);
                var team2 = gameId.Substring(11, 3);

                games.Add(new Game
                {
                    GameDate = new DateTime(year, month, day),
                    GameId = gameId,
                    Team1 = team1,
                    Team2 = team2

                });

                gamesRpt.DataSource = games;
                gamesRpt.DataBind();
            }
        }


        protected class Game
        {
            public string GameId { get; set; }
            public DateTime GameDate { get; set; }
            public string Team1 { get; set; }
            public string Team2 { get; set; }
        }

    }

    
}
