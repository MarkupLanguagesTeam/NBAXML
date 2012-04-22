<?xml version="1.0" encoding="us-ascii"?>
  <html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml">
  <body>
    <h2>GAME</h2>
	<xsl:for-each select="GAME/TEAM">
    <table border="1">
	  <tr> <xsl:value-of select="TEAMNAME" /></tr>
      <tr bgcolor="#9acd32">
        <th>PLAYER</th>
        <th>MIN</th>
		<th>PTS</th>
		<th>REB</th>
		<th>STL</th>
		<th>BLK</th>
      </tr>
	  <xsl:for-each select="PLAYER">
      <tr>
        <td><xsl:value-of select="NAME"/></td>
        <td><xsl:value-of select="MIN"/></td>
		<td><xsl:value-of select="PTS"/></td>
		<td><xsl:value-of select="REB"/></td>
		<td><xsl:value-of select="STL"/></td>
		<td><xsl:value-of select="BLK"/></td>
      </tr>
	  </xsl:for-each>
    </table>
	</xsl:for-each>
  </body>
 </html>