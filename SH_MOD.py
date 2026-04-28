from SH_read import automatic_read
from save_SH import*
from os import system
import random
import time

def lend_SH(li,flag=True):  #规范输入：
    s=input('输入')
    while True:
        if flag==True:
            if s=='':
                return s
        if s not in li:
            print('请规范输入')
            s=input()
        else:
            return s

def chance_SH(List):
    max0=0
    x1=0
    List1=[]
    for x in range(len(List)):
        List1.append(random.random()*List[x][1])
        if List1[x]>=max0:
            x1=x
            max0=List1[x]
    return List[x1][0]
def search_time():
    for y in time.keys():
        print(y)
        for x in story_total:
            if x.time_start==y:
                print(x.name)
                print(story_dic[x.name])

def read_normal(txt):
    t=open(txt)
    for t1 in t.readlines():
        print(t1)
#search_time()

def SH2(story,Save):
    if story==e2_a:
        if '光洁的大理石' in Save.bag:
            Save.bag.remove('光洁的大理石')
            story=e2_a
        elif '金制的“法西斯”饰品' in Save.bag:
            Save.bag.remove('金制的“法西斯”饰品')
            story=e2_b
        else:
            story=e2_c

    elif story==s2:
        if '布满刮痕的公交车卡' in Save.bag:
            story=s2_a
        elif '沾染泥土的书签' in Save.bag:
            story=s2_b
        else:
            while True:
                print('迷惘者终将湮没于无限的轮回中。')
                time.sleep(0.1)
                n=system('cls')

    n=system('cls')
    print('遇到事件：',story.name)
    print()
    t1=story.time_start
    t2=story.time_end
    t3=story.t_c
    print('Time',t1,time00[t1])

    get=automatic_read(story.path,speed=0.1)[2]
    for get1 in get:
        if get1 in story.end.keys() and story.name[:5]!='daily':
            Save.diary.append([story.name,get1])
        elif get1 in story.su_name:
            Save.bag.append(get1)
        elif get1 in story.emotion:
            Save.em.append(get1)            
    Save.time.append(t2)
    return get
    #Save.check()

def time_daily(Save,daily,episode,time,daily2=''):
        sit=SH2(daily,Save)
        if sit==['1']:
            Save.san_basis+=15
            if time=='19:00':
                get=automatic_read(n1.path,speed=0.1)[2][0]
                print(get)
                if get=='1':
                    m=random.choice(Save.win_ob)
                    Save.win_ob.remove(m)
                    Save.bag.append(m.name)
                    print('获得道具： ',m.name)
                    input()
            elif time=='23:00':
                get=automatic_read(n2.path,speed=0.1)[2][0]
                if get=='5':
                    Save.chaos_basis+=4*Save.pro['cc']
                elif get=='6':
                    Save.sans_basis+=4*Save.pro['ss']
                elif get=='7':
                    Save.pro['sight_basis']+=1
                    
            elif time=='4:00':
                get=automatic_read(n3.path,speed=0.1)[2][0]
                if get=='5':
                    print('当前状态已重置')
                    Save.situation='雀跃'
                    input()
        elif sit==['2']:
            if episode!=[]:
                sit1=random.choice(episode)
                episode.remove(sit1)
                SH2(sit1,Save)
            else:
                print('什么事都没发生')
                print('你感到有些疲倦')
                Save.time.append(time)

def SH(Save):
        diary_name=[story[0] for story in Save.diary]
        if Save.event=='午后':
            time_daily(Save,d1,episode15,'19:00')
        elif Save.event=='傍晚':
            time_daily(Save,d2,episode19,'23:00')
        elif Save.event=='深夜':
            time_daily(Save,d3,episode22,'4:00')

def SH_sy(Save):
    diary_name=[story[0] for story in Save.diary]
    if 'main01存在的证明 Who' not in diary_name:
        SH2(s1,Save)
    elif ('main02世界的漏洞 Why A'in diary_name or 'main02世界的漏洞 Why B'in diary_name):
        if 'main03逃脱的方法 How' not in diary_name and Save.event=='午后':
            SH2(s3,Save)
    elif 'main01存在的证明 Who'in diary_name and ( 'main02世界的漏洞 Why A' not in diary_name and  'main02世界的漏洞 Why B' not in diary_name) and Save.event=='傍晚':
        if '布满刮痕的公交车卡' in Save.bag:
            SH2(s2_a,Save)
        else:
            SH2(s2_b,Save)
    
def bag(Save):
    n=system('cls')
    print('-----背包界面-------')
    for ob in range(len(Save.bag)):
        print(str(ob)+'.',end='')
        object_total[Save.bag[ob]].check()

def self(Save):
    n=system('cls')
    print('-----自我界面-------')
    print('目前拥有的情感:')
    print(Save.em)
    print('当前状态: ',Save.situation)
    print('作用： ',eo_dic[Save.situation])
    print('当前sight等级：',Save.pro['sight'])
    print('当前san值:',Save.san)
    print('理智点数：',Save.sans,' sight加成:',Save.sans//7,
          ' 战斗血量加成* ：',round((Save.sans/10+0.5)**1.7,1))
    print('混乱点数：',Save.chaos,
          ' 蓄力速度加成*：',round((Save.chaos/8)**1.5,1),
        ' 蓄力上限加成*:',round((2**(Save.chaos/9))+0.5,1),
        ' 战斗伤害加成*：',round(Save.chaos/16,1)) 
    print('当前战斗血量: ',Save.pro2['hea'],' 当前战斗蓄力上限: ',Save.pro2['mon_max'])
    print('当前战斗蓄力速度： ',Save.pro2['mon_speed'],'当前战斗伤害加成： ',Save.pro2['power'])

def diary(Save):
    n=system('cls')
    print('-----日记界面-------')
    di=[]
    for diary in Save.diary_2.keys():
        if Save.diary_2[diary]==True:
            di.append(diary)
    for di1 in di:
        read_normal('txt\\diary'+di1+'.txt')
        print()
    print('\n\n\n-----结局界面-------')
    for story in Save.diary:
        print('在 %s 中获得了 %s'%(story[0],story[1]))
               
def ap(Save):
    diary_name=[story[0] for story in Save.diary]
    end_name=[story[1] for story in Save.diary]
    if 'main01存在的证明 Who'in diary_name:
        Save.diary_2['01']=True
    if 'main02世界的漏洞 Why A' in diary_name:
        Save.diary_2['03']=True
    if 'main02世界的漏洞 Why B'in diary_name:
        Save.diary_2['02']=True
    if '徘徊的罗马人' in diary_name and '遗失在岁月中的答案' not in end_name and e2_a not in episode19:
        episode19.append(e2_a)

def eo(Save):
    if len(emotion_story2)>1:
        sit1=random.choice(emotion_story2)
        m=random.choice(emotion_story[sit1])
        n=system('cls')
        read_normal('txt//system01.txt')
        print()
        print('遇到情感泡：',sit1[12:][:-4])
        print()
        print('获得状态: '+m)
        print('效果: '+eo_dic[m])
        get=automatic_read(sit1,speed=0.1)[2]
        Save.em.append(get[0])
        Save.situation=m
        return m
    else:
        pass
