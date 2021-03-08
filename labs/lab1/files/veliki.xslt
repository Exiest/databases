<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml"
                indent="yes"/>

    <xsl:template match="/">
        <html>
            <head>
                <meta charset="utf-8"/>
                <meta name="viewport" content="width=device-width, initial-scale=1"/>
                <title>Veliki</title>
            </head>
            <body>
                <div>
                    <div>
                        <h1>Veliki</h1>
                    </div>
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Price</th>
                                <th>Img</th>
                            </tr>
                        </thead>
                        <tbody>
                            <xsl:apply-templates/>
                        </tbody>
                    </table>
                </div>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="item">
        <tr>
            <td>
                <xsl:value-of select="name"/>
                <br/>
            </td>
            <td>
                <xsl:value-of select="price"/>
            </td>
            <td>
                <xsl:element name="img">
                    <xsl:attribute name="src">
                        <xsl:value-of select="img"/>
                    </xsl:attribute>
                </xsl:element>
            </td>
        </tr>
    </xsl:template>

</xsl:stylesheet>