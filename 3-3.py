# list use () /tuple uses[] /dictionary use {Key 和value} /Set只有value沒有get
family = {'dad':'papa','mom':'mama','son':'odd'}
#--------------------
family['dad'] = 'andy'
print(family)
print(family.get('dad'))
print(family.get('andy'))
#print(family('andy')) 出錯了
#-------------------------
print('dad' in family)
print(family)
#-----------------------------
print(family.keys())
print(family.values())
print(family.items())
#-----------------
family = {}
family['cousin'] = 'ccccc'
family.update({'uncle': 'uuuuu', 'aunt':'aaaa'})
print(family)
del family['cousin']
family.pop('uncle')
print(family)
#宣告⼀個dict，名稱為gradesDict
# gradesDict的‘chinese’是國⽂成績，‘english’是英 ⽂成績，‘math’是數學成績 •
# 印出數學成績 •
# 印出各科平均 •
# 新增⾃然(science)成績[94,90,96]，並印出全部成績
gradesDict = {'chinese':[5,14,7],'English':[23,36,28],'Math':[88,80,92]}
mathScores = gradesDict.values()
print(mathScores)
gradesDict.updates({'Science':[88,80,92]})
print(gradesDict)