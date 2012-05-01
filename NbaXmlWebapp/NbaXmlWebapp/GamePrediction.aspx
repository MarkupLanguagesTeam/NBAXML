<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true"
    CodeBehind="GamePrediction.aspx.cs" Inherits="NbaXmlWebapp.GamePrediction" %>

<asp:Content ID="Content1" ContentPlaceHolderID="HeadContent" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
    <h3>
        Predict a Game Winner</h3>
    CHI vs
    <asp:DropDownList ID="teamsDdl" runat="server">
    </asp:DropDownList>
    <br />
    <br />
    <asp:Button ID="btnGo" runat="server" Text="Predict Winner" /><br />
    <asp:PlaceHolder ID="resultsPh" runat="server" Visible="false"><strong>Winner:&nbsp;</strong><asp:Label
        ID="winnerLbl" runat="server" Font-Bold="true"></asp:Label><br />
        <strong>Confidence:&nbsp;</strong><asp:Label ID="confLbl" runat="server"></asp:Label><br />
        <strong>CHI Avg Score:&nbsp;</strong><asp:Label ID="team1AvgLbl" runat="server"></asp:Label><br />
        <strong><%= teamsDdl.SelectedValue %> Avg Score:&nbsp;</strong> <asp:Label ID="team2AvgLbl" runat="server"></asp:Label>
    </asp:PlaceHolder>
    <br />
    <br />
    <a href="Default.aspx">Back To Games</a>
</asp:Content>
