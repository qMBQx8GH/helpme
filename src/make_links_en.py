# -*- coding: UTF-8 -*-
import os
import gettext
import json
import re
import urllib

os.environ["LANGUAGE"] = 'en'
tr = gettext.translation('global', 'res\\texts')
links = []

with open('Wiki.en\\out\\links.json') as f:
    ships = json.load(f)
    for ship in ships:
        if ship["status_code"] == 200:
            links.append({
                "ship_id": ship["ship_id"],
                "url": ship["url"],
                "title": ship["title"],
                "ship_name":  ship["ship_name"],
            })

with open('db\\ship.json') as f:
    ships = json.load(f)
    for ship_id in ships:
        ship = ships[ship_id]
        ship_name = tr.gettext('IDS_' + ship['id_str'])
        search_query = "{} wows review".format(ship_name)
        url = "https://www.youtube.com/results?search_sort=video_date_uploaded&search_query={}".format(urllib.quote(search_query))
        links.append({
            "ship_id": ship_id,
            "url": url,
            "title": u"YouTube search",
        })

with open('..\\HelpMe\\en\\links.json', 'w') as outfile:
    json.dump(links, outfile, encoding='utf8', indent=2, sort_keys=True)