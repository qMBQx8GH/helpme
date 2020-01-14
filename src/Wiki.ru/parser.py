# -*- coding: UTF-8 -*-
import os
import json
import gettext
import urllib
import requests

os.environ["LANGUAGE"] = 'ru'
tr = gettext.translation('global', '..\\res\\texts')
nm = {
    'Zaō P': 'Zaō',
    'Николай I': 'Император Николай I',
    'Tachibana L': 'Tachibana Lima',
    'Дм. Донской': 'Дмитрий Донской',
    'Hipper': 'Admiral Hipper',
    'Arkansas B': 'Arkansas Beta',
    'Диана L': 'Диана Lima',
    'Marblehead L': 'Marblehead Lima',
    'F. der Große': 'Friedrich der Große',
    'Abruzzi': 'Duca degli Abruzzi',
    'Макаров': 'Адмирал Макаров',
    'S. Carolina': 'South Carolina',
    'Сов. Союз': 'Советский Союз',
    'HSF Graf Spee': 'Admiral Graf Spee',
    'Graf Spee': 'Admiral Graf Spee',
    'N. Carolina': 'North Carolina',
    'G. Kurfürst': 'Großer Kurfürst',
    'Gaede': 'Ernst Gaede',
    'Кутузов': 'Михаил Кутузов',
    'P. E. Friedrich': 'Prinz Eitel Friedrich',
    'Gearing P': 'Gearing',
    'Jurien': 'Jurien de la Gravière',
    'Сталинград 2': 'Сталинград',
    'K. Albert': 'König Albert',
    'Окт. революция': 'Октябрьская революция',
    'Iwaki A': 'Iwaki Alpha',
    'E. Dragon': 'Eastern Dragon',
    'Maass': 'Leberecht Maass',
    'S. Dragon': 'Southern Dragon',
    'Montecuccoli': 'Raimondo Montecuccoli',
    'Giussano': 'Alberto di Giussano',
}
f = open('..\\db\\ship.json')
ships = json.load(f)
f.close()

out_file = 'out\\links.json'
old_links = {}
if os.path.exists(out_file):
    f = open(out_file)
    old_ships = json.load(f)
    for old_ship in old_ships:
        old_links[old_ship["ship_id"]] = old_ship
    f.close()

links = {}
for ship_id in ships:
    ship = ships[ship_id]
    if ship["type"] == "Auxiliary":
        continue
    if ship["nation"] == "events":
        continue

    ship_name = tr.gettext('IDS_' + ship['id_str']).decode('utf8').strip("[]")
    if ship_name.endswith('(old)') or ship_name.endswith('(OLD)'):
        continue
    if ship_name.startswith('IDS_') or ship_name.startswith('Disabled:'):
        continue

    wiki_url = "http://wiki.wargaming.net/ru/Ship:" + urllib.quote(ship_name.replace(' ', '_').encode('utf8'))
    if ship_id in old_links and old_links[ship_id]["status_code"] == 200 and old_links[ship_id]["ship_name"] == ship_name:
        wiki_status = 200
    else:
        wiki_page = requests.get(wiki_url)
        wiki_status = wiki_page.status_code

    if wiki_status == 404 and ship_name.encode('utf8') in nm:
        wiki_url = "http://wiki.wargaming.net/ru/Ship:" + urllib.quote(nm[ship_name.encode('utf8')].replace(' ', '_'))
        print wiki_url
        wiki_page = requests.get(wiki_url)
        wiki_status = wiki_page.status_code

    links[ship_id] = {
        "ship_id": ship_id,
        "id_str": ship['id_str'],
        "nation": ship['nation'],
        "tier": ship['tier'],
        "type": ship['type'],
        "ship_name": ship_name,
        "title": u"Wiki",
        "url": wiki_url,
        "status_code": wiki_status,
    }

    if wiki_status != 200:
        print "    '{}': '{}',".format(ship_name.encode('utf8', errors='ignore'), wiki_status)

newlist = sorted(links.values(), key=lambda k: k['id_str'])
with open(out_file, 'w') as outfile:
    json.dump(newlist, outfile, encoding='utf8', indent=2, sort_keys=True)
