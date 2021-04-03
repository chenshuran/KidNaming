#coding=utf-8
import Mylib
import random

#数理81吉祥数
Goodfrom81=[1,3,5,6,7,11,13,15,16,21,23,24,29,31,32,33,35,37,41,45,47,48,52,57,61,63,65,67,68,81]

# 字集编号
# 1父亲初始字符集，大而全
# 2父亲03.26精简字符集
# 3父亲03.31精简字符集
# 4我的字符集
CharsetNum=1
# 根据编号选取一套字集
def getcharstringbynum(num,string01,string02,string03,string04):
    numbers = {
        1 : string01,
        2 : string02,
        3 : string03,
        4 : string04
    }
    return numbers.get(num, "无")



# 创建木，火，土字集实例
Mu_Set=Mylib.ChineseCharSet()
Huo_Set=Mylib.ChineseCharSet()
Tu_Set=Mylib.ChineseCharSet()

# 木，火，土字集初始化函数
def InitMuData(ChineseCharSet_Mu):
    # region 木字初始化
    Mu_Dict = {}
    MuFullList = list()
    # 3画木字
    charstring_ori = "干,工,弓,丌,及,孑,巾,久,口,廿,乞,彡,已"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar3mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 3, "木", "")
    Mu_Dict[3] = chinchar3mu
    MuFullList = MuFullList + chinchar3mu

    # 4画木字
    charstring_ori = "卞,丐,公,勾,介,今,斤,亢,孔,木,牛,亓,欠,犬,牙,元,月,匀"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar4mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 4, "木", "")
    Mu_Dict[4] = chinchar4mu
    MuFullList = MuFullList + chinchar4mu

    # 5画木字
    charstring_ori = "本,尕,甘,功,古,瓜,宄,卉,加,甲,叫,句,巨,卡,可,叩,卯,巧,丘,囚,去,外,未,五,仡,玉,札"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar5mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 5, "木", "")
    Mu_Dict[5] = chinchar5mu
    MuFullList = MuFullList + chinchar5mu

    # 6画木字
    charstring_ori = "朳,朵,尬,各,共,乩,吉,伎,奸,幵,囝,件,交,臼,伉,考,朽,旭,匡,夼,企,犰,曲,戎,仰,吁,聿,朱,竹"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar6mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 6, "木", "")
    Mu_Dict[6] = chinchar6mu
    MuFullList = MuFullList + chinchar6mu

    # 7画木字
    charstring_ori = "杓,材,岑,杈,床,村,杜,呃,伽,改,杆,杠,告,更,攻,估,谷,庋,呙,囯,旱,何,吼,肓,妓,忌,夹,见,角,疖,劫,妗,究,局,姖,君,佧,扛,囥,壳,克,扣,困,伲,你,杞,扦,羌,劬,却,杉,我,吴,吾,扤,杌,匣,吓,杏,言,吟,杖"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar7mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 7, "木", "")
    Mu_Dict[7] = chinchar7mu
    MuFullList = MuFullList + chinchar7mu

    # 8画木字
    charstring_ori = "昂,枊,板,杯,杵,东,妸,扼,枋,斧,秆,杲,疙,供,咕,姑,孤,固,呱,乖,官,果,杭,忽,昏,肌,亟,佶,技,季,佳,肩,艽,佼,届,卺,京,纠,赳,玖,疚,居,咀,具,卷,咔,咖,抗,肯,空,枕,枝,快,狂,林,枚,杪,艿,呢,杻,杷,枇,其,奇,歧,穹,虬,屈,券,枘,松,枉,卧,析,呷,欣,芎,厓,兖,杳,宜,竺,杼"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar8mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 8, "木", "")
    Mu_Dict[8] = chinchar8mu
    MuFullList = MuFullList + chinchar8mu

    # 9画木字
    charstring_ori = "柲,柄,柴,柢,芏,俄,枹,尜,肝,柑,竿,疳,肛,缸,纥,革,虼,哏,狗,枸,牯,故,冠,咣,皈,轨,癸,柜,哄,訇,虹,芨,咭,级,急,纪,既,枷,叚,架,建,牮,姜,姣,皆,界,疥,蚧,矜,劲,扃,九,韭,拘,狙,拒,军,看,柯,科,咳,客,芝,哐,柃,柳,咯,芒,怩,昵,拈,柈,芃,枰,祈,芑,契,恰,芊,俏,俅,酋,畎,芍,柿,柁,柝,芄,玩,侠,狎,柙,相,枵,彦,奕,弈,疫,羿,胤,柚,禺,竽,芋,栅,柘,枳,柱,斫,柞"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar9mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 9, "木", "")
    Mu_Dict[9] = chinchar9mu
    MuFullList = MuFullList + chinchar9mu

    # 10画木字
    charstring_ori = "桉,芭,笆,柏,栢,梆,苄,栟,屙,婀,苊,芳,芬,粉,芙,酐,绀,羔,高,哥,格,鬲,哿,根,耕,哽,肱,恭,蚣,躬,拱,贡,股,骨,罟,挂,倌,桄,鬼,桂,衮,核,桁,讧,笏,花,桓,恢,唧,姬,屐,笄,笈,脊,记,珈,家,痂,恝,兼,豇,狡,讦,拮,桀,芥,衿,肼,弪,径,柩,桕,疽,桔,俱,倨,娟,倦,桊,隽,拷,栲,珂,疴,恪,倥,恐,芤,栩,祗,哭,库,框,括,栝,栳,栗,匿,臬,耙,芘,栖,芪,耆,岂,起,气,虔,肷,芡,衾,芩,芹,祛,拳,缺,桑,芟,秫,栓,凇,笋,桃,桐,砼,桅,芴,奚,哮,校,芯,桠,芽,芫,唁,苡,倚,痈,邕,娱,圄,峪,原,纭,芸,笊,芷,桎,株,桌"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar10mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 10, "木", "")
    Mu_Dict[10] = chinchar10mu
    MuFullList = MuFullList + chinchar10mu

    # 11画木字
    charstring_ori = "茇,苞,苯,笨,苾,梐,彬,梣,茬,趁,笞,茌,崔,笪,笛,兜,轭,梵,苻,桴,符,苷,敢,舸,梗,珙,苟,笱,蛄,梏,牿,胍,规,匦,国,悍,捍,偈,寄,笳,袈,戛,蛱,胛,徦,假,坚,枧,趼,健,皎,教,秸,婕,堇,近,婧,竟,救,苴,趄,苣,捐,眷,桷,捃,胩,康,苛,氪,啃,寇,许,苦,眶,悝,盔,悃,捆,梱,婪,笠,啉,苓,茅,茆,茂,梅,苠,茉,苜,旎,偶,苤,笸,启,弃,乾,悄,茄,卿,顷,筇,蚯,区,蛆,朐,娶,悛,圈,痊,苒,若,啬,苫,梢,苕,笙,倏,梳,术,笥,桫,梭,苔,梯,笤,梃,桶,偓,梧,悟,晤,狭,厢,枭,偕,械,研,厣,眼,悒,挹,翊,茚,英,唷,圉,庾,苑,笮,苎,棁,茁,梓"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar11mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 11, "木", "")
    Mu_Dict[11] = chinchar11mu
    MuFullList = MuFullList + chinchar11mu

    # 12画木字
    charstring_ori = "棒,笔,草,策,茶,枨,茺,楮,篅,荈,棰,茈,茨,答,等,第,棣,迭,栋,筏,棼,茯,尴,皋,胳,袼,给,茛,轱,觚,酤,诂,雇,棺,贯,胱,晷,贵,棍,聒,椁,皓,闳,喉,荒,茴,嵇,极,戢,棘,殛,集,几,掎,悸,迦,袷,跏,间,犍,荐,绛,茭,椒,蛟,绞,窖,喈,街,杰,结,筋,荩,阱,景,痉,窘,啾,厩,掬,椐,莒,讵,距,犋,掘,珺,喀,开,凯,闶,钪,轲,棵,控,椋,植,筐,贶,傀,喟,蛞,棱,荔,络,荦,荬,棉,茗,猊,棚,椑,期,欺,祁,棋,掐,掮,茜,嵌,强,羟,乔,邱,球,诎,蛐,荃,筌,荏,茸,茹,阮,森,筛,耜,覃,棠,茼,统,筒,椭,皖,稀,厦,筅,荇,悻,荀,雅,掩,雁,尧,傜,荑,椅,茵,硬,哟,驭,饫,寓,栈,棹,茱,椎,棕,最"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar12mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 12, "木", "")
    Mu_Dict[12] = chinchar12mu
    MuFullList = MuFullList + chinchar12mu

    # 13画木字
    charstring_ori = "嗄,荸,箅,筴,搽,猹,槎,茝,椿,榱,戥,荻,椴,莪,蛾,愕,枫,莩,该,陔,赅,戤,概,感,幹,筻,嗝,塥,跟,绠,诟,彀,痼,诖,琯,诡,跪,嗬,荷,猴,逅,畸,嫉,楫,麂,荚,嫁,拣,笕,减,楗,毽,酱,郊,跤,脚,敫,揭,诘,睫,解,仅,禁,靳,经,茎,睛,胫,敬,迥,揪,舅,琚,雎,榉,绢,筠,揩,慨,楷,戡,莰,稞,窠,嗑,筘,廉,楝,窟,夸,蒯,诓,揆,暌,琨,髡,廓,莨,楞,莉,莅,琳,莽,莓"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar13mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 13, "木", "")
    Mu_Dict[13] = chinchar13mu
    MuFullList = MuFullList + chinchar13mu

    # 14画木字
    charstring_ori = "菝,榜,菢,菶,萆,菜,菖,苌,尝,篪,椽,菙,萃,萏,菪,凳,摁,菲,榧,菔,嘎,盖,赶,纲,睾,膏,搞,槁,诰,郜,歌,搿,箇,郠,构,菇,菰,箍,鼓,褂,管,逛,绲,帼,蜾,菡,赫,瘊,槐,萑,夥,箕,暨,跽,嘉,郏,瘕,笺,菅,搛,戬,僭,降,僬,侥,饺,酵,截,竭,诫,骱,紧,廑,菁,腈,兢,僦,裾,菊,矩,皲,菌,郡,忾,犒,裉,箜,榛,筝,骷,酷,筷,魁,睽,匮,愧,莱,榔,菱,榴,杩,樠,萌,墓,幕,萘,箄,裴,菩,桤,萋,嘁,萁,旗,綦,绮,葺,搴,歉,枪,敲,侨,诮,箧,轻,箐,逑,赇,巯,蜷,绻,榷,荣,榕,箬,瑟,菽,槊,菘,算,榫,榻,萄,萜,菟,菀,伪,萎,菥,箫,榍,榭,菸,厌,酽,疑,瘗,蜴,萤,郢,萸,语,妪,箢,瑗,愿,菑,榨,寨,肇,菹"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar14mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 14, "木", "")
    Mu_Dict[14] = chinchar14mu
    MuFullList = MuFullList + chinchar14mu

    # 15画木字
    charstring_ori = "葆,萹,箯,标,槽,箣,郴,樗,枞,稻,噔,蒂,腭,樊,葑,橄,稿,葛,赓,巩,穀,广,妫,瑰,郭,掴,荭,篌,糇,葫,槲,篁,蝗,叽,缉,赍,稽,瘠,挤,稷,葭,价,驾,稼,俭,翦,贱,腱,箭,僵,桨,娇,胶,噍,颉,羯,槿,儆,獍,阄,樛,驹,踞,蒈,慷,靠,颏,瞌,蝌,课,缂,抠,萱,箴,侉,侩,宽,款,诳,葵,醌,阃,楼,面,模,耦,葩,篇,葡,槭,葜,悭,椠,庆,穷,茕,萩,蝤,葚,枢,樘,葶,葳,苇,蒍,妩,葸,瞎,贤,缃,葙,箱,蝎,样,仪,谊,毅,莹,媵,窳,葬,樟,荮,著,箸,醉"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar15mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 15, "木", "")
    Mu_Dict[15] = chinchar15mu
    MuFullList = MuFullList + chinchar15mu

    # 16画木字
    charstring_ori = "蓓,荜,筚,蓖,篦,蔀,篰,苍,橙,篘,莼,笃,饿,谔,鄂,阏,萼,遏,噩,蒽,篚,噶,篙,糕,缟,膈,骼,鸪,毂,掼,龟,辊,过,蒿,嚆,横,黉,骺,鲎,桦,慌,隍,荤,机,畿,墼,蒺,剂,冀,髻,颊,缣,蒹,谏,踺,彊,耩,犟,挢,徼,缙,噤,颈,憬,橘,举,踽,窭,鄄,橛,麇,瞰,眍,篥,蓄,蓁,蒸,裤,哙,窥,愦,梦,蒲,朴,器,褰,黔,橇,桥,憔,樵,撬,鞘,亲,擒,檎,螓,檠,磬,遒,鼽,糗,趋,鸲,磲,桡,蓉,蓐,穑,树,蒴,蒜,荪,蓑,蓊,樨,县,橡,筱,啸,谐,阎,谚,窑,缢,荫,萦,蓥,嬴,颖,阈,遇,圜,樾,筑,篆,嘴,樽"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar16mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 16, "木", "")
    Mu_Dict[16] = chinchar16mu
    MuFullList = MuFullList + chinchar16mu

    # 17画木字
    charstring_ori = "蒡,蔽,檦,檗,蔡,柽,苁,葱,蔟,簇,档,瞪,懂,蔸,篼,擀,鸽,篝,购,媾,鸹,馆,簋,蝈,馘,癀,桧,豁,击,玑,激,哜,觊,艰,鞯,捡,检,謇,讲,蒋,鲛,矫,阶,鲒,鞠,鞫,据,飓,糠,颗,髁,恳,莲,联,敛,蓼,蓿,蔻,挎,狯,亏,栏,檑,檩,蒌,篓,簏,蔓,懋,甍,蔑,篾,茑,蓬,蹊,谦,瞧,擎,罄,蕖,阒,篸,蔌,簌,檀,蔚,檄,蓰,辖,罅,芗,魈,蔫,檐,营,狱,岳,箦,蔗,栉,赚,桩"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar17mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 17, "木", "")
    Mu_Dict[17] = chinchar17mu
    MuFullList = MuFullList + chinchar17mu

    # 18画木字
    charstring_ori = "槟,檫,蒇,槌,箪,簦,簟,蕫,鹅,额,颚,蕃,搁,隔,鲠,遘,觏,鹄,瞽,归,鲧,簧,蟥,蕙,获,犄,蕺,虮,鲫,鲣,睑,裥,简,谫,槛,糨,蕉,谨,觐,旧,屦,瞿,鹃,蕨,骒,蒉,篑,聩,拦,瞢,拟,腻,柠,骐,骑,荨,襁,鄡,荞,窍,翘,苘,躯,璩,觑,鬈,荛,绕,蕤,蕊,蔬,梼,檮,隗,魏,芜,黠,蕈,颜,蝇,鹆,蜮,簪,蕞"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar18mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 18, "木", "")
    Mu_Dict[18] = chinchar18mu
    MuFullList = MuFullList + chinchar18mu

    # 19画木字
    charstring_ori = "薜,簸,橱,薋,蹬,椟,臌,关,犷,薅,薨,蕻,谎,荟,讥,蓟,缰,缴,轿,醮,襟,馑,鲸,鬏,绔,胯,脍,旷,鲲,扩,蕾,枥,栎,橹,麓,难,鲵,攀,麒,髂,签,蔷,跷,缲,黢,醛,萨,薯,薇,蕹,萧,肖,撷,薤,蟹,薪,薛,赝,遗,蚁,薏,蓣,籀"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar19mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 19, "木", "")
    Mu_Dict[19] = chinchar19mu
    MuFullList = MuFullList + chinchar19mu

    # 20画木字
    charstring_ori = "藊,藏,榇,筹,篡,鹗,鳄,藁,鳇,攉,蠖,籍,继,舰,藉,警,竞,龃,遽,醵,觉,阚,悬,喾,跨,郐,纩,馈,蓝,篮,栊,栌,檬,藐,篷,脐,蛴,荠,骞,琼,鳅,劝,薷,薹,牺,献,薰,严,邀,议,橼,黦,槠,橥,纂"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar20mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 20, "木", "")
    Mu_Dict[20] = chinchar20mu
    MuFullList = MuFullList + chinchar20mu

    # 21画木字
    charstring_ori = "藨,鹘,顾,鳏,颢,饥,鸡,歼,鹣,茧,赆,夔,藜,藕,鞒,驱,饶,薮,藤,嚣,药,艺,龈,莺,樱"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar21mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 21, "木", "")
    Mu_Dict[21] = chinchar21mu
    MuFullList = MuFullList + chinchar21mu

    # 22画木字
    charstring_ori = "蔼,龚,瓘,蘅,骄,惧,鱇,邝,籁,苈,蔺,茏,笼,芦,蘑,孽,苹,蕲,氍,权,苏,俨,瘿,龉,鬻,蕴"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar22mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 22, "木", "")
    Mu_Dict[22] = chinchar22mu
    MuFullList = MuFullList + chinchar22mu

    # 23画木字
    charstring_ori = "蘩,蛊,鳜,藿,鹪,惊,鹫,蠲,蔹,兰,椤,蓦,蘖,蘧,癯,藓,鼹,验,驿"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar23mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 23, "木", "")
    Mu_Dict[23] = chinchar23mu
    MuFullList = MuFullList + chinchar23mu

    # 24画木字
    charstring_ori = "霭,簖,赣,羁,搅,蓠,篱,酿,衢,龋,魇,鹰,攥"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar24mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 24, "木", "")
    Mu_Dict[24] = chinchar24mu
    MuFullList = MuFullList + chinchar24mu

    # 25画木字
    charstring_ori = "观,鲚,髋,榄,萝,箩,蘸,缵"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar25mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 25, "木", "")
    Mu_Dict[25] = chinchar25mu
    MuFullList = MuFullList + chinchar25mu

    # 26画木字
    charstring_ori = "蠼,躜"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar26mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 26, "木", "")
    Mu_Dict[26] = chinchar26mu
    MuFullList = MuFullList + chinchar26mu

    # 27画木字
    charstring_ori = "颧,谳"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar27mu = Mylib.GetChineseCharlist(charstring_tmp, list(), 27, "木", "")
    Mu_Dict[27] = chinchar27mu
    MuFullList = MuFullList + chinchar27mu

    # endregion
    ChineseCharSet_Mu.dictbybihua = Mu_Dict
    ChineseCharSet_Mu.fulllist = MuFullList
    return ChineseCharSet_Mu
def InitHuoData(ChineseCharSet_Huo):
    # region 火字初始化
    Huo_Dict = {}
    HuoFullList = list()

    # # 2画火字
    # charstring_01="刁,丁,二,力,了"
    # charstring_02="刁,丁,二,力,了"
    # charstring_03=""
    # charstring_04=""
    # charstring_ori=getcharstringbynum(CharsetNum,charstring_01,charstring_02,charstring_03,charstring_04)
    #
    # charstring_tmp = Mylib.charStrtolist(charstring_ori)
    # chinchar2huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 2, "火", "")
    # Huo_Dict[2] = chinchar2huo
    # HuoFullList = HuoFullList + chinchar2huo

    # 3画火字
    charstring_01="彳,大,孓,女,勺,巳,乇,幺,弋,丈"
    charstring_02="大,勺"
    charstring_03 = "大,勺"
    charstring_04=""

    charstring_ori = getcharstringbynum(CharsetNum, charstring_01, charstring_02, charstring_03,charstring_04)

    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar3huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 3, "火", "")
    Huo_Dict[3] = chinchar3huo
    HuoFullList = HuoFullList + chinchar3huo

    # 4画火字
    # line1-原始集 / line2-3.26简化集合 / line3-3.31 简化集合 / lin4-抒然简化集合
    charstring_01 = "尺,丹,吊,仃,斗,火,井,支,仂,内,日,太,天,屯,午,爻,仉,止,中,之"
    charstring_02 = "尺,丹,仃,斗,火,支,内,太,天,止,中,之"
    charstring_03 = "尺,丹,仃,斗,火,支,内,太,天,止,中,之"
    charstring_04=""

    charstring_ori = getcharstringbynum(CharsetNum, charstring_01, charstring_02, charstring_03, charstring_04)

    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar4huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 4, "火", "")
    Huo_Dict[4] = chinchar4huo
    HuoFullList = HuoFullList + chinchar4huo

    # 5画火字
    # charstring_ori = "丙,代,旦,叨,氐,叮,冬,叻,立,尥,令,另,奶,尼,奴,冉,他,它,田,仝,仗,召,只,左"
    charstring_ori = "代,旦,叮,冬,立,令,另,冉,田,仗,召,左"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar5huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 5, "火", "")
    Huo_Dict[5] = chinchar5huo
    HuoFullList = HuoFullList + chinchar5huo

    # 6画火字
    # charstring_ori = "吃,弛,打,忉,氘,多,耳,旮,亘,光,尖,匠,她,决,旯,老,耒,劣,六,甪,氖,囡,年,乓,全,肉,同,氽,佤,妄,吆,宅,兆,旨,至,仲,自"
    charstring_ori = "多,亘,光,匠,六,年,全,同,兆,至,仲,自"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar6huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 6, "火", "")
    Huo_Dict[6] = chinchar6huo
    HuoFullList = HuoFullList + chinchar6huo

    # 7画火字
    # charstring_ori = "犴,呈,辵,呔,甙,但,低,弟,佃,甸,玎,疔,盯,豆,囤,旰,灸,良,牢,李,利,吝,伶,吕,卵,免,男,呐,佞,弄,努,求,忐,忑,町,廷,佟,彤,吞,托,佗,妥,巫,妖,佁,佔,志,豸,住,灼,姊,足"
    charstring_ori = "良,利,伶,免,努,求,廷,彤,托,妥,佔,志,住,灼,足"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar7huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 7, "火", "")
    Huo_Dict[7] = chinchar7huo
    HuoFullList = HuoFullList + chinchar7huo

    # 8画火字
    # charstring_ori = "哎,佰,长,炒,坼,侈,炊,佽,徂,耷,妲,沓,岱,宕,到,的,狄,底,玓,典,店,耵,定,咚,侗,抖,妒,咄,剁,佴,昉,炅,昊,戽,姐,咎,抉,炕,两,争,政,知,直,昆,剌,来,佬,肋,例,戾,冽,囹,呤,侣,仑,旻,奈,呶,妮,念,弩,疟,妾,炔,乳,侍,帑,弢,忝,佻,帖,投,罔,昕,炎,佯,易,找,制,帙,炙,忠,隹,卓"
    charstring_ori="佰,长,狄,底,宕,到,典,定,抖,炅,昊,攸,争,枕,知,直,昆,炎,易,制,忠,佳,卓"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar8huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 8, "火", "")
    Huo_Dict[8] = chinchar8huo
    HuoFullList = HuoFullList + chinchar8huo

    # 9画火字
    # charstring_ori = "炳,抶,抽,怛,待,怠,殆,眈,抵,帝,酊,订,段,祋,盹,盾,哆,哚,赴,拐,曷,烀,咴,姞,柬,炯,玦,俊,怜,亮,拉,厘,俚,俐,咧,拎,律,哪,娜,柰,耐,南,怒,虐,炮,炱,泰,炭,畋,殄,亭,突,凃,拖,拓,歪,纨,肟,炫,紃,殃,徉,咬,映,昱,怨,灾,炸,招,昭,者,贞,祉,致,盅,重,纣,胄,炷,籽,秭,耔,奏"
    charstring_ori="待,抵,段,赴,柬,俊,亮,俐,律,娜,耐,南,泰,亭,昱,招,者,致,胄,炷,籽,奏"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar9huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 9, "火", "")
    Huo_Dict[9] = chinchar9huo
    HuoFullList = HuoFullList + chinchar9huo

    # 10画火字
    # charstring_ori = "玳,耽,疸,紞,岛,倒,娣,玷,爹,瓞,冻,恫,蚪,趸,耿,烘,恍,疾,晋,珏,倔,烤,俩,凉,畜,烜,朕,肢,值,朗,烙,哩,娌,料,烈,玲,瓴,凌,留,旅,伦,倮,耄,拿,纳,肭,衲,孬,能,娘,恧,衄,哦,秦,恁,朊,芮,蚋,偌,晒,晌,恕,朔,趿,肽,唐,倘,讨,套,特,疼,屉,倜,恬,甜,挑,条,庭,挺,徒,彖,庹,挖,挝,倭,乌,娭,夏,讯,迅,秧,烊,窈,舀,旃,展,站,珍,秩,舯,衷,冢,祝,倬,笫,恣,哲"
    charstring_ori="耿,恍,晋,倔,值,玲,凌,留,旅,伦,能,泰,芮,特,恬,庭,挺,夏,讯,迅,秧,哲"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar10huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 10, "火", "")
    Huo_Dict[10] = chinchar10huo
    HuoFullList = HuoFullList + chinchar10huo

    # 11画火字
    # charstring_ori = "欸,捭,蛃,晡,眵,敕,从,凑,绐,带,袋,聃,胆,啖,蛋,盗,羝,顶,啶,动,敚,舵,阨,珥,烽,晗,焓,焊,斛,将,狷,诀,觖,梁,聊,振,执,徕,狼,勒,梨,狸,猁,唳,粒,羚,翎,聆,蛉,娄,卤,鹿,略,囵,捋,珞,那,婥,讷,您,胬,戚,软,晟,胎,酞,贪,袒,啕,剔,悌,粜,烃,停,珽,屠,豚,唾,娲,袜,烷,挽,焐,晞,烯,珣,珧,斩,张,章,帐,啁,侦,痔,窒,舳,捉,啄,眦,偬"
    charstring_ori="从,凑,给,带,袋,顶,舵,烽,振,聊,执"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar11huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 11, "火", "")
    Huo_Dict[11] = chinchar11huo
    HuoFullList = HuoFullList + chinchar11huo

    # 12画火字
    # charstring_ori = "掰,焙,采,场,焯,掣,程,塍,嗒,傣,贷,单,氮,悼,登,迪,觌,诋,邸,睇,掂,阽,惦,跌,喋,耋,痘,短,惇,敦,掇,迩,焚,钬,焦,接,嗟,晶,就,厥,吭,詈,晾,量,欻,诊,轸,证,焜,啦,喇,琅,稂,劳,犁,喱,理,傈,痢,捩,裂,趔,琉,硫,虏,掠,抡,捺,喃,赧,捻,傩,晴,闰,婼,邰,毯,探,掏,啼,腆,掭,祧,迢,贴,婷,痛,饨,跎,酡,惋,惘,喔,窝,幄,寻,循,巽,焱,蛘,轺,轶,媛,蛰,彘,智,痣,轴,粢"
    charstring_ori="掰,焙,采,场,程,单,登,迪,敦,焦,接,晶,理,铁,媛,智,轴"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar12huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 12, "火", "")
    Huo_Dict[12] = chinchar12huo
    HuoFullList = HuoFullList + chinchar12huo

    # 13画火字
    # charstring_ori = "稗,煲,煏,煸,裎,嗤,媸,驰,传,搭,靼,迨,亶,当,砀,嗲,电,殿,揲,牒,鼎,督,煅,顿,躲,惰,跺,烦,觥,煳,焕,煌,晃,幌,诙,迹,煎,炼,煊,睐,啷,廊,酪,诔,傫,愣,蜊,里,赁,零,旒,偻,赂,辂,琭,禄,路,乱,煤,睦,乃,恼,农,暖,逄,稔,塔,痰,逃,绨,提,跳,蜓,艇,退,煺,蜕,脱,驮,陀,顽,脘,畹,煨,炜,蜗,熄,烟,琰,扬,旸,炀,徭,虞,煜,詹,盏,照,罩,蜇,郅,置,雉,追,惴,琢,赀,觜,趑,訾"
    charstring_ori="驰,传,搭,当,鼎,督,煌,煌,幌,迹,炼,路,农,暖,提,烟,扬,照,琢"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar13huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 13, "火", "")
    Huo_Dict[13] = chinchar13huo
    HuoFullList = HuoFullList + chinchar13huo

    # 14画火字
    # charstring_ori = "熬,畅,尘,逞,瞅,绰,瘩,捣,嘀,嫡,递,腚,胨,郖,逗,端,对,裰,夺,尔,裹,伙,奖,尽,恺,奁,连,踉,僚,寥,廖,瘌,辣,罱,郎,嫪,嫘,酹,嘞,嫠,粼,绫,领,熘,绺,喽,陋,绿,纶,裸,雒,瑙,嫩,宁,喏,搦,炝,熔,煽,裳,台,态,叹,搪,耥,趟,慆,慝,滕,逖,惕,裼,舔,蜩,通,透,图,团,箨,蜿,绾,腕,诶,鞅,疡,摇,荧,毓,搌,绽,嫜,彰,胀,幛,赵,这,祯,种,逐,缀,缁"
    charstring_ori="畅,尘,逞,瞅,绰,端,尔,伙,连,僚,寥,郎,领,缘,宁,熔,煽,裳,台,态,搪,趟,通鞅,荧,绽,彰,种,逐"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar14huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 14, "火", "")
    Huo_Dict[14] = chinchar14huo
    HuoFullList = HuoFullList + chinchar14huo

    # 15画火字
    # charstring_ori = "皑,僾,熛,噌,层,彻,踟,齿,憏,憃,除,褚,踔,逴,辍,腠,褡,逮,儋,弹,德,敌,骶,缔,踮,调,蝶,董,陡,缎,饵,缓,践,瑾,进,噘,练,谅,辆,嘹,寮,阵,鸩,征,诤,赉,阆,唠,乐,黎,厉,撂,刘,瘤,搂,鲁,逯,戮,虑,轮,论,脶,骆,熳,鼐,腩,蝻,脑"
    charstring_ori="层,彻,瑾,进,练,谅,阵,征,诤,黎,历,论,侬,瑶"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar15huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 15, "火", "")
    Huo_Dict[15] = chinchar15huo
    HuoFullList = HuoFullList + chinchar15huo

    # 16画火字
    # charstring_ori = "撤,陈,撑,鸱,炽,俦,辏,达,殚,掸,惮,导,道,灯,谛,谍,蹀,都,赌,憝,吨,炖,遁,踱,燔,积,撅,獗,琏,撩,獠,燎,璇,臻,赖,褴,螂,捞,擂,缡,璃,罹,历,廪,陵,遛,龙,瘘,卢,陆,录,焖,挠,鲇,哝,诺,逎,燃,烧,燊,遂,鲐,昙,糖,螗,绦,陶,蹄,醍,头,暾,鸵,橐,熹,晓,谑,焰,鸯,晔,燚,燠,璋,瘴,踵,猪,撰,赘,谘,髭"
    charstring_ori="达,掸,导,道,积,琏,璇,臻,擂,历,龙,录,诺,燃,晓,晔媛,壁,惯,衡,恳,融,燕,余,豫,鸳,运,酝"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar16huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 16, "火", "")
    Huo_Dict[16] = chinchar16huo
    HuoFullList = HuoFullList + chinchar16huo

    # 17画火字
    # charstring_ori = "暧,餲,灿,龀,瞠,骋,丑,黛,担,瘅,挡,蹈,队,鸸,鲕,烩,绩,琎,爵,裢,殓,魉,疗,阑,痨,缧,儡,励,隶,临,瞵,磷,懔,隆,耧,蝼,缕,螺,麋,缪,黏,咛,騃,燧,遢,蹋,饧,膛,螳,醣,誊,嚏,瞳,疃,臀,襄,燮,谣,遥,繇,燥,择,辗,蟑,褶,鸷,膣,螽,烛,纵"
    charstring_ori="暖,灿,骋黛,挡,蹈,队,绩,励,隶,临,瞵,磷,隆,瞳,遥,择,纵"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar17huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 17, "火", "")
    Huo_Dict[17] = chinchar17huo
    HuoFullList = HuoFullList + chinchar17huo

    # 18画火字
    # charstring_ori = "痴,虫,戳,丛,戴,焘,鞮,癜,断,怼,丰,烬,粮,缭,职,醪,耢,釐,礼,鲤,膦,噜,辘,璐,谬,蛲,耨,懦,适,曙,抬,鹈,题,阗,餮,魍,曛,曜,烨,瞻,障,遮,谪,贽,掷,踬,转,骓,擢"
    charstring_ori="丛,焘,丰,职,题,烨,障,掷,转"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar18huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 18, "火", "")
    Huo_Dict[18] = chinchar18huo
    HuoFullList = HuoFullList + chinchar18huo

    # 19画火字
    # charstring_ori = "薆,摆,爆,蹭,嘲,蛏,歠,骴,哒,裆,邓,鲷,鸫,胴,蹲,齑,际,谲,蹶,帘,臁,蠊,脸,裣,辽,郑,羸,类,离,丽,呖,邻,遴,辚,鲮,馏,咙,撸,庐,氇,蠃,蟆,撵,脓,庞,曝,蹻,烁,谭,韬,鼗,玺,鄩,绎,赠,鄣,辙,骘,鲻"
    charstring_ori="摆,爆,蹭,际,丽,离,邻,庞,烁,韬,绎,赠"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar19huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 19, "火", "")
    Huo_Dict[19] = chinchar19huo
    HuoFullList = HuoFullList + chinchar19huo

    # 20画火字
    # charstring_ori = "宝,阐,郸,党,鲽,窦,嚼,矍,懒,黧,醴,疠,龄,骝,胧,拢,炉,掳,罗,糯,飘,赡,獭,挞,腾,龆,鼍,曦,耀,赢,躅"
    charstring_ori="宝,龄,拢,炉,飘,腾,耀"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar20huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 20, "火", "")
    Huo_Dict[20] = chinchar20huo
    HuoFullList = HuoFullList + chinchar20huo

    # 21画火字
    # charstring_ori = "缠,踌,跻,爝,腊,蜡,癞,斓,览,烂,累,俪,疬,珑,髅,骡,曩,鳎,鲦,鳐,鹞,灶,啭,馔,龇"
    charstring_ori="火,缠,踌,览,俪,珑"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar21huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 21, "火", "")
    Huo_Dict[21] = chinchar21huo
    HuoFullList = HuoFullList + chinchar21huo

    # 22画火字
    # charstring_ori = "颤,龊,籴,叠,读,龛,鲢,邋,粝,躐,鹨,聋,癃,窿,胪,舻,孪,囊,摄,赎,傥,饕,听,弯,鹧"
    charstring_ori = "叠,读,听,弯"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar22huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 22, "火", "")
    Huo_Dict[22] = chinchar22huo
    HuoFullList = HuoFullList + chinchar22huo

    # 23画火字
    # charstring_ori = "雠,恋,鹩,蛎,鳞,麟,轳,挛,栾,猡,猱,摊,体,显"
    charstring_ori = "恋,麟,栾,休,显"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar23huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 23, "火", "")
    Huo_Dict[23] = chinchar23huo
    HuoFullList = HuoFullList + chinchar23huo

    # 24画火字
    # charstring_ori = "螭,鞑,癫,蠹,攫,雳,谰,鳢,灵,陇,鹭,让,闼,瘫,厅,龌,鳣"
    charstring_ori="鹭,让,厅"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar24huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 24, "火", "")
    Huo_Dict[24] = chinchar24huo
    HuoFullList = HuoFullList + chinchar24huo

    # 25画火字
    # charstring_ori = "叆,纛,揽,鬣,酃,颅,脔,摞,囔"
    charstring_ori="揽"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar25huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 25, "火", "")
    Huo_Dict[25] = chinchar25huo
    HuoFullList = HuoFullList + chinchar25huo

    # 26画火字
    # charstring_ori = "叆,纛,揽,鬣,酃,颅,脔,摞,囔"
    charstring_ori = "逻,郦,邐"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar26huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 26, "火", "")
    Huo_Dict[26] = chinchar26huo
    HuoFullList = HuoFullList + chinchar26huo

    # 27画火字
    # charstring_ori = "叆,纛,揽,鬣,酃,颅,脔,摞,囔"
    charstring_ori = "骧"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar27huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 27, "火", "")
    Huo_Dict[27] = chinchar27huo
    HuoFullList = HuoFullList + chinchar27huo

    # 28画火字
    # charstring_ori = "叆,纛,揽,鬣,酃,颅,脔,摞,囔"
    charstring_ori = "鹦"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar28huo = Mylib.GetChineseCharlist(charstring_tmp, list(), 28, "火", "")
    Huo_Dict[28] = chinchar28huo
    HuoFullList = HuoFullList + chinchar28huo

    # endregion
    ChineseCharSet_Huo.dictbybihua = Huo_Dict
    ChineseCharSet_Huo.fulllist = HuoFullList
    return ChineseCharSet_Huo
def InitTuData(ChineseCharSet_Tu):
    Tu_Dict = {}
    TuFullList = list()
    # region 土字初始化
    # 3画土字
    # charstring_ori = "己,山,土,丸,兀,丫,也,尢,于"
    charstring_ori = "土,己,于"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar3tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 3, "土", "")
    Tu_Dict[3] = chinchar3tu
    TuFullList = TuFullList + chinchar3tu

    # 4画土字
    # charstring_ori = "厄,切,王,卬,夭,尹,引,尤,友,予,曰,允"
    charstring_ori = "切,尹,引,友,予,允"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar4tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 4, "土", "")
    Tu_Dict[4] = chinchar4tu
    TuFullList = TuFullList + chinchar4tu

    # 5画土字
    # charstring_ori = "凹,瓦,戊,矽,央,以,永,用,由,右,幼,孕,仔"
    charstring_ori = "央,以,永,用,由,右,幼"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar5tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 5, "土", "")
    Tu_Dict[5] = chinchar5tu
    TuFullList = TuFullList + chinchar5tu

    # 6画土字
    # charstring_ori = "吖,安,充,地,圪,艮,圭,灰,圾,岌,戌,圳,圮,屺,戍,似,吐,圩,仵,伍,伢,羊,伊,衣,圯,夷,亦,屹,因,有,宇,羽"
    charstring_ori = "安,充,地,圭,圳,似,伊,夷,亦,因,有,宇,羽"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar6tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 6, "土", "")
    Tu_Dict[6] = chinchar6tu
    TuFullList = TuFullList + chinchar6tu

    # 7画土字
    # charstring_ori = "岙,岜,坂,坌,辰,坊,坩,均,坎,坑,牡,圻,岐,岍,坍,秃,完,位,圬,氙,岘,呀,岈,延,冶,矣,佚,役,邑,吲,甬,攸,卣,佑,余,欤,玙,址"
    charstring_ori = "坂,延,佚,佑,余,址"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar7tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 7, "土", "")
    Tu_Dict[7] = chinchar7tu
    TuFullList = TuFullList + chinchar7tu

    # 8画土字
    # charstring_ori = "艾,坳,垇,坻,坫,矾,附,矸,岣,岵,岬,坷,岢,岫,盱,坤,垃,峁,岷,坭,爬,帕,坢,坯,坪,坡,坦,坨,宛,往,旺,委,忤,亚,奄,肴,夜,依,抑,佾,咏,呦,侑,於,盂,臾,昀,狁"
    charstring_ori = "艾,附,帕,往,旺,委,抑,咏"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar8tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 8, "土", "")
    Tu_Dict[8] = chinchar8tu
    TuFullList = TuFullList + chinchar8tu

    # 9画土字
    # charstring_ori = "哀,垵,拗,砭,垞,衩,昶,垤,垌,峒,肚,砘,垛,垩,垡,垓,垢,砍,砉,奎,趴,怕,盆,砒,垧,哇,娃,威,韦,畏,胃,瓮,屋,侮,型,峋,押,垭,娅,砑,咽,匽,怏,垚,姚,要,咿,怡,咦,姨,舣,姻,音,垠,俑,勇,幽,疣,羑,囿,宥,纡,舁,禹,垣,爰,约,玥,窀"
    charstring_ori="威,韦,屋,型,娅,怡,音,勇,垣,爰,约,玥"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar9tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 9, "土", "")
    Tu_Dict[9] = chinchar9tu
    TuFullList = TuFullList + chinchar9tu

    # 10画土字
    # charstring_ori = "啊,唉,埃,砹,鹌,俺,按,案,盎,敖,芺,峬,城,埕,砥,峨,恩,砝,砩,个,埂,埚,轩,砬,埒,埋,砰,破,埔,砌,峭,窃,容,埏,砷,堍,砣,娓,翁,唔,阢,峡,蚜,氩,恹,胭,宴,晏,氧,恙,眙,酏,益,殷,氤,蚓,祐,迂,邘,育,彧,眢,员,袁,砸,砟,砧,肫"
    charstring_ori = "按,盎,敖,城,埕,恩,个,埂,轩,埔,砌,翁,益,殷,迂,育,员"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar10tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 10, "土", "")
    Tu_Dict[10] = chinchar10tu
    TuFullList = TuFullList + chinchar10tu

    # 11画土字
    # charstring_ori = "挨,庵,唵,埯,崩,埠,堾,埭,岽,硐,堆,岗,硌,崮,硅,崞,胡,基,崛,崆,勖,峥,埴,堀,崃,硭,埝,鸟,啪,培,堋,埤,崎,畦,牵,眭,堂,窕,眺,婉,唯,帷,伟,尉,迕,捂,牾,硒,崤,硎,琊,崖,哑,讶,迓,崦,焉,偃,痒,野,痍,移,异,埸,翌,狺,寅,迎,茔,庸,恿,悠,蚰,蚴,狳,域,欲,蛭"
    charstring_ori="掰,焙,采,场,程,单,登,迪,敦,焦,接,晶,理,铁,媛,智,轴"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar11tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 11, "土", "")
    Tu_Dict[11] = chinchar11tu
    TuFullList = TuFullList + chinchar11tu

    # 12画土字
    # charstring_ori = "捱,媕,啽,晻,胺,媪,傲,奡,堡,堛,嵖,砗,堤,奠,堞,恶,费,黑,堠,画,黄,堪,跖,喹,岚,塄,嵋,垴,蛙,崴,为,围,帏,惟,喂,硪,婺,痦,翕,硖,翔,硝,砚,堰,揶,掖,猗,壹,诒,迤,贻,胰,喑,堙,喁,釉,嵛,鼋,粤,越,崽"
    charstring_ori="捱,画,翔,幃,围,为,硝,砚,贻,越"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar12tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 12, "土", "")
    Tu_Dict[12] = chinchar12tu
    TuFullList = TuFullList + chinchar12tu

    # 13画土字
    # charstring_ori = "阿,矮,爱,嗌,揞,暗,嗷,嶅,廒,奥,碑,碚,碘,碉,碇,碓,痱,话,觟,嵴,碱,垲,诩,块,跬,袅,硼,圣,嵊,嵩,塑,碎,塌,塘,填,琬,碗,嵬,猥,痿,艉,猬,温,嗡,握,呜,蜈,坞,勋,埙,睚,衙,揠,蜒,爷,揖,饴,诣,意,裔,饮,佣,雍,蛹,犹,猷,瘀,园,圆,援,塬,氲,恽,晕,愠,轾,稚,嵫"
    charstring_ori="爱,奥,碚,话,塑,琬,鸣,饴,意,圆,园,援"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar13tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 13, "土", "")
    Tu_Dict[13] = chinchar13tu
    TuFullList = TuFullList + chinchar13tu

    # 14画土字
    # charstring_ori = "肮,獒,塝,碥,碴,墋,诞,碲,垫,碟,砜,闺,监,碣,境,墚,顼,嘘,墟,逵,壸,嵝,墁,呕,碰,堑,岖,墒,塾,墅,硕,碳,维,玮,诬,误,寤,瑕,鞋,碹,腌,嫣,耶,腋,祎,旖,夤,瑛,墉,踊,诱,与,鸢,冤,猿,殒,翟,崭,嶂,坠,准"
    charstring_ori="诞,境,碟,塹,墅,硕,玮,耶,瑛,准"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar14tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 14, "土", "")
    Tu_Dict[14] = chinchar14tu
    TuFullList = TuFullList + chinchar14tu

    # 15画土字
    # charstring_ori = "腤,鞍,璈,墺,嶓,嶒,墀,磁,磋,嶝,墩,堕,废,坟,磙,嘿,糊,蝴,峤,磕,糈,蝰,崂,磊,嶙,碾,嬲,欧,殴,怄,磐,嵚,确,豌,纬,诿,卫,慰,庑,娴,鸦,养,噎,叶,靥,亿,逸,影,慵,忧,邮,鱿,蝣,牖,谀,缘,院,阅,增,磔"
    charstring_ori="鞍,磊,碾,欧,确,纬,卫,叶,影,缘,增"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar15tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 15, "土", "")
    Tu_Dict[15] = chinchar15tu
    TuFullList = TuFullList + chinchar15tu

    # # 16画土字
    # charstring_ori = "嗳,嫒,谙,聱,螯,懊,磅,壁,碜,惯,衡,垦,垮,磨,瓯,碛,墙,融,坛,违,谓,怃,歙,遐,鸭,阉,燕,噫,颐,峄,殪,阴,壅,馀,豫,鸳,螈,运,郓,酝,砖"
    # charstring_tmp = Mylib.charStrtolist(charstring_ori)
    # chinchar16tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 16, "土", "")
    # Tu_Dict[16] = chinchar16tu
    # TuFullList = TuFullList + chinchar16tu

    # 17画土字
    # charstring_ori = "隘,闇,鮟,醠,遨,謷,磴,礅,鲑,壕,壑,磺,矶,礁,圹,岭,硗,嵘,闱,鲔,邬,压,阳,嶷,忆,怿,翳,应,婴,膺,拥,优,黝,隅,屿,辕,远,龠,郧"
    # charstring_tmp = Mylib.charStrtolist(charstring_ori)
    # chinchar17tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 17, "土", "")
    # Tu_Dict[17] = chinchar17tu
    # TuFullList = TuFullList + chinchar17tu

    # 18画土字
    # charstring_ori = "碍,瑷,盫,袄,蹦,璧,础,礓,垒,讴,韪,鄢,医,黟,彝,癔,鄞,鄘,鼬,陨"
    charstring_ori = "蹦,璧,垒,讴,医"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar18tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 18, "土", "")
    Tu_Dict[18] = chinchar18tu
    TuFullList = TuFullList + chinchar18tu

    # 19画土字
    # charstring_ori = "爊,礤,坏,疆,坜,垄,垆,稳,鹉,骛,臆,臃,韵"
    charstring_ori="疆,坜,垄,穏,鹜,韵"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar19tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 19, "土", "")
    Tu_Dict[19] = chinchar19tu
    TuFullList = TuFullList + chinchar19tu

    # 20画土字
    # charstring_ori = "骜,巉,矿,岿,砾,壤,鼯,鹜,邺,瘾,嘤,罂"
    charstring_ori = "砾,壌,鹜"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar20tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 20, "土", "")
    Tu_Dict[20] = chinchar20tu
    TuFullList = TuFullList + chinchar20tu

    # 21画土字
    # charstring_ori = "鳌,礴,蠡,砺,砻,碌,礞,巍,撄,誉,跃"
    charstring_ori="砺,巍,誉,跃"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar21tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 21, "土", "")
    Tu_Dict[21] = chinchar21tu
    TuFullList = TuFullList + chinchar21tu

    # 22画土字
    # charstring_ori = "巅,峦,鸥,懿,隐,璎,鳙,饔"
    charstring_ori="峦,鸥,懿,隐"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar22tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 22, "土", "")
    Tu_Dict[22] = chinchar22tu
    TuFullList = TuFullList + chinchar22tu

    # 23画土字
    # charstring_ori = "娈,岩,缨"
    charstring_ori = "缨"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar23tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 23, "土", "")
    Tu_Dict[23] = chinchar23tu
    TuFullList = TuFullList + chinchar23tu

    # 24画土字
    # charstring_ori = "坝,罐,盐,艳,呓"
    charstring_ori = "坝,艳,呓"
    charstring_tmp = Mylib.charStrtolist(charstring_ori)
    chinchar24tu = Mylib.GetChineseCharlist(charstring_tmp, list(), 24, "土", "")
    Tu_Dict[24] = chinchar24tu
    TuFullList = TuFullList + chinchar24tu
    # endregion

    ChineseCharSet_Tu.dictbybihua = Tu_Dict
    ChineseCharSet_Tu.fulllist = TuFullList
    return ChineseCharSet_Tu

# 初始化

Mu_Set=InitMuData(Mu_Set)
Huo_Set=InitHuoData(Huo_Set)
Tu_Set=InitTuData(Tu_Set)
print()
print("--------- 初始化完成 ------------")
print("木属性字："+str(len(Mu_Set.fulllist)))
print("火属性字："+str(len(Huo_Set.fulllist)))
print("土属性字："+str(len(Tu_Set.fulllist)))

print()
# 根据名五行顺序得出名字集
def GetNameByWuxing(fulllist1,fulllist2):
    # ChineseName类队列
    Namelist=list()

    FullList1=fulllist1
    FullList2=fulllist2
    for i in fulllist1:
        for j in fulllist2:
            # 创建名字类例
            Myname = Mylib.ChineseName()
            Myname.Setinfo(i.zi,i.bihua,i.wuxing,"",j.zi,j.bihua,j.wuxing,"")
            Namelist.append(Myname)
    #         print(Myname.givenname,end="")
    # print(str(len(Namelist)))
    return Namelist

# 根据81数理吉凶得出吉利名字
def GetNameByGood81(list):
    Myname=[]
    for i in list:
        if i.zongbihua in Goodfrom81:
           Myname.append(i)

    return Myname



# print("--------- 火土组合名字 ---------")
#
# NamelistByHuoTu= GetNameByWuxing(Huo_Set.fulllist,Tu_Set.fulllist)
# # print()
# NamelistByHuoTuBy81=GetNameByGood81(NamelistByHuoTu)
# print("火土组合共：" + str(len(NamelistByHuoTu)) + "个，"+"其中符合81数理名字：" + str(len(NamelistByHuoTuBy81)) + "个")
# # 顺序打印名字组合，每行50个
# for i in NamelistByHuoTu:
#     if (NamelistByHuoTu.index(i)+1) % 50 != 0:
#         print(i.givenname+",",end="")
#     else:
#         print(i.givenname)





# print("--------- 土火组合名字 ---------")
# NamelistByTuHuo= GetNameByWuxing(Tu_Set.fulllist,Huo_Set.fulllist)
# # print()
# NamelistByTuHuoBy81=GetNameByGood81(NamelistByTuHuo)
# print("土火组合共：" + str(len(NamelistByTuHuo)) + "个，"+"其中符合81数理名字：" + str(len(NamelistByTuHuoBy81)) + "个")
# # 顺序打印名字组合，每行50个
# for i in NamelistByTuHuo:
#     if (NamelistByTuHuo.index(i)+1) % 50 != 0:
#         print(i.givenname+",",end="")
#     else:
#         print(i.givenname)
