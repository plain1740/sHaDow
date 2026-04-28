from os import listdir
class story():
    def __init__(self,name,subject,emotion,end,time):
        self.name=name
        self.path='txt\\'+name+'.txt'
        self.subject=subject
        self.emotion=emotion
        self.end=end
        self.time_start=time[0]
        self.time_end=time[1]
        self.t_c=time[2]
        self.l=[]
        self.su_name=[]
        for s1 in self.subject:
            self.su_name.append(s1.name)

class ob():
    def __init__(self,name,belong,b2=''):
        self.name=name
        m=open('object%s\\%s.txt'%(str(b2),belong+name)).readlines()
        self.pro=m[0]
        self.skill=m[1]
        self.extra=m[2:]
        self.l=[self.name,self.pro,self.skill,self.extra]
    def check(self):
         print(self.name,'属性:',self.pro)
         print(self.skill)
         for e in self.extra:
             print(e.strip())
         print()
def check_ob(x):
    for x1 in x:
        print(x1.name)
        for x2 in x1.subject:
            x2.check()
        print('----------------------')
s1_0=ob('布满刮痕的公交车卡','s1')
s1_1=ob('过去的日记','s1')
s1_2=ob('沾染泥土的书签','s1')
s1=story('main01存在的证明 Who',[s1_0,s1_1,s1_2],[],
    {'记住她':'negative','活下去':'positive'},['23:00','4:00','6h'])

s2=story('main02世界的漏洞 Why A',[],[],
    {'忽魂悸以魄动':'positive'},['19:00','23:00','4h'])
s2_a_0=ob('手写的地图','s2_a')
s2_a=story('main02世界的漏洞 Why A',[s2_a_0],[],
    {'忽魂悸以魄动':'positive'},['19:00','23:00','4h'])

s2_b_0=ob('《除我之外的世界》','s2_b')
s2_b=story('main02世界的漏洞 Why B',[s2_b_0],[],
    {'恍惊起而长嗟':'negative'},['19:00','23:00','4h'])



s3_0=ob('纸条','s3')
s3=story('main03逃脱的方法 How',[s3_0],[],
    {'曙光':'positive'},['15:00','19:00','4h'])

s4_a=story('main04 谜底 A',[],[],
    {},['??','??','??'])
s4_b=story('main04 谜底 B',[],[],
    {},['??','??','??'])


d1=story('daily01惬意的午后',[],[],{},['15:00','19:00','??'])
d2=story('daily02熟悉的黄昏',[],[],{},['19:00','23:00','??'])
d3=story('daily03独自的深夜',[],[],{},['23:00','4:00','??'])
d4=story('daily04时间线的混乱',[],[],{},['4:00','15:00','??'])

n1=story('daily01迷路的小孩',[],[],{},['??','??','??'])
n2=story('daily02瘫倒在地的魔法师',[],[],{},['??','??','??'])
n3=story('daily03公园长椅上的怪人',[],[],{},['??','??','??'])


e1_0=ob('《机械忍者2》典藏版','e1')
e1_1=ob('绮良的日记','e1')
e1_2=ob('热门游戏的通用秘籍','e1')
e1=story('偶遇的死宅女孩',[e1_0,e1_1,e1_2],['安逸的','无趣的'],
    {'琐碎与安逸':'positive','意外之喜':'positive','朋友？':'positive',
     '背驰而去':'negative'},['15:00','19:00','4h'])

e2_0=ob('光洁的大理石','e2')
e2_1=ob('金制的“法西斯”饰品','e2')
e2=story('徘徊的罗马人',[e2_0,e2_1],['盲目的'],
         {'盲目与莽撞':'negative','壁炉与沙发':'positive',
          '飘散在时间之中的问题':'positive'},
         ['19:00','23:00','4h'])

e2_a_0=ob('维苏威火山的余烬','e2_a')
e2_a=story('徘徊的罗马人a',[e2_a_0],[],
           {'遗失在岁月中的答案':'positive'},['19:00','23:00','4h'])
e2_b_0=ob('帝国之影','e2_b')
e2_b=story('徘徊的罗马人b',[e2_b_0],[],
           {'遗失在岁月中的答案':'positive'},['19:00','23:00','4h'])
e2_c=story('徘徊的罗马人c',[],['迷茫的'],
           {'遗失在岁月中的答案':'positive'},['19:00','23:00','4h'])


e3_0=ob('兰波的诗集','e3')
e3_1=ob('黑色的戒指','e3')
e3=story('小酒馆的外乡人',[e3_0,e3_1],['干渴的','振奋的','微醺的','乏味的'],
         {'节制和理智':'positive','炒饭，谢谢':'positive'
          ,'生活与啤酒':'negative','生活与诗':'negative',
          '诗和甘菊茶':'positive'},['23:00','4:00','6h'])

e4_0=ob('残破的花篮','e4')
e4_1=ob('她的白蔷薇','e4')
e4_2=ob('她的红蔷薇','e4')
e4_3=ob('她的信','e4')
e4=story('风与蔷薇',[e4_0,e4_1,e4_2,e4_3],['愧疚的'],
         {'“神经病”':'negative','一地狼藉':'positive',
          '垃圾分类':'negative','残风':'negative','信风':'positive'
          ,'她和他':'positive','狂风骤起':'negative'
          ,'玩笑':'positive','“冒失鬼”':'positive',},['15:00','19:00','4h'])

e5_0=ob('月华','e5')
e5_1=ob('兰狄索斯的稿纸','e5')
e5_2=ob('伊始','e5')
e5=story('兰狄索斯的夜',[e5_0,e5_1,e5_2],['惆怅的','惧怕的'],
          {'“夜色浓重”':'negative','夜色浓重':'positive',
          '无痕':'negative','自尽之人':'negative','下弦':'positive'
          ,'归途之中':'positive','星夜':'positive'},
         ['23:00','4:00','6h'])

e6_0=ob('金酒之杯','e6')
e6_1=ob('往昔','e6')
e6=story('旧时代的老妇人',[e6_0,e6_1],['恼怒的','平静的'],
          {'这片大地':'negative','这个人过分慎重':'positive',
          '转瞬即逝的幻影':'positive'},
         ['23:00','4:00','6h'])


s5=ob('sHaDow','s',2)

z_0=ob('《终末世界的残响》','z',2)
z_1=ob('闪耀星海的信标','z',2)
z_2=ob('远天旅人的追忆','z',2)
z_3=ob('旧友难觅','z',2)


n_21=ob('残局棋谱','n',3)

q_1=ob('已有裂纹的风铃','q',3)
q_7=ob('枯木拐杖','q',3)

n_0=ob('猫人哥伦布','n',2)
n_1=ob('蛋黄酱','n',2)
n_2=ob('精致的羽毛','n',2)
n_3=ob('蛋包饭','n',2)
h_25=[n_0,n_1,n_2,n_3]

n_4=ob('不知名的怀表','n',2)
n_20=ob('绿宝石胸针','n',2)
h_40=[n_4,n_20]

n_5=ob('邪王真眼','n',2)
n_6=ob('游戏代币','n',2)
n_7=ob('锈蚀的小刀','n',2)
p_20=[n_5,n_6,n_7]

n_8=ob('闪耀的偏方三八面体','n',2)
n_19=ob('奇怪的咒语','n',2)
p_40=[n_8,n_19]

n_9=ob('呱太面具','n',2)
n_10=ob('《理想》','n',2)
n_11=ob('《只有我不存在的城市》','n',2)
n_12=ob('石鬼面','n',2)
sa_20=[n_9,n_10,n_11,n_12]

n_18=ob('入教申请书','n',2)
s_1=[n_18]
n_13=ob('“无差别日记”','n',2)
s_2=[n_13]

n_14=ob('国际象棋的一颗棋子','n',2)
n_15=ob('一束头发','n',2)
n_16=ob('白笛','n',2)
n_17=ob('《冰菓》','n',2)


si=[n_14,n_15,n_16,n_17]





eo_dic={'雪落':'看不到地图轮廓(；′⌒`)','焕然':'让地图焕然一新╰(*°▽°*)╯',
        '空明':'可以看到无法行走的格子','暴雨':'地图中刷新新的敌人',
        '纠缠':'走固定步数会进行一次随机传送','脆弱':'遇到敌人直接战败',
        '忽视':'走过的路留下印记。再次踏上san数值减少',
        '漠视':'看不到敌人',
        '希冀':'理智获得加倍','犹豫':'混乱获得加倍',
        '雀跃':'让你热情高涨'}

extra=[z_0,z_1,z_2,z_3,q_1,q_7,s5]
extra+=[n_0,n_1,n_2,n_3,n_4,n_5,n_6,n_7,n_8,n_9,n_10,n_11,n_12,n_13,n_14,n_15,n_16,n_17,
n_18,n_19,n_20,n_21]

#fight_object=[n_0,n_1,n_2,n_3,n_4,n_5,n_6,n_7,n_8,n_13,n_18,n_19,n_20,n_21,q_1,q_2,q_6,q_7,q_12,q_13,q_14]#测试用

fight_object_total=[n_0,n_1,n_2,n_3,n_4,n_5,n_6,n_7,n_8,n_9,n_10,n_11,n_12,n_13,n_14,n_15,n_16,n_17,
n_18,n_19,n_20,n_21,q_1,q_7,z_0,z_1,z_2,z_3]

story_total=[s1,s2_a,s2_b,s3,e1,e2,e2_a,e2_b,e3,e4,e5,e6,#e7,
             d1,d2,d3,d4]
    
object_total={}
story_dic={}

for sd in story_total: #初始化story_dic
    story_dic[sd.name]=sd

for st in story_total:  #初始化object_total
    for st1 in st.subject:
        object_total[st1.name]=st1
for ex1 in extra:
    object_total[ex1.name]=ex1

episode15=[e1,e4]
episode19=[e2]
episode22=[e3,e5,e6]
emotion_story={'txt//emotion雪.txt':['雪落','焕然'],
               'txt//emotion雨后.txt':['空明','暴雨'],
               'txt//emotion缠绕.txt':['纠缠','脆弱'],
               'txt//emotion漠视.txt':['忽视','漠视'],
               'txt//emotion无需言说.txt':['希冀','犹豫']}
emotion_story2=list(emotion_story.keys())



time00={'15:00':'午后','19:00':'傍晚','23:00':'深夜','4:00':'拂晓'}




#check_ob(story_total)
#[ob.check() for ob in extra]
