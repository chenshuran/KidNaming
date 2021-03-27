# 字类
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


# 字串转List
def charStrtolist(str):
    charlist_temp=list(str)
    charlist_new=[]
    for i in charlist_temp:
        if not i in charlist_new:
            # 去掉逗号
            if i!=',':
                charlist_new.append(i)
    return charlist_new
# 打印字List（含笔画，五行）
def printCharLlist(list):
    for i in list:
        # info=i.zi+":"+"笔画"+str(i.bihua)+",五行:"+i.wuxing
        info = i.zi + "(" + str(i.bihua) + i.wuxing + ")"
        if list.index(i) + 1 != len(list):
            print(info + ",", end="")
        else:
            print(info)
print("------------------------------------")