import sys
sys.path.append('.')

from http import *

client = Client()
response = client.mirror('http://lumberjaph.net', '/tmp/lj.txt')
