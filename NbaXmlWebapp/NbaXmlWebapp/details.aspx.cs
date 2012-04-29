using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Xml;
using System.Xml.Xsl;
using System.Text;
using System.IO;
using System.Xml.XPath;

namespace NbaXmlWebapp
{
    public partial class details : System.Web.UI.Page
    {
        private string gameDetailsHtml;
        protected string GameDetailsHtml
        {
            get
            {
                if (string.IsNullOrEmpty(gameDetailsHtml))
                {
                    var fileName = Request.QueryString["g"] + ".xml";
                    var path = Server.MapPath("~/Xml/" + fileName);

                    var xsltPath = Server.MapPath( "~/Xml/nbaxml.xsl");

                    gameDetailsHtml = GetHtml(xsltPath, File.ReadAllText(path));
                }

                return gameDetailsHtml;
            }
        }

        

        protected void Page_Load(object sender, EventArgs e)
        {
            
                
            
        }

        public static string GetHtml(string xsltPath, string xml)
        {
            MemoryStream stream = new MemoryStream(ASCIIEncoding.Default.GetBytes(xml));
            XPathDocument document = new XPathDocument(stream);
            StringWriter writer = new StringWriter();
            XslCompiledTransform transform = new XslCompiledTransform();
            transform.Load(xsltPath);
            transform.Transform(document, null, writer);
            return writer.ToString();
        }
    }
}