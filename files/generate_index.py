# encoding: utf-8

import glob
import os
import sys

def file2list(filepath):
    ret = []
    with open(filepath, encoding='utf8', mode='r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def list2file(filepath, ls):
    with open(filepath, encoding='utf8', mode='w') as f:
        f.writelines(['{:}\n'.format(line) for line in ls] )

def get_filename(path):
    return os.path.basename(path)

def get_basename(path):
    return os.path.splitext(get_filename(path))[0]

MYFULLPATH = os.path.abspath(sys.argv[0])
MYDIR = os.path.dirname(MYFULLPATH)

query = '{}/*.md'.format(MYDIR)
markdown_files = glob.glob(query, recursive=False)

lines = []
for filepath in markdown_files:
    basename = get_basename(filepath)

    text = basename
    url = '{}.html'.format(basename)
    line = '- [{}]({})'.format(text, url)

    lines.append(line)

lines.insert(0, '# Index')

list2file('index.md', lines)
