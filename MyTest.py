import Mylib





# 3画木字
print("------------------------------------")
charstring_ori="干,工,弓,丌,及,孑,巾,久,口,廿,乞,彡,已"
mu_3new=Mylib.charStrtolist(charstring_ori)

# 字List转字类List
chinchar3mu=list()
for i in mu_3new:
    a1=Mylib.ChineseChar(i,3,"木","")
    chinchar3mu.append(a1)

# 打印字类List信息（含笔画，五行）
print("3画木字共："+str(len(mu_3new))+"个")
Mylib.printCharLlist(chinchar3mu)


# 5画火字
charstring_ori="丙,代,旦,叨,氐,叮,冬,叻,立,尥,令,另,奶,尼,奴,冉,他,它,田,仝,仗,召,只,左"
Huo_5new=Mylib.charStrtolist(charstring_ori)

# 字List转字类List
chinchar5huo=list()
for i in Huo_5new:
    a1=Mylib.ChineseChar(i,5,"火","")
    chinchar5huo.append(a1)

# 打印字类List信息（含笔画，五行）
print("5画火字共："+str(len(Huo_5new))+"个")
Mylib.printCharLlist(chinchar5huo)

# 3画木和5画火排列
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
    if  (mu3huo5.index(i)+1) % 20 == 0 and mu3huo5.index(i)>0:
        print(str(mu3huo5.index(i)+1)+":"+i)
    elif (mu3huo5.index(i)+1) != len(mu3huo5):
        print(str(mu3huo5.index(i)+1)+":"+i+",",end="")
    else:
        print(str(mu3huo5.index(i) + 1) + ":" + i, end="")

