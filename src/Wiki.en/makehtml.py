# -*- coding: UTF-8 -*-
import json
import urllib

f = open('out\\links.json')
links = json.load(f)
f.close()

newlist = sorted(links, key=lambda k: k['id_str'])

f = open('out\\test.html', 'wb')
f.write("<html><body><table>\n")
f.write("<tr><th>id_str</th><th>nation</th><th>type</th><th>tier</th><th>ship_id</th><th>ship_name</th><th>url</th></tr>\n")
for ship in newlist:
    f.write('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td nowrap>' % (ship['id_str'], ship['nation'], ship['type'], ship['tier'], ship['ship_id']))
    f.write(ship['ship_name'].encode('utf8'))
    f.write('</td><td nowrap><a href="%s">' % ship['url'])
    url = urllib.unquote(ship['url'].encode('utf8'))
    f.write(url)
    f.write("</a></td></tr>\n")
f.write("</table></body></html>\n")
f.close()
