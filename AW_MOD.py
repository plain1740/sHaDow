import os
import random
import copy
name_dic={'slient':'谨慎的','brave':'莽撞的','balance':'随和的'
     ,'cat':'小偷','pig':'醉汉',
     'dog':'流氓'}
name_dic2={'偷':'cat','氓':'dog','醉':'pig'}
lead={-2:'defend',-1:'hide',0:'mon',1:'clap'}
dic_defend={'slient':0.8,'brave':0.3,'balance':0.5}
dic_hide={'slient':1.2,'brave':0.8,'balance':1}
dic_mon={'slient':1.2,'brave':1.2,'balance':1}
dic_clap={'slient':0.8,'brave':1.5,'balance':1}
dic_mon1={'slient':1,'brave':1.5,'balance':0.5}
hea_init={'cat':5,'pig':3,'dog':1}
mon_init={'cat':1,'pig':5,'dog':3}

dic={-2:'反弹',-1:'趴下',0:'蓄力'}
for x in range(1,100):  #完善dic
    dic[x]='%s拳'%x




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
class Object():
    def __init__(self,name,monster,personality=None,mon=None,hea=None,mon_max=None
                 ,floor=0,mon_speed=1,power=1,bag=[],speed=False):
        self.name=name
        self.mon=mon
        self.mon_max=mon_max
        self.hea=hea
        self.mon_speed=mon_speed
        self.power=power
        self.monster=monster
        self.pro=0
        self.mon_init=1
        self.habit=random.choice(['no brain','wise'])
        self.type=random.choice(['slient','brave','balance'])
        self.personality=personality
        self.floor=floor*0.7
        self.bag=bag
        if self.name=='孤独的观测者':
            self.mon=0
            self.mon_speed=70 
            return
        if self.monster==True:
            self.hea=round((random.uniform(1,3)+hea_init[self.personality])*(floor*2+1),1)
            self.mon_max=round(5*(floor*2+1),1)
            self.mon=round((random.uniform(0,self.mon_max//10+0.5)+mon_init[self.personality])*(floor//2+1),1)
            if self.mon>self.mon_max:
                self.mon=self.mon_max
            self.mon_speed=self.mon_max//5
            self.name=name_dic[self.type]+name_dic[self.personality]
        if speed==True:
            self.mon*=1.5

        
    def right(self,a):
        if self.mon<1:
            return 0
        else:
            return a
    def right1(self,a):
        if self.mon<self.mon_max//4+1:
            return 0
        else:
            return a

    def shuchu(self,time,other):#enemy thinking
        
        if self.name=='孤独的观测者':
            if time%5==1:
                self.pro=0
                m=70
                m1=[random.randint(14,18) for x in range(2)]+[13]
                random.shuffle(m1)
                m1.append(m-sum(m1)-13)
                self.type=m1
            else:
                if self.type[(time-2)%5]==13:
                    self.pro=-2
                else:
                    self.pro=self.type[(time-2)%5]
                
            return

        while True:
            if self.habit=='no brain': #random
                self.pro=chance([[-2,self.right1(dic_defend[self.type])],
                                 [-1,dic_hide[self.type]],
                                 [0,dic_mon[self.type]],
                                 [1,self.right(dic_clap[self.type])]])
                
                if self.mon>=self.mon_max:#max
                    self.pro=chance([[-2,self.right1(dic_defend[self.type])],
                                 [-1,dic_hide[self.type]],
                                 [1,self.right(dic_clap[self.type])]])
                if self.pro==1:
                        self.pro=random.randint(1,int(self.mon))
                        return
                else:
                        return False
            elif self.habit=='wise':
                if other.mon<2*dic_mon1[self.type]: #根据对方钱数进行判定
                    self.pro=chance([[0,dic_mon[self.type]]
                                 ,[1,self.right(dic_clap[self.type])]])
                    if self.mon>=self.mon_max:#max
                        self.pro=1
                    if self.pro==1:
                            self.pro=random.randint(1,int(self.mon))
                            return
                    else:
                            return False

                else:
                    if self.type=='brave' and self.mon>=self.mon_max//2:
                        self.pro=self.mon_max//2
                        return
                        
                    else:
                        self.pro=chance([[-2,self.right1(dic_defend[self.type])],
                                 [-1,dic_hide[self.type]],
                                 [0,dic_mon[self.type]],
                                 [1,self.right(dic_clap[self.type])]])
                        if self.mon>=self.mon_max:#max
                            self.pro=chance([[-2,self.right1(dic_defend[self.type])],
                                 [-1,dic_hide[self.type]],
                                 [1,self.right(dic_clap[self.type])]])
                        if self.pro==1:
                                self.pro=random.randint(1,int(self.mon))
                                return
                        else:
                                return False
            break
    def shuru(self):#people thinking
        c=['.']
        for b in range(-2,99):
            c.append(str(b))
        while True:
            a=input('输入')
            if a=='.':
                a=-1
            
            if a in c:
               a=int(a)
               if a==0 and self.mon>=self.mon_max:
                   print('蓄力已经达到上限')
               elif a<=self.mon or ('《机械忍者2》典藏版' in self.bag and a<=self.mon_max//8+1) :
                   if a==-2 and self.mon<self.mon_max//4+1:
                       print('使用拳数超过蓄力条')
                   else:
                       self.pro=a
                       return
               else:
                   print('使用拳数超过蓄力条')
            else:
                print('输入超出范围')
def chuli(mt,pr,time):
     if pr.name=='孤独的观测者':
         mt.shuru()
         pr.shuchu(time,mt)

         a=mt.pro
         b=pr.pro
         if a==0 :
             mt.mon+=1*mt.mon_speed
             if mt.mon>=mt.mon_max:
                 mt.mon=mt.mon_max
         if b==0 :
             pr.mon+=1*pr.mon_speed
             if pr.mon>=pr.mon_max:
                 pr.mon=pr.mon_max
         if a>0:
            if ('《机械忍者2》典藏版' in mt.bag and a<=mt.mon_max//8+1):
                 print('《机械忍者2》典藏版效果发动')
            else:
                mt.mon-=a
         if b>0:
             pr.mon-=b
         if a==-2:
             mt.mon-=(mt.mon_max//4+1)
             ft=(mt.mon_max//4+1)
         if b==-2:
             pr.mon-=13

         print(mt.name,dic[a],end=' ')
         print(pr.name,dic[b])

         if (a in [-2,-1,0] and b in [-2,-1,0])or(a==b):
             print('无事发生')
         elif b==0:
                a1=round((a-b)*mt.power,1)
                pr.hea-=a1
                print(pr.name,'生命减少',a1)
             
         elif a>=0 and b>0:
             if a>b:
                 a1=round((a-b)*mt.power,1)*0.2
                 pr.hea-=a1
                 print('孤独的观测者隐藏在黑雾之中')
                 print(pr.name,'躲避后生命减少',a1)
             if b>a:
                 a1=round((b-a)*pr.power,1)
                 if '三途之骨' in mt.bag and mt.mon!=0:
                     if mt.mon>=a1:
                         mt.mon-=a1
                         a1=0
                         print('三途之骨效果发动,抵挡全部伤害')
                     else:
                         a1-=mt.mon
                         mt.mon=0
                         mt.hea-=a1
                         print('三途之骨效果发动,抵挡部分伤害')
                         print(mt.name,'生命减少',a1)
                 else:
                     mt.hea-=a1
                     print(mt.name,'生命减少',a1)
         elif a==-1:
                 a1=round((b)*pr.power*0.2,1)
                 if '三途之骨' in mt.bag and mt.mon!=0:
                     if mt.mon>=a1:
                         mt.mon-=a1
                         a1=0
                         print('三途之骨效果发动,抵挡全部伤害')
                     else:
                         a1-=mt.mon
                         mt.mon=0
                         mt.hea-=a1
                         print('三途之骨效果发动,抵挡部分伤害')
                         print(mt.name,'躲避后生命减少',a1)
                 else:
                     mt.hea-=a1
                     print(mt.name,'躲避后生命减少',a1)
         elif a==-2:
             if b>ft*2:
                 print('反弹失败')
                 a1=round(b*pr.power,1)
                 if '三途之骨' in mt.bag and mt.mon!=0:
                     if mt.mon>=a1:
                         mt.mon-=a1
                         a1=0
                         print('三途之骨效果发动,抵挡全部伤害')
                     else:
                         a1-=mt.mon
                         mt.mon=0
                         mt.hea-=a1
                         print('三途之骨效果发动,抵挡部分伤害')
                         print(mt.name,'生命减少',a1)
                 else:
                     mt.hea-=a1
                     print(mt.name,'生命减少',a1)
             else:
                 print('反弹！')
                 if '名刀的碎片 ▪ 壹' in mt.bag:
                     print('名刀的碎片 ▪ 贰 效果发动,双倍反弹!')
                     a1=round(b*mt.power*2,1)
                     pr.hea-=a1
                     print(pr.name,'生命减少',a1)
                 else:
                     a1=round(b*mt.power,1)
                     pr.hea-=a1
                     print(pr.name,'生命减少',a1)
         elif b==-2:
             if a*mt.power>26:
                 print('反弹失败')
                 a1=round(a*mt.power,1)
                 pr.hea-=a1
                 print(pr.name,'生命减少',a1)
             else:
                 print('反弹！')
                 a1=round(a*pr.power,1)
                 if '三途之骨' in mt.bag and mt.mon!=0:
                     if mt.mon>=a1:
                         mt.mon-=a1
                         a1=0
                         print('三途之骨效果发动,抵挡全部伤害')
                     else:
                         a1-=mt.mon
                         mt.mon=0
                         mt.hea-=a1
                         print('三途之骨效果发动,抵挡部分伤害')
                         print(mt.name,'生命减少',a1)
                 else:
                     mt.hea-=a1
                     print(mt.name,'生命减少',a1)
         return

     
     if mt.monster==True:
         mt.shuchu(time,pr)
     else:
         mt.shuru()
     if pr.monster==True:
         pr.shuchu(time,mt)
     else:
         pr.shuru()
     a=mt.pro
     b=pr.pro
     if a==0 :
         mt.mon+=1*mt.mon_speed
         if mt.mon>=mt.mon_max:
             mt.mon=mt.mon_max
     if b==0 :
         pr.mon+=1*pr.mon_speed
         if pr.mon>=pr.mon_max:
             pr.mon=pr.mon_max
     if a>0:
        if ('《机械忍者2》典藏版' in mt.bag and a<=mt.mon_max//8+1):
             print('《机械忍者2》典藏版效果发动')
        else:
            mt.mon-=a
     if b>0:
         pr.mon-=b
     if a==-2:
         mt.mon-=(mt.mon_max//4+1)
         ft1=(mt.mon_max//4+1)
     if b==-2:
         pr.mon-=(pr.mon_max//4+1)
         ft2=(pr.mon_max//4+1)
     print(mt.name,dic[a],end=' ')
     print(pr.name,dic[b])
     if (a in [-2,-1,0] and b in [-2,-1,0])or(a==b):
         print('无事发生')
     elif a>=0 and b>=0:
         if a>b:
             a1=round((a-b)*mt.power,1)
             pr.hea-=a1
             print(pr.name,'生命减少',a1)
         if b>a:
             a1=round((b-a)*pr.power,1)
             if '三途之骨' in mt.bag and mt.mon!=0:
                 if mt.mon>=a1:
                     mt.mon-=a1
                     a1=0
                     print('三途之骨效果发动,抵挡全部伤害')
                 else:
                     a1-=mt.mon
                     mt.mon=0
                     mt.hea-=a1
                     print('三途之骨效果发动,抵挡部分伤害')
                     print(mt.name,'生命减少',a1)
             else:
                 mt.hea-=a1
                 print(mt.name,'生命减少',a1)
     elif a==-1:
         a1=round((b)*pr.power*0.2,1)
         if '三途之骨' in mt.bag and mt.mon!=0:
             if mt.mon>=a1:
                 mt.mon-=a1
                 a1=0
                 print('三途之骨效果发动,抵挡全部伤害')
             else:
                 a1-=mt.mon
                 mt.mon=0
                 mt.hea-=a1
                 print('三途之骨效果发动,抵挡部分伤害')
                 print(mt.name,'生命减少',a1)
         else:
             mt.hea-=a1
             print(mt.name,'躲避后生命减少',a1)
     elif b==-1:
             a1=round((a)*mt.power*0.2,1)
             pr.hea-=a1
             print(pr.name,'躲避后生命减少',a1)
     elif a==-2:
         if b>ft1*2:
             print('反弹失败')
             a1=round(b*pr.power,1)
             if '三途之骨' in mt.bag and mt.mon!=0:
                 if mt.mon>=a1:
                     mt.mon-=a1
                     a1=0
                     print('三途之骨效果发动,抵挡全部伤害')
                 else:
                     a1-=mt.mon
                     mt.mon=0
                     mt.hea-=a1
                     print('三途之骨效果发动,抵挡部分伤害')
                     print(mt.name,'生命减少',a1)
             else:
                 mt.hea-=a1
                 print(mt.name,'生命减少',a1)
         else:
             print('反弹！')
             if '名刀的碎片 ▪ 壹' in mt.bag:
                 print('名刀的碎片 ▪ 贰 效果发动,双倍反弹!')
                 a1=round(b*mt.power*2,1)
                 pr.hea-=a1
                 print(pr.name,'生命减少',a1)
             else:
                 a1=round(b*mt.power,1)
                 pr.hea-=a1
                 print(pr.name,'生命减少',a1)
     elif b==-2:
         if a>ft2*2:
             print('反弹失败')
             a1=round(a*mt.power,1)
             pr.hea-=a1
             print(pr.name,'生命减少',a1)
         else:
             print('反弹！')
             a1=round(a*pr.power,1)
             if '三途之骨' in mt.bag and mt.mon!=0:
                 if mt.mon>=a1:
                     mt.mon-=a1
                     a1=0
                     print('三途之骨效果发动,抵挡全部伤害')
                 else:
                     a1-=mt.mon
                     mt.mon=0
                     mt.hea-=a1
                     print('三途之骨效果发动,抵挡部分伤害')
                     print(mt.name,'生命减少',a1)
             else:
                 mt.hea-=a1
                 print(mt.name,'生命减少',a1)

             
def panding(mt,pr):
    if mt.hea<=0:
        return mt.name
    elif pr.hea<=0:
        return pr.name
    else:
        return False
def qianyan(mt,pr):
    print(mt.name,':','hp',round(mt.hea,1),'pow',round(mt.mon,2),'/',round(mt.mon_max,1))
    print(pr.name,':','hp',round(pr.hea,1),'pow',round(pr.mon,2),'/',round(pr.mon_max,1))

exp1=Object('玩家',False,mon=2,hea=30,mon_max=3,mon_speed=3,power=3)
exp2=Object('敌人',True,personality='dog',floor=4)

def fight(mt,pr):
    mt=copy.deepcopy(mt)
    os.system('cls')
    time=0
    print('你遇到的敌人是： ',pr.name)
    print()
    print('''输入索引：
    -2为反弹，蓄力消耗1
    -1为趴下，无法受到伤害 0为蓄力,超过蓄力极限则无法继续增加蓄力值
    1及以上为出拳，消耗相应的蓄力数''')
    while True:
        time+=1
        print('-----------')
        print('第%s回合'%time)

        if time%2==1 and '残破的花篮' in mt.bag:
            mt.power*=2
        elif time%2==0 and '残破的花篮' in mt.bag:
            mt.power/=2
            
        
        qianyan(mt,pr)

        p=panding(mt,pr) #判定行
        if p==False:
            pass
        else:
            if p==mt.name:
                print(pr.name,'胜利')
            else:
                print(mt.name,'胜利')
            return p
        chuli(mt,pr,time)
#fight(exp1,exp2)    

  
