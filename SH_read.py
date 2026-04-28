'''格式为字母+两位数字+文本
字母和数字可省略,
开头两个数字为位置
A为读取的开头
B为转折点，格式为字母+小写字母+数字（位置）
C为无转折点时的结尾，开头的数字写去处
D为判定姓名而进行不同转折的转折点，格式为D+两个数字(坐标)+姓名(3个空+两个数字+'其他'+两个数字
N为输入姓名
M为判定条件
数字写在文本前
E为文本全部的结尾，为结局,且与A有相同性质 最后一行是获得的东西
方便起见将不会去除开头和结尾的数字，可以看到
在任意地方输入大写的S会进行游戏存档，在任意地方输入大写的L会读档
最后结尾的地方要写个/'''
#strip函数功能为去掉空格
#n=os.system('cls')的功能为清空屏幕
#os.listdir作用为返回列表值
import time
import os
def Space(space):
    if space==False:
        print()
def automatic_read(txt,name='',speed=0.1,space=False):
    Flag=True
    with open(txt)as a:
        a=a.readlines()
    total=[[]for i in range(101) ]
    for line in a:
        if line[0]=='A'or line[0]=='E' or line[0]=='D':
            c=int(line[1:3].strip())     
        total[c].append(line[:-1])
        if line[0]=='B':
                c=100
    else: 
        save=0  #将存档初始位置设为0
        Save=[name,save,[]]
    while Flag==True:
        x=total[save]
        if x[0][0]=='E':#结局将会打完所有文本后结束
            for a in x[:-1]:
                Space(space)
                print(a)
                time.sleep(speed)
            Save[2]+=x[-1].split()
            print('输入回车结束')
            while True:
               s=input()
               if s in ['L','E','R','']:
                   break
            if s=='L':
                save=Save[1]
                print('已读档,当前位置',save)
                continue
            elif s=='R':
                save=0
                continue
            elif s=='E':
                Save[1]=save
                return Save
            else:
                return Save
        if x[0][0]=='D':
            if name==x[0][3:6].strip():
                save=int(x[0][6:8].strip())
            else:
                save=int(x[0][10:12].strip())
            continue
        for a in x :
            a=a.replace('%s',name)
            if a[0]=='N':
                Space(space)
                name=input()
                Save[0]=name
            elif a[0]=='B':
                Flag2=True
                while Flag2==True:   #存档模块
                    ans=input()
                    if ans=='S':
                        n=os.system('cls')
                        print('已存档，当前位置',save)
                        Save[1]=save
                        break
                    if ans=='L':
                        n=os.system('cls')
                        print('已读档,当前位置',save)
                        save=Save[1]
                        break
                    if ans in a[1:]and '9'<ans or ans<'0' and ans!='':#确保不是数字
                        b=a[:-1].find(ans)
                        save=int(a[b+1:b+3].strip())
                        Flag2=False
                        n=os.system('cls')
                    else:
                        print('输出选项不存在')
            elif a[0]=='C':
                save=int(a[1:3].strip())
       
            if 'A'<=a[0]<='Z' and a[0]!='B':
                Space(space)
                print(a[1:])
            elif a[0]=='B':
                pass
            else:
                Space(space)
                print(a)
            time.sleep(speed)
def search():
    m=os.listdir('txt')
    n=[]
    for x in m:
        if x[-4:]=='.txt':
           n.append([x[:-4]])
    for y in range(len(n)):
        n[y]=[y,':']+n[y]
    return n
def search_2():
    m=search()
    while True:
        for m1 in m:
            print(''.join(map(str,m1)))
        n=m[int(input())]
        automatic_read('txt/'+n[2]+'.txt',name='',speed=0.1,space=False,ob=False)
        n=os.system('cls')
#automatic_read('txt\\徘徊的罗马人b.txt',speed=0,space=False)
