import subprocess
import xml.etree.ElementTree as ET

path_to_game = 'C:\\Games\\World_of_Warships'

res = subprocess.run(['hg', 'update', 'release'])
if res.returncode != 0:
    exit(res.returncode)

f = open('version.txt', 'r')
version = f.read()
f.close()
print('version: {}'.format(version))

res_mods = ''
f = open(path_to_game + '\\paths.xml', 'r')
xml = ET.fromstring(f.read())
f.close()
for path in xml.iter('Path'):
    if path.text.startswith('res_mods'):
        res_mods = path.text[9:]
print('res_mods: {}'.format(res_mods))

if version != res_mods:
    res = subprocess.run(['hg', 'merge', 'default', '--tool', 'internal:other'], stderr=subprocess.PIPE)
    print(res.returncode, res.stderr.decode())

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
