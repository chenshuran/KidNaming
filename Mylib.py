# 定义字类
class ChineseChar():
    def __init__(self,zi,bihua,wuxing,jixiong):
        self.zi=zi
        self.bihua=bihua
        self.wuxing=wuxing
        self.jixiong=jixiong
    def showinfo(self):
        print("字",self.zi)
        print("笔画", self.bihua)
        print("五行", self.wuxing)
        print("吉凶", self.jixiong)

#定义字集类
#字集类包含：一个以笔画分组的队列字典dictbybihua，一个字全集队列fulllist)
class ChineseCharSet(object):
    def __init__(self):
        pass
    def Setinfo(self,dict,list):
        self.dictbybihua=dict
        self.fulllist=list

# 定义名字类
class ChineseName():
    def __init__(self):
        pass
    def Setinfo(self,zi1,bihua1,wuxing1,jixiong1,zi2,bihua2,wuxing2,jixiong2):
        self.zi1=zi1
        self.bihua1=bihua1
        self.wuxing1=wuxing1
        self.jixiong1=jixiong1
        self.zi2 = zi2
        self.bihua2 = bihua2
        self.wuxing2 = wuxing2
        self.jixiong2 = jixiong2
        self.name="陈"+zi1+zi2  #名
        self.zongbihua=16+bihua1+bihua2  #总笔画
        self.wuxingdapei="火"+wuxing1+wuxing2 #五行搭配
    def showinfo(self):
        print("名字",self.name)
        print("总笔画", self.zongbihua)
        print("五行", self.wuxingdapei)
        print("吉凶", self.jixiong)



# 字符串转字列表
def charStrtolist(str):
    charlist_temp=list(str)
    charlist_new=[]
    for i in charlist_temp:
        if not i in charlist_new:
            # 去掉逗号
            if i!=',':
                charlist_new.append(i)
    return charlist_new
# 打印字列表
def printCharList(list):
    for i in list:
        # info=i.zi+":"+"笔画"+str(i.bihua)+",五行:"+i.wuxing
        # info = i.zi + "(" + str(i.bihua) + i.wuxing + ")"
        info = str(list.index(i)+1)+":"+i.zi
        if list.index(i) + 1 != len(list):
            print(info + ",", end="")
        else:
            print(info)
    print("------------------------------------")
# 由字列表得到字类列表
def GetChineseCharlist(list_tmp, list, bihua, wuxing, jixiong):
    for i in list_tmp:
        a1 = ChineseChar(i, bihua, wuxing, jixiong)
        list.append(a1)
    print(str(bihua)+"画字共：" + str(len(list)) + "个")
    printCharList(list)
    # print("------------------------------------")
    return list