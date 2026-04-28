import os
import random
import time
import json
import sys

import DO_MOD as DO
import AW_MOD as AW
import SH_MOD as SH

#屏幕大小为（79，40） 用80会换行

import tkinter as tk  #tk代替tkinter
screen = tk.Tk()  # 创建窗口
screen.title('sHaDow')
screen.geometry("250x200+100+100")  # 长x宽+x*y
screen.wm_attributes('-topmost',1)
canvas = tk.Canvas(screen, bg='white', height=250, width=250)

bool_input=[False]
order_present=['q']

gametime=0

class but: #按键用
    def fun():
        order_present.append(a)
        bool_input.append(True)
    def __init__(self,a):
        self.bt=tk.Button(command=lambda:(order_present.append(a)
        ,bool_input.append(True)),relief='groove',width=50,text=a)
        self.bt.pack()
            
def bind(event): #按键用
    order_present.append(event.keysym)
    bool_input.append(True)

def type0(m): #按键用
    return [m1.name for m1 in m]

class Save(): #大类
    global gametime

    bt=[]
    order={'bag','diary','self','back'}
    event='深夜'
    
    def judge(self):
        if type(self.pl)!=type(1):
            return
        #属性累加
        sa_e=0#san值
        h_e=1#生命加成
        h1_e=0#生命
        p_e=1#伤害倍率
        sp_e=0#蓄力速度
        sp1_e=1#蓄力速度加成
        si=0#视野
        ss_e=0#理智
        cc_e=0#混乱
        s_m_e=0#视野上限
        sp_m=1#蓄力上限
        for ob in self.bag:
            if ob in type0(SH.h_25):
                h_e+=0.25
            elif ob in type0(SH.h_40):
                h_e+=0.40#hp
            elif ob in type0(SH.p_20):
                p_e+=0.20
            elif ob in type0(SH.p_40):
                p_e+=0.40#power
            elif ob in type0(SH.s_1):
                sp_e+=1
            elif ob in type0(SH.s_2):
                sp_e+=2#speed
            elif ob in type0(SH.si):
                si+=1
            elif ob=='旧友难觅':
                h_e+=round((100-self.san)/100,1)
            elif ob=='金酒之杯':
                h_e-=0.5
                sp1_e+=1
            elif ob=='《终末世界的残响》':
                sa_e+=len([ob1 for ob1 in self.bag if SH.object_total[ob1].pro=='special'])*15          
            elif ob=='她的信':
                h1_e+=len([ob1 for ob1 in self.bag if SH.object_total[ob1].pro=='special'])*8
            elif ob=='月华':
                self.order.add('teleport')
            elif ob=='兰狄索斯的稿纸':
                self.order.add('relive')
            elif ob=='纸条':
                self.order.add('end')    
            elif ob=='她的白蔷薇 ':
                sa_e+=30
            elif ob=='绮良的日记':
                sa_e+=len(self.em)*15
            elif ob in type0(SH.sa_20):
                sa_e+=20#san
            elif ob=='帝国之影':
                cc_e+=10*self.pro['cc']
            elif ob=='金制的“法西斯”饰品':
                cc_e+=5*self.pro['cc']
            elif ob=='沾染泥土的书签':
                cc_e+=3*self.pro['cc']
                ss_e+=1*self.pro['ss']
                s_m_e-=2
                sp_e+=1
            elif ob=='已有裂纹的风铃':
                s_m_e+=2
            elif ob=='布满刮痕的公交车卡':
                ss_e+=5*self.pro['ss']
            elif ob=='残局棋谱':
                ss_e+=5*self.pro['ss']
            elif ob=='光洁的大理石':
                si+=2
            elif ob=='咒锥':
                sa_e-=20
                sp1_e+=0.3
            elif ob=='咒缚草人':
                sa_e-=20
                sp_m+=0.3
            elif ob=='老旧的旅行双肩包':
                h_e+=len([ob1 for ob1 in self.bag])*0.03
            elif ob=='古典八音盒':
                p_e+=len(self.em)*0.15
            elif ob=='冥灯':
                s_m_e+=2
                si+=3
            elif ob=='sHaDow':
                sa_e+=10000
                s_m_e+=3
                ss_e+=100
                cc_e+=100
                self.order.add('sHaDow')
                
        ma=self.Map[self.pl][0]  #黑戒
        block=0
        for x in range(-1,2):
            for y in range(-1,2):
                if 0<=x+ma.di[0]<=ma.width-1 and 0<=y+ma.di[1]<=ma.height-1:
                    if ma.it[y+ma.di[1]][x+ma.di[0]]=='  ':
                      block+=1
                else:
                    block+=1
        if block>=4 and '黑色的戒指' in self.bag:
            si+=2

        self.walk=len(set(tuple(x) for x in self.didi[self.pl]))
        if '手写的地图' in self.bag: #手写的地图及步数设置
            si+=self.walk//50
        self.walk=len(self.didi[self.pl])
                             
        self.san=round(self.san_basis+sa_e,1) #每过一层sight-1
        self.pro['sight_max']=self.pro['s_m_b']+s_m_e

        self.sans=self.sans_basis+ss_e
        self.chaos=self.chaos_basis+cc_e

        if self.pl<=4:
            pl_max=self.pl
        else:
            pl_max=4
        self.pro['sight']=self.pro['sight_basis']+si-pl_max+(self.sans//10+1)
        if 'sHaDow'in self.bag:
            self.pro['sight']=100
        if '伊始' in self.bag:
            self.pro['sight']=2
        if self.situation=='希冀':
            self.pro['ss']=2
        else:
            self.pro['ss']=1
        if self.situation=='犹豫':
            self.pro['cc']=2
        else:
            self.pro['cc']=1        

        #DO
        if self.san>=60:
            self.si2='正常。是在一尘不变的日常中麻木自我的健全人'
        elif self.san>=30:
            self.si2='恍惚。你精神涣散，却又莫名的兴奋'
        elif self.san>0:
            self.si2='涣散。除了想要追寻之物其他你什么都看不到'

        #走一步2.6 分钟
        a=gametime+480
        self.time_event=a
        h=(a//(60)%13+15)%24
        if 15<=h<19 and self.event=='深夜':
            SH.SH2(SH.d4,self)
            if '兰波的诗集' in self.bag:
                self.san_basis-=10
            else:
                self.san_basis-=30
            a=self.Map[plain.pl][0]
            a.print(self)
            print('''指令：wasd 移动 q跳过回合''')
        if 15<=h<19:
            self.event='午后'
        elif 19<=h<23:
            self.event='傍晚'
        else:
            self.event='深夜'
        #AW        
        self.pro2['hea']=round(3*((self.sans/5+0.5)**1.7*h_e),1)
        self.pro2['mon_max']=max(round((3*((self.chaos/9))**2+0.5)*sp_m,1),1.2)
        self.pro2['mon']=0
        
        if '热门游戏的通用秘籍' in self.bag:
            self.pro2['mon']=self.pro2['mon_max']//2
            
        self.pro2['mon_speed']=max(round((self.chaos/8)**1.5*sp1_e+sp_e,1),0.5)
        self.pro2['power']=round((self.chaos/16)*p_e+1,1)
        self.aw=AW.Object(name=self.name,monster=False,
    mon=self.pro2['mon'],hea=self.pro2['hea'],mon_max=self.pro2['mon_max'],
    mon_speed=self.pro2['mon_speed'],power=self.pro2['power'],bag=self.bag)

        #main
        try: #按键设置
            self.order=set(list(self.order).sort()[::-1])
        except:
            pass
        for i,o  in enumerate(self.order):
            if o in [bt['text'] for bt in self.bt]:
                continue
            b=but(o)
            self.bt.append(b.bt)
        for bt in self.bt:
            bt.pack()
        
    def __init__(self,name):
        #SH
        self.situation='雀跃'
        self.bag=[]
        self.em=[]
        self.diary=[]
        self.diary_2={'01':False,'02':False,'03':False}
        self.time=[]
        self.san_basis=100
        self.sans_basis=0
        self.chaos_basis=0

        self.win_ob=SH.fight_object_total #战胜后获得道具
        #DO
        self.pl=0 #当前角色地图位置
        self.Map=[] #当前地图总览
        self.pro={'sight':3 ,'md3':DO.md3,'sight_basis':2,'sight_max':6,
                  's_m_b':6,'cc':1,'ss':1}
        self.didi=[[] for x in range(8)]
        self.titi=[[] for x in range(8)]
        self.time_start=time.time()
        for x in range(7):
            while True:
                a=DO.init_map(width=random.randint(30,36),
                height=random.randint(30,32),direction=x)
                a.record=DO.deep(a.it,a.di2[0],a.di2[1],DO.map_dic)
                if a.record[0]==True:
                    break
            self.Map.append([a,x+1])
        self.Map[-1][1]=7

        while True:
            a=DO.init_map(width=random.randint(40,50),
                    height=random.randint(40,50),direction=7)
            a.record=DO.deep(a.it,a.di2[0],a.di2[1],DO.map_dic)
            if a.record[0]==True:
                    break    
        self.Map.append([a,'success'])
        
        #AW
        self.pro2={'mon':1,'hea':3,'mon_max':3,'mon_speed':1,'power':1}
        self.aw=AW.Object(name=name,monster=False,
                          mon=self.pro2['mon'],hea=self.pro2['hea'],
                          mon_max=self.pro2['mon_max'])
        #main
        self.si2='' 
        self.name=name
        self.judge()
        self.order={'bag','diary','self'}

        self.time_event=480 
        self.event='深夜'
        self.mix=0#纠缠

    def order0(self,m):
        if m=='back':
            show(self)
        if m=='diary':
            SH.diary(self)
            return 
        elif m=='self':
            SH.self(self)
            return 
        elif m=='bag':
            SH.bag(self)
            return 
        elif m=='teleport':
            m1=self.Map[self.pl][0]
            x1=[m1.xx(),m1.yy()]
            while m1.it[x1[0]][x1[1]]!='■':
                x1=[m1.xx(),m1.yy()]
            m1.it[m1.di[1]][m1.di[0]]='■'
            m1.it[x1[0]][x1[1]]='你'
            m1.di=x1[::-1]
            self.san_basis-=5
            show(self)
        elif m=='relive':
            m1=self.Map[self.pl][0]
            di=m1.di2[0]
            if self.san<=30:
                self.san_basis+=DO.distance(m1.di,di)*0.5
            m1.it[m1.di[1]][m1.di[0]]='■'
            m1.it[di[0]][di[1]]='始'
            m1.di=di
            
            show(self)
        elif m=='sHaDow':
            m1=self.Map[self.pl][0]
            di=m1.di2[1]
            m1.it[m1.di[1]][m1.di[0]]='■'
            m1.di=di
        elif m=='end':
            if self.pl==7:
                return
            self.order.remove('end')
            self.bag.remove('纸条')
            if '布满刮痕的公交车卡' in self.bag:
                SH.read_normal('txt//main04 谜底 A.txt')
                input()
                self.pl=7
                self.situation='雪落'
                self.pro['s_m_b']=3
                show(self)
            elif '沾染泥土的书签' in self.bag:
                SH.read_normal('txt//main04 谜底 B.txt')
                input()
                mt2=AW.Object(name='孤独的观测者',monster=True,personality=AW.name_dic2['醉'],hea=500,mon_max=70,floor=self.pl,bag=self.bag) 
                m=AW.fight(plain.aw,mt2)
                if m==self.name:
                    self.san=-100
                else:
                    self.pl='true'
                    print('''对峙，盘旋，厮杀
    你一次次撕开黑雾，然而那黑影的体力似乎无穷无尽
    不知过了多久，在你恢复了一些意识，睁开眼后
    黑影已经不见了
    全身上下都是伤，你几乎就想躺在地上好好睡一觉
    然而你勉强站了起来，知道这不是休息的时候''')
                    input()
            bool_input[-1]=False


def check_screen():
    while os.get_terminal_size()[0]<80 or os.get_terminal_size()[1]<40:
        print('当前屏幕宽度和长度：',os.get_terminal_size()[:]);print()
        print('需求宽度和长度至少为(80,40)，若未达成请放大屏幕或全屏化');print()
        print('按回车以检验')
        input()

def video():
    for x in range(50):
        m=[[' 'for m1 in range(79)] for m2 in range(40)]
        z=random.randint(0,60-x)+1
        o=60-x-z+1
        for z1 in range(z*10):
            m[(random.randint(0,39))][random.randint(0,78)]='0'
        for o1 in range(o*10):
            m[(random.randint(0,39))][random.randint(0,78)]='1'
        for m3 in m:
            print(''.join(m3))
        time.sleep(0.0001)
        n=os.system('cls')
    time.sleep(0.3)
    n=os.system('cls')
    for x in range(7):
        print('''\n\n\n
　　　　　　Ｈ　　　Ｈ　　　　　　　ＤＤＤＤ　
　　　　　　Ｈ　　　Ｈ　　　　　　　Ｄ　　　Ｄ
　ｓｓｓ　　Ｈ　　　Ｈ　ａａａａ　　Ｄ　　　Ｄ　　ｏｏｏ　　ｗ　ｗ　ｗ
ｓ　　　ｓ　Ｈ　　　Ｈ　　　　　ａ　Ｄ　　　Ｄ　ｏ　　　ｏ　ｗ　ｗ　ｗ
ｓ　　　　　ＨＨＨＨＨ　　　　　ａ　Ｄ　　　Ｄ　ｏ　　　ｏ　ｗ　ｗ　ｗ
　ｓｓｓ　　Ｈ　　　Ｈ　　ａａａａ　Ｄ　　　Ｄ　ｏ　　　ｏ　ｗ　ｗ　ｗ
　　　　ｓ　Ｈ　　　Ｈ　ａ　　　ａ　Ｄ　　　Ｄ　ｏ　　　ｏ　　ｗｗｗ
ｓ　　　ｓ　Ｈ　　　Ｈ　ａ　　　ａ　Ｄ　　　Ｄ　ｏ　　　ｏ　　ｗ　ｗ
　ｓｓｓ　　Ｈ　　　Ｈ　　ａａａａ　ＤＤＤＤ　　　ｏｏｏ　　　ｗ　ｗ
''')
        time.sleep(0.05)
        n=os.system('cls')
        time.sleep(0.05)

def show(save):
        n=os.system('cls')
        save.judge()
        notice(save)
        a=save.Map[plain.pl][0]
        a.print(save)
        print('''指令：wasd 移动 q跳过回合''')


def notice(plain):
    if plain.titi[plain.pl]!=[]:
        time=round(plain.titi[plain.pl][-1]-plain.titi[plain.pl][0],1)
    else:
        time=0
    print(plain.pl,'层 ',' 步数：',plain.walk,' 时间:',time,' 秒')
    t=plain.time_event
    print('事件时间:','第%d天 %d:%d 时间段:%s'%(t//(13*60),((t//(60))%13+15)%24,t%(60),plain.event))
    print('san: ',plain.san,'  ',plain.si2)
    print('sight',plain.pro['sight'],' /',plain.pro['sight_max'])
    print('状态： ',plain.situation,' 作用：',SH.eo_dic[plain.situation])
        
def check_aw(plain):
    while True:
        #ob=random.choice(SH.fight_object)
        #SH.fight_object.remove(ob)
        #plain.bag.append(ob.name)
        #plain.bag.append('《机械忍者2》典藏版')
        plain.judge()
        SH.bag(plain)
        SH.self
        mt2=AW.Object('敌人',True,personality=AW.name_dic2[random.choice(['偷','氓','醉'])],
                  floor=plain.pl)    
        m=AW.fight(plain.aw,mt2)
        plain.pl+=1
def check_sh(m):
    while True:
        SH.SH(m)
        SH.ap(m)
        SH.diary(m)
        SH.bag(m)
        #SH.eo(m)
        SH.self(m)

#check_sh(plain)
check_screen()
SH.read_normal('txt//游戏操作提示.txt')
input()
video()
plain=Save('plain')

#plain.bag.append('sHaDow')

#start
SH.SH_sy(plain)
SH.ap(plain)


def main():
    global gametime
    n=os.system('cls')
    a=plain.Map[plain.pl][0]
    a.player_move(order_present[-1],plain)
    if type(plain.pl)!=type(1):
            return
    plain.judge()
    a.monster_move(plain)
    notice(plain)
    a.print(plain)
    gametime+=2.6
    print('''指令：wasd 移动 q跳过回合''')

canvas.bind_all('<KeyPress-w>',bind)
canvas.bind_all('<KeyPress-a>',bind)
canvas.bind_all('<KeyPress-s>',bind)
canvas.bind_all('<KeyPress-d>',bind)
canvas.bind_all('<KeyPress-q>',bind)

main()

while plain.pl!='success' and plain.san>=0 and plain.pl!='true':
    try:
        plain.judge()
        time.sleep(0.01)
        screen.update()
        if bool_input[-1]==True:
            if order_present[-1] in ['w','a','s','d','q']:
                main()       
            else:
                plain.order0(order_present[-1])
            bool_input.append(False)
    except Exception as e:
        print(e)
        input()
        
if plain.san<0:
    print('你陷入了恐惧之中，无法再行走半步')
    print('游戏结束')
    input()
    sys.exit()
    
if plain.pl=='success' and '布满刮痕的公交车卡' in plain.bag:
    n=os.system('cls')
    SH.automatic_read('txt\\diary05.txt',speed=0.1)
    input()
if plain.pl=='true' and '沾染泥土的书签' in plain.bag:
    n=os.system('cls')
    SH.automatic_read('txt\\diary04.txt',speed=0.1)
    input()
n=os.system('cls')
print('游戏通关')
print('最后看一眼你的属性吧')
input()
SH.self(plain)
input()
SH.bag(plain)
input()
SH.diary(plain)
input()
n=os.system('cls')
time2=0
for x in range(7):
    try:
        if plain.titi[x]!=[]:
            time1=round(plain.titi[x][-1]-plain.titi[x][1],1)
            print('第%s层用时'%str(x),time1,'秒')
            time2+=time1
    except Exception as e:
        print(e)
print('总用时：',time2)
step=0
for x in range(7):
    try:
        if plain.didi[x]!=[]:
            print('第%s层步数'%str(x),len(plain.didi[x]))
            step+=len(plain.didi[x])
    except Exception as e:
        print(e)
print('总步数：',step)
input()
SH.read_normal('txt//幕后.txt')
input()
SH.read_normal('txt//感谢名单.txt')
input()
sys.exit()  



        
        
