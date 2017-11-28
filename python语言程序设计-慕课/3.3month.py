# usr/bin/python
# -*- coding:utf-8 -*-

m = int(input("请输入一个表示月份的数字(1-12):"))

while(True):
    if m <=0 or m > 12:
        m =int(input("请输入一个有效的表示月份的数字(1-12):")) 
        continue
   
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    pos = (m-1)*3
    monthAbbrev = months[pos:pos+3]
    print("月份的简称是"+monthAbbrev+'.')
    break