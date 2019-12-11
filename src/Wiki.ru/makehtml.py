# -*- coding: UTF-8 -*-
import json
import urllib

f = open('out\\links.json')
links = json.load(f)
f.close()

newlist = sorted(links, key=lambda k: k['id_str'])

f = open('out\\test.html', 'wb')
f.write("<html><body><table>\n")
f.write("<tr><th>id_str</th><th>nation</th><th>type</th><th>tier</th><th>ship_id</th><th>ship_name</th><th>url</th><th>status</th></tr>\n")
for ship in newlist:
    f.write('<tr {}><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td nowrap>{}</td><td nowrap><a href="{}">{}</a></td><td>{}</td></tr>'.format(
        'style="background-color:yellow"' if ship['status_code'] != 200 else '',
        ship['id_str'],
        ship['nation'],
        ship['type'],
        ship['tier'],
        ship['ship_id'],
        ship['ship_name'].encode('utf8'),
        ship['url'],
        urllib.unquote(ship['url'].encode('utf8')),
        ship['status_code']
    ))
    f.write("\n")
f.write("</table></body></html>\n")
f.close()
