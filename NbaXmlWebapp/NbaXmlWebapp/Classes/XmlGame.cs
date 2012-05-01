using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Xml.Linq;

namespace NbaXmlWebapp.Classes
{
    public class XmlGame
    {
        public string HomeTeam { get; set; }
        public string AwayTeam { get; set; }
        public XDocument GameData { get; set; }
    }
}