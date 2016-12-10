# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

script,from_file,to_file=argv

open(to_file,'w').write(open(from_file).read())
#简化版
open(from_file).close()
open(to_file).close()