#coding=utf-8
import Mylib
import random
import InitData

#数理81吉祥数
Goodfrom81=[1,3,5,6,7,8,11,13,15,16,17,18,21,23,24,25,29,30,31,32,33,35,37,38,39,41,45,47,48,51,52,57,58,61,63,65,67,68,71,73,75,77,78,81]



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

# 总格根据81数理取吉利
def GetNameByZonggeFromGood81(namelist):
    Myname=[]
    for i in namelist:
        if i.zongge in Goodfrom81:
           Myname.append(i)

    return Myname
# 人格根据81数理取吉利
def GetNameByRengeFromGood81(namelist):
    Myname = []
    for i in namelist:
        if i.renge in Goodfrom81:
            Myname.append(i)

    return Myname
# 地格根据81数理取吉利
def GetNameByDigeFromGood81(namelist):
    Myname = []
    for i in namelist:
        if i.renge in Goodfrom81:
            Myname.append(i)

    return Myname
# 三才配置取吉利
def GetNameBySancai(namelist):
    Myname = []
    for i in namelist:
        if( (i.renge % 10)== 5) or ( (i.renge % 10)== 6):
            if ( (i.dige % 10)== 3) or ( (i.dige % 10)== 4):
                Myname.append(i)
    return Myname




# 二字五行取名
# 木木名
def GetName_MuMU():
    print("--------- 木木组合名字 ---------")

    namelistfull = GetNameByChar(Mu_Set.fulllist, Mu_Set.fulllist)
    print("木木组合共：" + str(len(namelistfull)) + "个，其中")
    namelist_renge_by81=GetNameByRengeFromGood81(namelistfull)
    print("人格符合81数理名字：" + str(len(namelist_renge_by81)) + "个")
    # 打印，每行x个
    for i in namelist_renge_by81:
        if (namelist_renge_by81.index(i) + 1) % 10 != 0:
            print(
                "【" + i.givenname + "】" + "(" + str(i.bihua1) + "/" + str(i.bihua2) + ",人" + str(i.renge) + "),", end="")
        else:
            print(
                "【" + i.givenname + "】" + "(" + str(i.bihua1) + "/" + str(i.bihua2) + ",人" + str(i.renge) + "),")


    namelist_dige_by81=GetNameByDigeFromGood81(namelist_renge_by81)
    namelist_zongge_by81 = GetNameByZonggeFromGood81(namelist_dige_by81)
    namelist_sancai=GetNameBySancai(namelist_zongge_by81)



    # print("木木组合共：" + str(len(namelistfull)) + "个，其中：")
    # print("人格，地格，总格均符合81数理名字，且三才配置7/(5,6)/(3,4)：" + str(len(namelist_sancai)) + "个")
    #
    # # 打印，每行x个
    # for i in namelist_sancai:
    #     if (namelist_sancai.index(i) + 1) % 10 != 0:
    #         print("【"+i.givenname+"】" +"("+str(i.bihua1)+"/"+str(i.bihua2)+",人"+str(i.renge)+"/地"+str(i.dige)+"/总"+str(i.zongge)+",三才"+i.sancai+"),", end="")
    #     else:
    #         print("【"+i.givenname+"】" +"("+str(i.bihua1)+"/"+str(i.bihua2)+",人"+str(i.renge)+"/地"+str(i.dige)+"/总"+str(i.zongge)+",三才"+i.sancai+"),")



# 火木名
def GetName_HuoMu():
    print("--------- 火木组合名字 ---------")

    namelistfull = GetNameByChar(Huo_Set.fulllist, Mu_Set.fulllist)
    print("火木组合共：" + str(len(namelistfull)) + "个，其中")
    namelist_renge_by81 = GetNameByZonggeFromGood81(namelistfull)



    namelist_dige_by81 = GetNameByDigeFromGood81(namelist_renge_by81)
    namelist_zongge_by81 = GetNameByZonggeFromGood81(namelist_dige_by81)
    print("五格符合81数理名字：" + str(len(namelist_zongge_by81)) + "个")
    namelist_sancai = GetNameBySancai(namelist_zongge_by81)
    # print("三才配置后还剩：" + str(len(namelist_sancai)) + "个")
    print("人格，地格，总格均符合81数理名字，且三才配置7/(5,6)/(3,4)：" + str(len(namelist_sancai)) + "个")

    # 打印，每行x个
    for i in namelist_sancai:
        if (namelist_sancai.index(i) + 1) % 10 != 0:
            print("【"+i.givenname+"】" +"("+str(i.bihua1)+"/"+str(i.bihua2)+",人"+str(i.renge)+"/地"+str(i.dige)+"/总"+str(i.zongge)+",三才"+i.sancai+"),", end="")
        else:
            print("【"+i.givenname+"】" +"("+str(i.bihua1)+"/"+str(i.bihua2)+",人"+str(i.renge)+"/地"+str(i.dige)+"/总"+str(i.zongge)+",三才"+i.sancai+"),")


# 木火名
def GetName_MuHuo():
    print("--------- 木火组合名字 ---------")

    NamelistByMuHuo = GetNameByChar(Mu_Set.fulllist,Huo_Set.fulllist)
    # print()
    NamelistByMuHuoBy81 = GetNameByZonggeFromGood81(NamelistByMuHuo)
    print("木火组合共：" + str(len(NamelistByMuHuo)) + "个，" + "其中符合81数理名字：" + str(len(NamelistByMuHuoBy81)) + "个")
    # 顺序打印符合81数理的木木名字组合，每行50个
    for i in NamelistByMuHuoBy81:
        if (NamelistByMuHuoBy81.index(i) + 1) % 50 != 0:
            print(i.givenname + ",", end="")
        else:
            print(i.givenname)
# 火土名
def GetName_HuoTu():
    print("--------- 火土组合名字 ---------")

    NamelistByHuoTu = GetNameByChar(Huo_Set.fulllist, Tu_Set.fulllist)
    # print()
    NamelistByHuoTuBy81 = GetNameByZonggeFromGood81(NamelistByHuoTu)
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
    NamelistByTuHuoBy81 = GetNameByZonggeFromGood81(NamelistByTuHuo)
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
    NamelistByTuTuBy81 = GetNameByZonggeFromGood81(NamelistByTuTu)
    print("土土组合共：" + str(len(NamelistByTuTu)) + "个，" + "其中符合81数理名字：" + str(len(NamelistByTuTuBy81)) + "个")
    # # 顺序打印名字组合，每行50个
    # for i in NamelistByTuTuBy81:
    #     if (NamelistByTuTuBy81.index(i) + 1) % 50 != 0:
    #         print(i.givenname + ",", end="")
    #     else:
    #         print(i.givenname)




# GetName_MuMU()
GetName_HuoMu()
# GetName_MuHuo()
# GetName_HuoTu()
# GetName_TuHuo()
# GetName_TuTu()












