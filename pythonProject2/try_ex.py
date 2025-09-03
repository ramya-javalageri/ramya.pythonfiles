a=2
b=0
try:
    print(a/b)
except Exception as e:
    print(e)
else:
    print('nothing')
finally:
    print('done')