#usr/bin/python
import random
import sys
import os

super_villains = {
    'captain cold' : 'leonard snart',
    'mirror master': 'sam scudder',
    'pied piper'   : 'thomas peterson'
}

#prints value for captain cold
print super_villains['captain cold']

#deletes mirror master key and value
del super_villains['mirror master']

#prints all keys and values
print super_villains

#changed value for one key
super_villains['pied piper'] = 'harley rathaway'
print super_villains['pied piper']

#prints all keys without values
print super_villains.keys()

#prints all values without keys
print super_villains.values()
