with open('artificates01.txt','r') as f:
    text=f.read()


with open('artificates02.txt','w') as f:
    text = f.write(text + ' added lines')
print('end of stage 03')