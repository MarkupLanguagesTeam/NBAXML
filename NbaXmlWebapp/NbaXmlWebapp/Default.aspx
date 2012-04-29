<%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.master" AutoEventWireup="true"
    CodeBehind="Default.aspx.cs" Inherits="NbaXmlWebapp._Default" %>

<asp:Content ID="HeaderContent" runat="server" ContentPlaceHolderID="HeadContent">
</asp:Content>
<asp:Content ID="BodyContent" runat="server" ContentPlaceHolderID="MainContent">
    <h3>
        Games</h3>
    <table style="width: 100%">
        <thead>
            <tr>
                <td>
                    <strong>Date</strong>
                </td>
                <td>
                    <strong>Team</strong>
                </td>
                <td>
                    <strong>VS.</strong>
                </td>
                <td><strong>View</strong></td>
            </tr>
        </thead>
    <asp:Repeater ID="gamesRpt" runat="server">
        <ItemTemplate>
            <tr>
                <td>
                    <%# ((DateTime)Eval("GameDate")).ToShortDateString() %>
                </td>
                <td>
                    <%# Eval("Team1") %>
                </td>
                <td>
                    <%# Eval("Team2") %>
                </td>
                <td><a href='/Details.aspx?g=<%# Eval("GameId")%>'>View Game Details</a></td>
            </tr>
        </ItemTemplate>
    </asp:Repeater>
    </table>
</asp:Content>
