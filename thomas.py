from anagram import *
ana = AnagramHelper('Thomas Orlando')
res = ana.show_cons_vow_blurb()
print(res)

res = ana.try_all('hot', 'doom', 'snarl')
print(res)

res = ana.try_all('snarl', 'at', 'oh', 'doom')
print(res)


res = ana.try_all('oh', 'snarl', 'at', 'doom')
print(res)

res = ana.try_all('snort', 'mold')
print(res)

res = ana.try_all('loo', 'and', 'or', 'maths')
print(res)

res = ana.try_all('loo', 'and', 'sort', 'ham')
print(res)

res = ana.try_all('loo', 'and')
print(res)

res = ana.try_all('loo', 'asm')
print(res)

res = ana.try_all('hot', 'asmr', 'and', 'loo')
print(res)

res = ana.try_all('asm')
print(res)


res = ana.try_all('drool')
print(res)

res = ana.try_all('a', 'sloth', 'doorman')
print(res)

res = ana.try_all('hot', 'doorman')
print(res)

res = ana.try_all('doorman')
print(res)

res = ana.try_all('sloth')
print(res)

res = ana.try_all('a', 'randoom', 'sloth')
print(res)

res = ana.try_all('random')
print(res)

res = ana.try_all('random', 'has', 'tool')
print(res)

res = ana.try_all('random', 'stool', 'ah')
print(res)

res = ana.try_all('almond')
print(res)

res = ana.try_all('oath', 'or', 'almonds')
print(res)

res = ana.try_all('oath')
print(res)

res = ana.try_all('oath', 'mood', 'snarl')
print(res)

res = ana.try_all('loo', 'mad', 'snort', 'ha')
print(res)

res = ana.try_all('snort', 'da', 'moolah')
print(res)

res = ana.try_all('sad', 'moon') 
print(res)
