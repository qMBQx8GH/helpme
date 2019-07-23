import os
import subprocess
import xml.etree.ElementTree as ET
import configparser

config = configparser.ConfigParser()
config.read('build.ini')
path_to_game = config['Game']['folder']

res = subprocess.run(['hg', 'update', 'release'])
if res.returncode != 0:
    exit(res.returncode)

f = open('version.txt', 'r')
version = f.read()
f.close()
print('version: {}'.format(version))

res_mods = ''
f = open(path_to_game + '\\game_info.xml', 'r')
xml = ET.fromstring(f.read())
f.close()
for vers in xml.iter('version_name'):
    res_mods = ".".join(vers.text.split(".")[0:4])
print('res_mods: {}'.format(res_mods))

if version != res_mods:
    res = subprocess.run(['hg', 'merge', 'default', '--tool', 'internal:other'], stderr=subprocess.PIPE)

    if res.returncode == 0:
        res = subprocess.run(['hg', 'com', '-v', '-m', 'merge'])
        if res.returncode != 0:
          exit(res.returncode)
    elif res.stderr.decode().startswith('abort: merging with a working directory ancestor has no effect'):
        pass
    else:
        print(res.stderr.decode())
        exit(res.returncode)

    f = open('version.txt', 'w')
    f.write(res_mods)
    f.close()
    res = subprocess.run(['hg', 'com', '-v', '-m', res_mods, 'version.txt'])
    if res.returncode != 0:
      exit(res.returncode)
    
subprocess.run(['hg', 'update', 'default'])
