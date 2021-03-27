import Mylib


# 3画木字
charstring_ori="干,工,弓,丌,及,孑,巾,久,口,廿,乞,彡,已"
charstring_tmp=Mylib.charStrtolist(charstring_ori)
chinchar3mu= Mylib.printChineseCharlist(charstring_tmp,list(),3,"木","")

# 4画木字
charstring_ori="卞,丐,公,勾,介,今,斤,亢,孔,木,牛,亓,欠,犬,牙,元,月,匀"
charstring_tmp=Mylib.charStrtolist(charstring_ori)
chinchar4mu= Mylib.printChineseCharlist(charstring_tmp,list(),4,"木","")

# 5画木字
charstring_ori="本,尕,甘,功,古,瓜,宄,卉,加,甲,叫,句,巨,卡,可,叩,卯,巧,丘,囚,去,外,未,五,仡,玉,札"
charstring_tmp=Mylib.charStrtolist(charstring_ori)
chinchar5mu= Mylib.printChineseCharlist(charstring_tmp,list(),5,"木","")

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

# # 3画木和5画火排列
# mu3huo5=list()
# for i in chinchar3mu:
#     for j in chinchar5huo:
#         name=i.zi+j.zi
#         # print(name)
#         mu3huo5.append(name)
#         name=j.zi+i.zi
#         mu3huo5.append(name)
# print("木3画和火5画排列名字数共："+str(len(mu3huo5))+"个")
# for i in mu3huo5:
#     if  (mu3huo5.index(i)+1) % 20 == 0 and mu3huo5.index(i)>0:
#         print(str(mu3huo5.index(i)+1)+":"+i)
#     elif (mu3huo5.index(i)+1) != len(mu3huo5):
#         print(str(mu3huo5.index(i)+1)+":"+i+",",end="")
#     else:
#         print(str(mu3huo5.index(i) + 1) + ":" + i, end="")

