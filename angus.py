from anagram import *
ana = AnagramHelper('angus goodner')

res = ana.try_all('gong', 'sound', 'era')
res = ana.try_all('sag', 'or', 'dungeon')
res = ana.try_all('nerd', 'goon', 'suga')

res = ana.try_all('dr', 'nono', 'gauges')
res = ana.try_all('dr', 'no', 'gauge', 'son')

res = ana.try_all('surge')

res = ana.try_all('no', 'gags', 'no', 'rude')


res = ana.try_all('Dragon', 'Us', 'Gone')
res = ana.try_all('sun', 'dragon', 'ego')
res = ana.try_all('one', 'dragon', 'gus')
res = ana.try_all('dragonugones')
