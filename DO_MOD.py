import random
import os
import copy
import time
import sys


import SH_MOD as SH
import AW_MOD as AW

def form(s):
    for x in range(len(s)):
        s[x][0][0]-=1
        s[x][0][1]-=1
        s[x][0][0],s[x][0][1]=s[x][0][1],s[x][0][0]

    return s
def deep(Maze,start,end,map_dic):
    maze=copy.deepcopy(Maze)
    start=list(start[::-1])#换成正的，输入是倒的（y,x
    end=list(end[::-1])
    for it1 in range(len(maze)):  #转换形式
        for it2 in range(len(maze[it1])):
            maze[it1][it2]=map_dic[maze[it1][it2]]
    maze.append([1 for x in range(len(maze[0]))])
    maze=[[1 for x in range(len(maze[0]))]]+maze
    for x in range(len(maze)):
        maze[x]=[1]+maze[x]+[1]
    st=[]
    Open=0
    Close=1
    Passed=2
    dirs=((0,1),(1,0),(0,-1),(-1,0))
    start[0]+=1;start[1]+=1
    end[0]+=1;end[1]+=1
    st.append([start,0])
    maze[start[0]][start[1]]=Passed
    if start==end:
        return [True,form(st)]
    while len(st)>0:
        pos,nextd=st[-1]
        if nextd==4:
            st.pop()
        while nextd<4:
            nextp=[pos[0]+dirs[nextd][0],pos[1]+dirs[nextd][1]]
            if nextp==end:
                st.append([end,0])
                return [True,form(st)]
            if maze[nextp[0]][nextp[1]]==Open:
                maze[nextp[0]][nextp[1]]=Passed
                st.append([nextp,0])
                break
            else:
                nextd+=1
                st[-1][1]=nextd
            if nextd==4:
                st.pop()
                if len(st)>0:
                    st[-1][1]+=1
    return [False,form(st)]       
'在这个代码中，坐标都是(x,y)的形式，调用则是[y][x]'
'模块不传入变量也可以直接用'
player_pl=0
map_list=[]
Maptype=[]
itdic={-2:'',-1:'',0:'口',1:'  '}
map_dic={'口':0,'  ':1,'你':0,'终':0,'始':0,0:0,1:1,'偷':0
         ,'醉':0,'氓':0,'影':0,'奇':0,'の':0,'◆':0}
mst=['偷','醉','氓','影']  #用在后面的类里了
mst_normal=['偷','醉','氓']

map_example=list(map_dic.keys())
map_hentai=['§','№','☆','○','●',
            '◎','◇','□','[]','€€',
            '口','△','▲','※','→','←',
            '↑','↓','〓','¤','♀','＠',
            '＆','＃']
map_hentai2=['а','б','в','г','д','е',
             'ё','ж','з','и',
             'л','м','н','о',
             'п','р','с','т','у',
             'ц','ч','ш','щ','ъ','ы','ь']
#用于焕然
md3={}
for x in range(len(map_example)):
    md3[map_example[x]]=random.choice(map_hentai)
    md3['??']=random.choice(map_hentai2)
#用于纠缠 以前
md4={'':''}
m41=['w','a','s','d','q']
m42=m41[::]
random.shuffle(m42)
for x in range(5):
    md4[m41[x]]=m42[x]

def chance(List):
    max0=0
    x1=0
    List1=[]
    for x in range(len(List)):
        List1.append(random.random()*List[x][1])
        if List1[x]>=max0:
            x1=x
            max0=List1[x]
    return List[x1][0]

#sight的初始化
def sight(n):
    if n%2==1:
        return [(x,y) for x in range(-n,n+1) for y in range(-n,n+1)]
    else:
        a=[(x,y) for x in range(-n+1,n) for y in range(-n+1,n)]
        b=[(-n,0),(n,0),(0,n),(0,-n)]
        return (a+b)
sight_dic={}   
for x in range(1,10):
    sight_dic[x]=sight(x)

'''前进应使用wsad'''
'[y][x]'
def lend(li,flag=False):  #规范输入：
    s=input('输入')
    if flag==True:
        if s=='':
            return s
    while True:
        if s not in li:
            print('请规范输入')
            s=input()
        else:
            return s
def distance(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5
class Map_total():
    #初始化函数
    def xx(self):
        return random.randint(0,self.height-1)
    def yy(self):
        return random.randint(0,self.width-1) #就根据惯性思维用就可以(x,y
    def huge_analyze(self):
        huge=0 
        for x in self.it:
            for y in x:
                if y=='口':
                    huge+=1#判定地图空格的一个函数
        return huge
 

    def update_monster(self,nu): 
        for x in range(nu):
            x1=[self.xx(),self.yy()]
            while self.it[x1[0]][x1[1]]!='口'or distance(self.di,x1[::-1])<=5:
                x1=[self.xx(),self.yy()]
            x2=random.choice(mst_normal)
            self.it[x1[0]][x1[1]]=x2
    def update_shijian(self):
        qi=[self.di[::-1]]
        for x in range(6):
            x1=[self.xx(),self.yy()]
            while self.it[x1[0]][x1[1]]!='口'or min([distance(x2,x1) for x2 in qi])<=5:
                x1=[self.xx(),self.yy()]
            self.it[x1[0]][x1[1]]='奇'
            qi.append(x1)
        for x in range(5):
            x1=[self.xx(),self.yy()]
            while self.it[x1[0]][x1[1]]!='口':
                x1=[self.xx(),self.yy()]
            self.it[x1[0]][x1[1]]='の'
    def update_shadow(self,nu):
        for x in range(nu):
            x1=[self.xx(),self.yy()]
            while self.it[x1[0]][x1[1]]!='口'or distance(self.di,x1[::-1])<=5:
                x1=[self.xx(),self.yy()]
            self.it[x1[0]][x1[1]]='影'

    def add_blank(self,x,y):
        for x1 in x:
            for y1 in y:
                self.it[y1][x1]='  '
                
    def add_blank_random(self,nu):
        for m in range(nu):
            self.it[self.xx()][self.yy()]='  '
    

    def born(self):
        while True:
            start=[self.xx(),self.yy()]
            end=[self.xx(),self.yy()]
            while self.it[start[0]][start[1]]!='口':
                start=[self.xx(),self.yy()]
            while self.it[end[0]][end[1]]!='口':
                end=[self.xx(),self.yy()]
            a=distance(start,end)>=int(self.height**2+self.width**2)**0.5*0.5
            if start!=end and a:
                break   #终点和起点距离限制，可调
        self.it[start[0]][start[1]]='你'
        self.it[end[0]][end[1]]='终'
        self.di=start[::-1]
        self.di2=[start[::-1],end[::-1]]#在此处翻转


    #用于维持地图运行  
    def print(self,save):  #skylin 打印地图
        if save.situation=='纠缠':
            if save.walk-save.mix>=20:
                save.mix=save.walk
                save.order0('teleport')
                save.san_basis+=5
        if save.san<30: #san惩罚
            save.pro['md3']={}
            for x in range(len(map_example)):
                save.pro['md3'][map_example[x]]=random.choice(map_hentai)
                save.pro['md3']['??']=random.choice(map_hentai2) 
        itself=copy.deepcopy(self.it)
        itself_init=copy.deepcopy(self.it_init)

        x1=[]
        y1=[]

        if '闪耀星海的信标'in save.bag:
            end=self.di2[1]
            itself_init[end[1]][end[0]]=2
        
        for y in range(len(itself)):#遍历
            for x in range(len(itself[y])):
                if itself[y][x]=='  ' and save.situation=='空明':
                    itself_init[y][x]=2
                elif [x,y] in save.didi[save.pl] and '远天旅人的追忆' in save.bag:
                    itself_init[y][x]=2
                if itself[y][x] in mst and '维苏威火山的余烬' in save.bag:
                    itself_init[y][x]=2
                elif itself[y][x] =='奇' and '她的红蔷薇' in save.bag:
                    itself_init[y][x]=2

        if save.pro['sight']==100:
            for y in range(len(itself_init)):
                for x in range(len(itself_init[y])):
                    itself_init[y][x]=2
        if save.pro['sight']<1:
            save.pro['sight']=1
        if save.pro['sight']>save.pro['sight_max']:
            save.pro['sight']=save.pro['sight_max']
        
        elif save.pro['sight']<=save.pro['sight_max']: #关于视力范围。
            for sight in sight_dic[save.pro['sight']]:
                y=self.di[1]+sight[1]
                x=self.di[0]+sight[0]
                if 0<=x<=self.width-1 and 0<=y<=self.height-1:
                    itself_init[y][x]=2
                
                    
                    x1.append(x)#雪落
                    y1.append(y)
            xmax,xmin,ymax,ymin=max(x1),min(x1),max(y1),min(y1)

        else:
            for sight in sight_dic[6]:
                y=self.di[1]+sight[1]
                x=self.di[0]+sight[0]
                if 0<=x<=self.width-1 and 0<=y<=self.height-1:
                    itself_init[y][x]=2

        for y in range(len(itself_init)):
            for x in range(len(itself_init[y])):
                if itself_init[y][x]==2:  #标注点
                    if itself[y][x]=='の':
                        itself[y][x]='口'
                    if save.situation=='漠视' and itself[y][x] in mst:
                        itself[y][x]='口'
                    if [x,y] in save.didi[save.pl][:-1] and ( save.situation=='忽视'):
                        itself[y][x]='◆'



                else:
                    itself[y][x]='??'

                    if save.situation=='雪落' and not(ymin<=y<=ymax and xmin<=x<=xmax):
                        itself[y][x]=''
                if save.situation=='焕然'or save.san<30:
                    itself[y][x]=save.pro['md3'][itself[y][x]]


        itself2=[]
        if save.situation=='雪落':
            for it2_1 in range(len(itself)):
                itit=''
                for it2_2 in range(len(itself[it2_1])):
                    if ymin<=it2_1<=ymax and xmin<=it2_2<=xmax:
                        itit+=itself[it2_1][it2_2]
                if itit!='':
                    itself2.append("".join(itit))
            print("\n".join(itself2))
            return
        
        sample=''.join([str(x)+' ' for x in range(self.width)if x<10]+
                      [str(x) for x in range(self.width)if x>=10])

        print(sample)


        
        for it2_1 in range(len(itself)):
            itself2.append("".join(itself[it2_1])+str(it2_1))
        print("\n".join(itself2))

        self.it[self.di[1]][self.di[0]]='你'
        
    def mark(self):  #用于标记出口和入口
        start=self.di2[0]
        end=self.di2[1]
        if self.di!=self.di2[0]:
            self.it[start[1]][start[0]]='始'
        if self.di!=self.di2[1]:
            self.it[end[1]][end[0]]='终'
        
    def exchange(self,lend1,di=None):  #用于变换坐标
        if di==None or di=='q':
            di=copy.deepcopy(list(self.di))
        if lend1=='w':
            di[1]-=1
        elif lend1=='s':
            di[1]+=1
        elif lend1=='a':
            di[0]-=1
        elif lend1=='d':
            di[0]+=1
        return list(di)

    def player_move(self,lend1,save): #none 用于空格识别
        di=self.exchange(lend1)

        if not(0<=di[0]<=self.width-1 and 0<=di[1]<=self.height-1):
                print('''
WARING:

超过地图边界

''')
                return
        elif self.it[di[1]][di[0]] =='  ':
                print('''
WARING:

禁止通行

''')
                return

        if '往昔' in save.bag:
            if di in save.didi[save.pl]:
                pass
            else:
                save.san_basis+=0.3
        if save.situation=='忽视':
            if di in save.didi[save.pl]:
                save.san_basis-=0.5
        save.didi[save.pl].append(di)
        save.titi[save.pl].append(time.time())
        
        if self.it[di[1]][di[0]] in mst:  #遇到怪物 
            mt=self.it[di[1]][di[0]]
            if mt=='影':
                mt=random.choice(['偷','氓','醉'])
            mt2=AW.Object('敌人',True,personality=AW.name_dic2[mt],floor=save.pl,bag=save.bag)    
            save.aw.speed=True
            if '伊始' not in save.bag and save.situation!='脆弱' and save.aw.mon_speed !=0:
                m=AW.fight(save.aw,mt2)
            elif '伊始' in save.bag:
                m='?????'
                print('''
WARING:

伊始效果发动。获得战斗胜利。

''')
            elif save.situation=='脆弱':
                m=save.name
                print('''
WARING:

脆弱效果发动，战败

''')
            elif save.aw.mon_speed==0:
                m=save.name
                
            if m==save.name:
                self.fail(save)
            else:
                self.success(save)
            input()
            n=os.system('cls')

        if self.it[di[1]][di[0]]=='终':  #链表
            save.pl=save.Map[save.pl][1]
            SH.SH_sy(save)
            SH.ap(save)
        elif self.it[di[1]][di[0]]=='奇':  #链表
            SH.SH(save)
            SH.ap(save)
        elif self.it[di[1]][di[0]]=='の':
            m=SH.eo(save)
            if m=='暴雨':
                self.update_shadow(30)
            elif m=='断离':
                save.em=[]
        self.it[self.di[1]][self.di[0]]='口'
        self.it[di[1]][di[0]]='你'
        self.di=di
        self.mark() #用于出口和入口的标记wq
   
    def move(self,di):
        li=[]
        for x in [[0,1],[1,0],[0,-1],[-1,0]]:
            a=[di[0]+x[0],di[1]+x[1]]
            if 0<=a[0]<=self.width-1 and 0<=a[1]<=self.height-1:
                if self.it[a[1]][a[0]]=='口'or self.it[a[1]][a[0]]=='你':
                    li.append(a)
        if li!=[]:
            a=random.choice(li)
            return a
        return False
        
    def monster_move(self,save):  #每次找到地图中所有的怪并让他们移动
        li=[]
        for y in range(self.height):
            for x in range(self.width):
                if self.it[y][x] in mst:
                    di=self.move([x,y])
                    li.append([[x,y],di])
        for a in li:
            x=a[0][0];y=a[0][1];di=a[1]
            if di!=False:
                if self.it[di[1]][di[0]]=='你':
                    mt=self.it[y][x]
                    self.it[y][x]='口'
                    if mt=='影':
                        mt=random.choice(['偷','氓','醉'])
                    mt2=AW.Object('敌人',True,personality=AW.name_dic2[mt],floor=save.pl,bag=save.bag,speed=True)
                    print('''
WARING:

''')
                    print('你听到背后有脚步声')
                    print('你感到头部被重击')
                    self.fail(save)

                else:
                    self.it[di[1]][di[0]]=copy.deepcopy(self.it[y][x])
                    self.it[y][x]='口'

    def success(self,save):
        print('''对方趔趔趄趄逃走了
你感到有些劳累
san值减少''')
        if '《除我之外的世界》' not in save.bag:
                save.san_basis-=10
        else:
                print('《除我之外的世界》效果发动。理智消耗减免')
                save.san_basis-=5
        m=chance([['else',4],['ob',6]])
        if m=='ob' and len(save.win_ob)>0:
            print('你发现对方似乎遗漏了什么东西在地上')
            m=random.choice(save.win_ob)
            save.win_ob.remove(m)
            save.bag.append(m.name)
            print('获得道具： ',m.name)
        m=random.choice(['s','c'])
        if m=='s':
            n=random.randint(1,3)
            print('获得理智点数',n)
            save.sans_basis+=n
        if m=='c':
            n=random.randint(1,3)
            print('获得混乱点数',n)
            save.chaos_basis+=n
    def fail(self,save):
        print('''你失去了意识。
许久之后当你重新站起来时
感到身上各处酸痛不已
san值减少

''')
        save.san_basis-=20

class init_map(Map_total):
    def __init__(self,width,height,direction,di2=[],time=0,record=None):
        self.width=width
        self.height=height
        self.direction=direction  #地图的位置标志
        self.di2=di2 #地图的起点和终点 
        self.time=time#记录你的回合数
        self.it=[[0 for x in range(width)]for y in range(height)]
        self.it_init=copy.deepcopy(self.it)
        for it1 in range(len(self.it)):  #转换形式
            for it2 in range(len(self.it[it1])):
                self.it[it1][it2]=itdic[self.it[it1][it2]]
        self.huge=0.5*self.huge_analyze()#用来加空格
        self.add_blank_random(random.randint(int(0.8*self.huge),int(self.huge)))
        self.huge=self.huge_analyze()
        self.born()
        if self.direction==7:
            self.update_shadow(40)
            return
        self.update_monster(int(self.huge/55+3))
        if record==True:
            pass
        else:
            self.update_shijian()
    def print_pro(self):
        a=[self.width,self.height,self.di,self.di2,self.direction,self.it,it_init,
           self.huge,self.record]
        b=['width宽','height高','di玩家位置(x,y)','di2初始点终末点(y,x',
           'direction地图位置','it地图本体','it_init 由0和1组成的初始地图边界,利用这个帮助sight',
           'huge空白数','record寻路路径']
        for x in range(len(a)):
            print(b[x],':',a[x])
