# -*- coding: utf-8 -*-
import subprocess
from shutil import copyfile

python = 'C:\\Python27\\python.exe'

copyfile('C:\\src\\mxstat\\db\\ship.json', 'db\\ship.json')
copyfile('C:\\src\\mxstat\\res\\texts\\en\\LC_MESSAGES\\global.mo', 'res\\texts\\en\\LC_MESSAGES\\global.mo')
copyfile('C:\\src\\mxstat\\res\\texts\\ru\\LC_MESSAGES\\global.mo', 'res\\texts\\ru\\LC_MESSAGES\\global.mo')

res = subprocess.run(
    [python, 'parser.py'],
    shell=True,
    cwd='Wiki.ru'
)
if res.returncode != 0:
    exit(1)

res = subprocess.run(
    [python, 'makehtml.py'],
    shell=True,
    cwd='Wiki.ru'
)
if res.returncode != 0:
    exit(1)

res = subprocess.run(
    [python, 'parser.py'],
    shell=True,
    cwd='Forum.ru'
)
if res.returncode != 0:
    exit(1)

res = subprocess.run(
    [python, 'makehtml.py'],
    shell=True,
    cwd='Forum.ru'
)
if res.returncode != 0:
    exit(1)

res = subprocess.run(
    [python, 'make_links.py'],
    shell=True,
    cwd='.'
)
if res.returncode != 0:
    exit(1)

res = subprocess.run(
    [python, 'parser.py'],
    shell=True,
    cwd='Wiki.en'
)
if res.returncode != 0:
    exit(1)

res = subprocess.run(
    [python, 'makehtml.py'],
    shell=True,
    cwd='Wiki.en'
)
if res.returncode != 0:
    exit(1)

res = subprocess.run(
    [python, 'make_links_en.py'],
    shell=True,
    cwd='.'
)
if res.returncode != 0:
    exit(1)
