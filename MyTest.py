import Mylib
import CharStringOriginal


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
# charstring_ori="干,工,弓,丌,及,孑,巾,久,口,廿,乞,彡,已"
mu_3new=charStrtolist(charstring_ori_mu_3)

# 字List转字类List
chinchar3mu=list()
for i in mu_3new:
    a1=Mylib.ChineseChar(i,3,"木","")
    chinchar3mu.append(a1)

# 打印字类List信息（含笔画，五行）
print("3画木字共："+str(len(mu_3new))+"个")
printCharLlist(chinchar3mu)



print("------------------------------------")
charstring_ori="丙,代,旦,叨,氐,叮,冬,叻,立,尥,令,另,奶,尼,奴,冉,他,它,田,仝,仗,召,只,左"
Huo_5=list(charstring_ori)
# for a in mu_3:
# mu_3.remove('干')
Huo_5new=[]
for i in Huo_5:
    if not i in Huo_5new:
        if i!=',':
            Huo_5new.append(i)
print("5画火字共："+str(len(Huo_5new))+"个")
chinchar5huo=list()
for i in Huo_5new:
    a1=Mylib.ChineseChar(i,5,"火","")
    # print(a1.zi)
    # print(a1.bihua)
    # print(a1.wuxing)
    # print(a1.jixiong)
    chinchar5huo.append(a1)


for i in chinchar5huo:
    # info=i.zi+":"+"笔画"+str(i.bihua)+",五行:"+i.wuxing
    info = i.zi
    print(info+",",end="")

print("------------------------------------")
mu3huo5=list()


for i in chinchar3mu:
    for j in chinchar5huo:
        name=i.zi+j.zi
        # print(name)
        mu3huo5.append(name)
        name=j.zi+i.zi
        mu3huo5.append(name)
print("木3画和火5画排列名字数共："+str(len(mu3huo5))+"个")
for i in mu3huo5:
    if  (mu3huo5.index(i)+1) % 10 == 0 and mu3huo5.index(i)>0:
        print(str(mu3huo5.index(i)+1)+":"+i)
    elif (mu3huo5.index(i)+1) != len(mu3huo5):
        print(str(mu3huo5.index(i)+1)+":"+i+",",end="")
    else:
        print(str(mu3huo5.index(i) + 1) + ":" + i, end="")

