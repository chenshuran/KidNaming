#coding=utf-8
import Mylib
import random
import InitData

#数理81吉祥数
Goodfrom81=[1,3,5,11,13,15,16,21,23,24,25,29,31,32,33,35,37,39,41,45,47,48,52,57,65,67,68,82]
Finefrom81=[6,7,17,18,27,30,38,51,55,61,75]



# 初始化
# 创建木，火，土字集实例
Mu_Set=Mylib.ChineseCharSet()
Huo_Set=Mylib.ChineseCharSet()
Tu_Set=Mylib.ChineseCharSet()

Mu_Set=InitData.InitMuData(Mu_Set)
Huo_Set=InitData.InitHuoData(Huo_Set)
Tu_Set=InitData.InitTuData(Tu_Set)
print()
print("--------- 初始化完成 ------------")
print("木属性字："+str(len(Mu_Set.fulllist)))
print("火属性字："+str(len(Huo_Set.fulllist)))
print("土属性字："+str(len(Tu_Set.fulllist)))

print()
# 根据名字二字的五行排列，得出名字。
def GetNameByChar(Charfulllist1, Charfulllist2):
    # ChineseName类队列
    Namelist=list()

    FullList1=Charfulllist1
    FullList2=Charfulllist2
    for i in Charfulllist1:
        for j in Charfulllist2:
            # 创建名字类例
            Myname = Mylib.ChineseName()
            Myname.Setinfo(i.zi,i.bihua,i.wuxing,"",j.zi,j.bihua,j.wuxing,"")
            Namelist.append(Myname)
    #         print(Myname.givenname,end="")
    # print(str(len(Namelist)))
    return Namelist
# 根据81数理吉凶得出吉利名字
def GetNameByGood81(namelist):
    Myname=[]
    for i in namelist:
        if i.zongbihua in Goodfrom81:
           Myname.append(i)

    return Myname

# 二字五行取名
# 木木名
def GetName_MuMU():
    print("--------- 木木组合名字 ---------")

    NamelistByMuMu = GetNameByChar(Mu_Set.fulllist, Mu_Set.fulllist)
    # print()
    NamelistByMuMuBy81 = GetNameByGood81(NamelistByMuMu)
    print("木木组合共：" + str(len(NamelistByMuMu)) + "个，" + "其中符合81数理名字：" + str(len(NamelistByMuMuBy81)) + "个")
    # 顺序打印符合81数理的木木名字组合，每行50个
    # for i in NamelistByMuMuBy81:
    #     if (NamelistByMuMuBy81.index(i) + 1) % 50 != 0:
    #         print(i.givenname + ",", end="")
    #     else:
    #         print(i.givenname)
    # # 顺序打印全部木木名字组合，每行50个
    # for i in NamelistByMuMu:
    #     if (NamelistByMuMu.index(i)+1) % 50 != 0:
    #         print(i.givenname+",",end="")
    #     else:
    #         print(i.givenname)
# 火木名
def GetName_HuoMu():
    print("--------- 火木组合名字 ---------")

    NamelistByHuoMu = GetNameByChar(Huo_Set.fulllist, Mu_Set.fulllist)
    # print()
    NamelistByHuoMuBy81 = GetNameByGood81(NamelistByHuoMu)
    print("火木组合共：" + str(len(NamelistByHuoMu)) + "个，" + "其中符合81数理名字：" + str(len(NamelistByHuoMuBy81)) + "个")
    # # 顺序打印符合81数理的木木名字组合，每行50个
    # for i in NamelistByHuoMuBy81:
    #     if (NamelistByHuoMuBy81.index(i) + 1) % 50 != 0:
    #         print(i.givenname + ",", end="")
    #     else:
    #         print(i.givenname)
# 木火名
def GetName_MuHuo():
    print("--------- 木火组合名字 ---------")

    NamelistByMuHuo = GetNameByChar(Mu_Set.fulllist,Huo_Set.fulllist)
    # print()
    NamelistByMuHuoBy81 = GetNameByGood81(NamelistByMuHuo)
    print("木火组合共：" + str(len(NamelistByMuHuo)) + "个，" + "其中符合81数理名字：" + str(len(NamelistByMuHuoBy81)) + "个")
    # # 顺序打印符合81数理的木木名字组合，每行50个
    # for i in NamelistByMuHuoBy81:
    #     if (NamelistByMuHuoBy81.index(i) + 1) % 50 != 0:
    #         print(i.givenname + ",", end="")
    #     else:
    #         print(i.givenname)
# 火土名
def GetName_HuoTu():
    print("--------- 火土组合名字 ---------")

    NamelistByHuoTu = GetNameByChar(Huo_Set.fulllist, Tu_Set.fulllist)
    # print()
    NamelistByHuoTuBy81 = GetNameByGood81(NamelistByHuoTu)
    print("火土组合共：" + str(len(NamelistByHuoTu)) + "个，" + "其中符合81数理名字：" + str(len(NamelistByHuoTuBy81)) + "个")
    # # 顺序打印名字组合，每行50个
    # for i in NamelistByHuoTuBy81:
    #     if (NamelistByHuoTuBy81.index(i) + 1) % 50 != 0:
    #         print(i.givenname + ",", end="")
    #     else:
    #         print(i.givenname)
# 土火名
def GetName_TuHuo():
    print("--------- 土火组合名字 ---------")
    NamelistByTuHuo = GetNameByChar(Tu_Set.fulllist, Huo_Set.fulllist)
    # print()
    NamelistByTuHuoBy81 = GetNameByGood81(NamelistByTuHuo)
    print("土火组合共：" + str(len(NamelistByTuHuo)) + "个，" + "其中符合81数理名字：" + str(len(NamelistByTuHuoBy81)) + "个")
    # # 顺序打印名字组合，每行50个
    # for i in NamelistByTuHuoBy81:
    #     if (NamelistByTuHuoBy81.index(i) + 1) % 50 != 0:
    #         print(i.givenname + ",", end="")
    #     else:
    #         print(i.givenname)
# 土土名
def GetName_TuTu():
    print("--------- 土土组合名字 ---------")

    NamelistByTuTu = GetNameByChar(Tu_Set.fulllist, Tu_Set.fulllist)
    # print()
    NamelistByTuTuBy81 = GetNameByGood81(NamelistByTuTu)
    print("土土组合共：" + str(len(NamelistByTuTu)) + "个，" + "其中符合81数理名字：" + str(len(NamelistByTuTuBy81)) + "个")
    # # 顺序打印名字组合，每行50个
    # for i in NamelistByTuTuBy81:
    #     if (NamelistByTuTuBy81.index(i) + 1) % 50 != 0:
    #         print(i.givenname + ",", end="")
    #     else:
    #         print(i.givenname)




GetName_MuMU()
GetName_HuoMu()
GetName_MuHuo()
GetName_HuoTu()
GetName_TuHuo()
GetName_TuTu()












