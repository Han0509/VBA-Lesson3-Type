#tuple1 = '1', '2',' 3', '4', '5'
#y = tuple1[3]
#print(y)

#tuple3 = ('lisa', 23, 'femal')
#namw, age, sex = tuple3
#print (namw, age, sex)
#宣告⼀個Tuple，名稱為gradesTuple •
# gradesTuple的第0個元素是國⽂成績，第1個是英⽂成績， 第2個是數學成績 •
# 1印出數學成績 •2印出各科平均 •3新增⾃然成績(94,90,96)，並印出全部成績
tuple4 = 1
tuple4 = 1,
#索引是中括號 Tuple 是小括號
gradesTuple = ((5,14,7),(23,36,28),(88,80,92))
print(gradesTuple[2])
x = sum(gradesTuple[2])/len(gradesTuple)
print(x)
#gradesTuple.append([94,90,96])  Tuple不能用append
scienceTuple = ((94,90,96),) #逗號是讓他知道是雙層的
gradesTuple = gradesTuple + scienceTuple
print(gradesTuple)




