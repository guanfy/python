
'''
exec("""for i in range(5):
    print("iter time:%d" % i)
""")

str = "for i in range(5):    print(i)"
c = compile(str,'','exec')
exec(c)


str = "3*4+5"
a = compile(str,'','eval')
print(eval(a))

'''
ws = ["desssssss","fxs","sdddd","qwerasdf"]
for w in ws[:]:
    print(w)
    if len(w) > 6:
        ws.insert(0,'w')
print(ws)

