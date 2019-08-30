#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import requests
import json
import time
#下面这句库引入是在python2.x中
#import MySQLdb
#python3.x中的数据库库类引入
import pymysql
#在python中可以注释掉下面三句
'''import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
#删掉了数据库连接的信息
class news_scrapy(object):
    def __init__(self):
        # 这里是真的懒得想英文.....而且一共没有几个栏目，不需要写爬虫
        self.__columnUrlDict = {
        '''
            "zhongyaoxinwen": "https://www.xuexi.cn/98d5ae483720f701144e4dabf99a4a34/5957f69bffab66811b99940516ec8784.html",
            "zhongyaohuodong": "https://www.xuexi.cn/c06bf4acc7eef6ef0a560328938b5771/9a3668c13f6e303932b5e0e100fc248b.html",
            "zhongyaohuiyi": "https://www.xuexi.cn/89acb6d339cd09d5aaf0c2697b6a3278/9a3668c13f6e303932b5e0e100fc248b.html",
            "zhongyaojianghua": "https://www.xuexi.cn/588a4707f9db9606d832e51bfb3cea3b/9a3668c13f6e303932b5e0e100fc248b.html",
            "zhongyaowenzhang": "https://www.xuexi.cn/6db80fbc0859e5c06b81fd5d6d618749/9a3668c13f6e303932b5e0e100fc248b.html",
            "chuguofangwen": "https://www.xuexi.cn/2e5fc9557e56b14ececee0174deac67f/9a3668c13f6e303932b5e0e100fc248b.html",
            "zhishipishi": "https://www.xuexi.cn/682fd2c2ee5b0fa149e0ff11f8f13cea/9a3668c13f6e303932b5e0e100fc248b.html",
            "handianzhici": "https://www.xuexi.cn/13e9b085b05a257ed25359b0a7b869ff/9a3668c13f6e303932b5e0e100fc248b.html",
            "xinshidaijishi": "https://www.xuexi.cn/9ca612f28c9f86ad87d5daa34c588e00/9a3668c13f6e303932b5e0e100fc248b.html",
            "xuexishipin": "https://www.xuexi.cn/d05cad69216e688d304bb91ef3aac4c6/9a3668c13f6e303932b5e0e100fc248b.html",
            "zonghexinwen": "https://www.xuexi.cn/7097477a9643eacffe4cc101e4906fdb/9a3668c13f6e303932b5e0e100fc248b.html",
            "toutiaoxinwei":"https://www.xuexi.cn/72ac54163d26d6677a80b8e21a776cfa/9a3668c13f6e303932b5e0e100fc248b.html"
        '''
            #学习重点
           	"xuexizhongdian":"https://www.xuexi.cn/72bead8d9b5821a270f4f2c043d1ef02/463634d0259f8d74722f42db51b659b5.html",
            #学习新思想
            "zhongyaoxinwen":"https://www.xuexi.cn/lgdata/1jscb6pu1n2.json?_st=26095725",
            "zhongyaohuodong":"https://www.xuexi.cn/lgdata/1jpuhp6fn73.json?_st=26095746",
            "zhongyaohuiyi":"https://www.xuexi.cn/lgdata/19vhj0omh73.json?_st=26095747",
            "zhongyaojianghua":"https://www.xuexi.cn/lgdata/132gdqo7l73.json?_st=26095749",
            "zhongyaowenzhang":"https://www.xuexi.cn/lgdata/1ahjpjgb4n3.json?_st=26095750",
            "chuguofangwen":"https://www.xuexi.cn/lgdata/1je1objnh73.json?_st=26095752",
            "zhishipishi":"https://www.xuexi.cn/lgdata/1kvrj9vvv73.json?_st=26095752",
            "handianzhici":"https://www.xuexi.cn/lgdata/17qonfb74n3.json?_st=26095753",
            "xinshidaijishi":"https://www.xuexi.cn/lgdata/1i30sdhg0n3.json?_st=26095754",
            "xuexishipin":"https://www.xuexi.cn/lgdata/1ap1igfgdn2.json?_st=26095755",
            "zonghexinwen":"https://www.xuexi.cn/lgdata/1ajhkle8l72.json?_st=26095756",
            "toutiaoxinwei":"https://www.xuexi.cn/lgdata/1crqb964p71.json?_st=26095757",
            #十九大时间
            "shijiudawenxian":"https://www.xuexi.cn/lgdata/11d24l914n4.json?_st=26095831",
            "shijiudabaogao":"https://www.xuexi.cn/lgdata/1a78j52k2n4.json?_st=26095832",
            "shijiujiezhongyangquanhui":"https://www.xuexi.cn/lgdata/1c7mgi6tg74.json?_st=26095835",
            "shijiujiezhongyangjiweiquanhui":"https://www.xuexi.cn/lgdata/1niulj5tbn4.json?_st=26095836",
            "yanshenyuedu":"https://www.xuexi.cn/lgdata/1nf12u57o74.json?_st=26096131",
            "niwenwoda":"https://www.xuexi.cn/lgdata/1jfhm81amn4.json?_st=26096132",
            "xueximianduimian":"https://www.xuexi.cn/lgdata/11gg7rev674.json?_st=26096133",
            #学习理论
            "xuexililun":"https://www.xuexi.cn/lgdata/u1ght1omn2.json?_st=26096137",
            #红色中国
            "yongyuandefengbei":"https://www.xuexi.cn/lgdata/1n544qrtv7c.json?_st=26096145",
            #视频需要用视频爬虫去单独处理
            #"shipinzhuanqu":"https://www.xuexi.cn/lgdata/3jsf4shrl928.json?_st=26096148",
            ##红色中国-红色记忆
            "changzhengjinianguan":"https://www.xuexi.cn/lgdata/u16ui97tnm.json?_st=26096163",
            "kangzhanjinianguan":"https://www.xuexi.cn/lgdata/1c0be8revnm.json?_st=26096164",
            "jiefangzhanzheng":"https://www.xuexi.cn/lgdata/1bh4bl63fnm.json?_st=26096164",
            "hongselvyou":"https://www.xuexi.cn/lgdata/181gpjpb4nm.json?_st=26096165",
            "hongselvyouluxian":"https://www.xuexi.cn/lgdata/1dil8gmtq7m.json?_st=26096166",
            "lijiedangdaihui":"https://www.xuexi.cn/lgdata/1of97bn6c7m.json?_st=26096168",
            #红色中国-党史研究
            "dangshigushi":"https://www.xuexi.cn/lgdata/1drkih7p27m.json?_st=26096167",
            "dangshizhishi":"https://www.xuexi.cn/lgdata/1k8ffl9m8nm.json?_st=26096170",
            "dangshiyanjiu":"https://www.xuexi.cn/lgdata/1ogogofuqnm.json?_st=26096170",
            #红色中国-中国精神研究
            "wusijingshen":"https://www.xuexi.cn/lgdata/1ibpde47i7l.json?_st=26096176",
            "hongchuanjingshen":"https://www.xuexi.cn/lgdata/ue2lvnpl7l.json?_st=26096176",
            "jinggangshanjingshen":"https://www.xuexi.cn/lgdata/uo3b9nde7l.json?_st=26096177",
            "changzhengjingshen":"https://www.xuexi.cn/lgdata/136cgvrgp7l.json?_st=26096178",
            "yananjingshen":"https://www.xuexi.cn/lgdata/1ebgr501e7l.json?_st=26096179",
            "taihangjingshen":"https://www.xuexi.cn/lgdata/10444suc57l.json?_st=26096179",
            "yimengjingshen":"https://www.xuexi.cn/lgdata/1nf7dv27p7l.json?_st=26096180",
            "xibaipojingshen":"https://www.xuexi.cn/lgdata/1gqebjagq7l.json?_st=26096181",
            "tierenjingshen":"https://www.xuexi.cn/lgdata/1ganajvkg7l.json?_st=26096181",
            "jiaoyulujingshen":"https://www.xuexi.cn/lgdata/16td1roi77l.json?_st=26096182",
            "liangdanyixingjingshen":"https://www.xuexi.cn/lgdata/17ictec57nl.json?_st=26096182",
            "hansaibajingshen":"https://www.xuexi.cn/lgdata/11fksd93o7l.json?_st=26096183",
            "gaigekaifangjingshen":"https://www.xuexi.cn/lgdata/2qvbqhmdrube.json?_st=26096184",
            #学习科学
            "kejisixiangyanjiu":"https://www.xuexi.cn/lgdata/1eppcq11fne.json?_st=26096190",
            "kexuejingshentan":"https://www.xuexi.cn/lgdata/1armpdlt5ne.json?_st=26096194",
            "guojiagongcheng":"https://www.xuexi.cn/lgdata/1moa0khf17e.json?_st=26096195",
            "5G":"https://www.xuexi.cn/lgdata/56j1nv2difvo.json?_st=26096196",
            "kejiqianyan":"https://www.xuexi.cn/lgdata/152ijthp37e.json?_st=26096196",
            "dangdaikexuejiagushi":"https://www.xuexi.cn/lgdata/11jihrmq37e.json?_st=26096198",
            "yixianfengcai":"https://www.xuexi.cn/lgdata/1cieuomejnn.json?_st=26096198",
            "zhengcejiedu":"https://www.xuexi.cn/lgdata/1lje05c9une.json?_st=26096200",
            "kepuzhishi":"https://www.xuexi.cn/lgdata/1drofao4h7e.json?_st=26096205",
            "zhongguokejishi":"https://www.xuexi.cn/lgdata/110jqimatnn.json?_st=26096206",
            "zhongguolidaikexuejia":"https://www.xuexi.cn/lgdata/153hr7eadnn.json?_st=26096206",
            "waiguokexuejia":"https://www.xuexi.cn/lgdata/14ddfon4e7n.json?_st=26096207",
            "shijiekejishi":"https://www.xuexi.cn/lgdata/14gko3bjk7n.json?_st=26096208",
            #科学著作是pdf文本，爬到存数据库不好存，暂时去掉
            #"kexuezhuzuo":"https://www.xuexi.cn/lgdata/u6i3lnss7e.json?_st=26096210",
            "xinlifudao":"https://www.xuexi.cn/lgdata/1h4s6pojfne.json?_st=26096211",
            #环球视野
            "xijinpingwaijiaosixiang":"https://www.xuexi.cn/lgdata/1ooaa665snf.json?_st=26096213",
            "shijieyanzhongdexijinping":"https://www.xuexi.cn/lgdata/vdppiu92n1.json?_st=26096214",
            #环球视野-一带一路
            "xinwenzixun":"https://www.xuexi.cn/lgdata/1kok79h5s7n.json?_st=26096216",
            "zhengcehuanjing":"https://www.xuexi.cn/lgdata/1mjdmg8mtnn.json?_st=26096216",
            "hulianhutong":"https://www.xuexi.cn/lgdata/1kb4calll7n.json?_st=26096217",
            "guojihezuo":"https://www.xuexi.cn/lgdata/t1u2cdg6nn.json?_st=26096218",
            "jicushuju":"https://www.xuexi.cn/lgdata/1dqdq0hj07n.json?_st=26096218",
            "gonghuasilu":"https://www.xuexi.cn/lgdata/1kmjuu09c7n.json?_st=26096219",
            "wenboyaniu":"https://www.xuexi.cn/lgdata/1063lvdd6nd.json?_st=26096222",
            #视频，先去掉
            #"wenbogongkiake":"https://www.xuexi.cn/lgdata/1o2r10b6f7d.json?_st=26096223",
            #"wenbojilupian":"https://www.xuexi.cn/lgdata/17j565ghcnd.json?_st=26096224",
            #习近平文汇:栏目内容较杂，先去掉
            #学习电视台和学习慕课都是视频：先去掉
            #学习文化：栏目很多，先爬建筑、武术、楹联、医药，其余的基本功能满足后再加
            #学习文化-中国建筑：建筑与文化、建筑知识栏目数据不是通过json生成，而是在data+MD5里，先去掉
            "gudaijianzhujicui":"https://www.xuexi.cn/lgdata/v4pq4uth7d.json?_st=26096242",
            "jindaijianzhujicui":"https://www.xuexi.cn/lgdata/1c59olfnvnd.json?_st=26096243",
            "jianshewenhuayujianzhuyanjiu":"https://www.xuexi.cn/lgdata/1oog782287d.json?_st=26096246",
            "jianzhumingjia":"https://www.xuexi.cn/lgdata/tnigd8qund.json?_st=26096248",
            #学习文化-中华武术,中华武术教学是视频，先去掉
            "wushuyanbian":"https://www.xuexi.cn/lgdata/1lnc6c84mnd.json?_st=26096250",
            "zhonghuashangwujingshen":"https://www.xuexi.cn/lgdata/11j85c92mnd.json?_st=26096252",
            "zhonghuawuhun":"https://www.xuexi.cn/lgdata/13d9au2i0nd.json?_st=26096253",
            "zhonghuawuxue":"https://www.xuexi.cn/lgdata/vb0qh7so7d.json?_st=26096254",
            #学习文化-中华医药
            "zhongyidianji":"https://www.xuexi.cn/lgdata/urm3g97vnn.json?_st=26096257",
            "lidaimingyi":"https://www.xuexi.cn/lgdata/168delc1d7e.json?_st=26096259",
            "dangdaimingyi":"https://www.xuexi.cn/lgdata/18r1mt5nh7e.json?_st=26096260",
            "zhonghuayiyaoyushijie":"https://www.xuexi.cn/lgdata/15q5l76icne.json?_st=26096262",
            #学习文化-中华楹联,楹联视频先去掉
            "minglianjianshang":"https://www.xuexi.cn/lgdata/1i276vso3ne.json?_st=26096267",
            #学习文化-中华楹联-楹联与习俗-楹联习俗
            "chunlianxisu":"https://www.xuexi.cn/lgdata/4j8eurk302bq.json?_st=26096268",
            #学习文化-中华楹联-楹联与习俗-节令楹联
            "jielingyinglian":"https://www.xuexi.cn/lgdata/4b0a3rjqb9uq.json?_st=26096270",
            #学习文化-中华楹联-楹联与习俗-行业楹联
            "hangyeyinglian":"https://www.xuexi.cn/lgdata/48oc8va2veoh.json?_st=26096271",
            #学习文化-中华楹联-楹联与习俗-喜庆楹联
            "xiqingyinglian":"https://www.xuexi.cn/lgdata/4qkgon8lvjdj.json?_st=26096272",
            #学习文化-中华楹联-楹联与习俗-宗教楹联
            "zongjiaoyinglian":"https://www.xuexi.cn/lgdata/3m1efumdciph.json?_st=26096273",
            #学习文化-中华楹联-楹联与习俗-其他楹联
            "qitayinglian":"https://www.xuexi.cn/lgdata/4a3hb4kkg5v4.json?_st=26096275",
            #学习文化-中华楹联-楹联知识
            "yinglianzhishi":"https://www.xuexi.cn/lgdata/10jabihga7e.json?_st=26096277",
            #强军兴军：1、习近平强军思想研究 2、强军时评 3、学习军史：军事家、军史故事、军史档案、军史文物4、古代军事家 5、古代兵器 6、兵器大观
            #其他的多数是图片和视频，先去掉
            "xijinpingqiangjunsixiangyanjiu":"https://www.xuexi.cn/lgdata/12lm260c37e.json?_st=26096287",
            "qiangjushiping":"https://www.xuexi.cn/lgdata/1j2fuv9rs7e.json?_st=26096378",
            "junshijia":"https://www.xuexi.cn/lgdata/16ap1a07pnn.json?_st=26096382",
            "junshigushi":"https://www.xuexi.cn/lgdata/178c76irs7n.json?_st=26096383",
            "junshidangan":"https://www.xuexi.cn/lgdata/1nan78i05nn.json?_st=26096384",
            "junshirenwu":"https://www.xuexi.cn/lgdata/12l486vm97n.json?_st=26096385",
            "gudaijunshijia":"https://www.xuexi.cn/lgdata/1mo5h6vk07f.json?_st=26096387",
            "gudaibingqi":"https://www.xuexi.cn/lgdata/ug4o30g07f.json?_st=26096390",
            "bingqidaguan":"https://www.xuexi.cn/lgdata/1gd1n2n667f.json?_st=26096445",
            #美丽中国:1、生态文明建设思想研究2、生态文明建设实践3、走遍中国4、记住乡愁5、历史文化名城6、历史文化名镇7、历史文化名街
            "shengtaiwenmingjianshesixiangyanjiu":"https://www.xuexi.cn/lgdata/1ahi87vjg7e.json?_st=26096452",
            "shengtaiwenmingjiansheshijian":"https://www.xuexi.cn/lgdata/1eiarm6b5ne.json?_st=26096462",
            "zoubianzhongguo":"https://www.xuexi.cn/lgdata/3alk4pkja8hl.json?_st=26096463",
            "jizhuxiangchou":"https://www.xuexi.cn/lgdata/dfo6qrb8n1p.json?_st=26096457",
            "lishiwenhuamingcheng":"https://www.xuexi.cn/lgdata/12k7uv48b7e.json?_st=26096458",
            "lishiwenhuamingzhen":"https://www.xuexi.cn/lgdata/1ogcjrb5c7e.json?_st=26096466",
            "lishiwenhuamingjie":"https://www.xuexi.cn/lgdata/1b04bc5p5ne.json?_st=26096467"

            }
        self.db = pymysql.connect("172.17.1.4", "emspapp", "emspapp", "QIANGGUO", charset='utf8')
        self.headers={
             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
            }
        self.urlList=[]#定义全局资讯详情url
        self.columnNum = 1#栏目数量
        self.countContent=1#某栏目的资讯数量

    def __decorateArticleUrlDict__(self):
        """
        用于对文章栏目url进行补充，以达到爬取网站所有文章的目的
        :return:
        """
        #下面三单引号注释的是对txt里的地址的空链接处理，爬取内容的话已初始化，无需再处理
        from aboutCategory.get_category_url import get_category_url
        scrapy = get_category_url()#类的实例化
        #从其他脚本拿到所有可用的栏目url
        validUrlList = scrapy.getValidurlList()#去除空链接的列表

        #将原来的栏目url字典变成列表
        completedArticleColumnUrl = []
        for value in self.__columnUrlDict.values():
            completedArticleColumnUrl.append(value)#现在一个是原来txt里处理过空链接的列表validUrlList，一个是初始化里字典处理后的列表
        #将所有新拿到的且内容文章的栏目url，加入到completedArticleColumnUrl这个列表中
        for columnUrl in validUrlList:
            try:
                temp = self.__getPercolumn_allUrl__(columnUrl)#文章详情url列表
                #print(temp)
                articleColumnUrl = columnUrl
                #print(articleColumnUrl)
                #判断本次的栏目url是否已经存在于列表中
                flag = True
                for url in completedArticleColumnUrl:
                    if url == articleColumnUrl:
                        flag = False

                #本次栏目不存在于列表时才插入
                if flag == True:
                    completedArticleColumnUrl.append(articleColumnUrl)
            except:
                print ("这是一个无法获取文章的栏目，应该是视频")
        print ("文章栏目更新完毕，下面开始更新文章")
        return completedArticleColumnUrl  #返回的是所有栏目的链接，里面是具体的内容

    def __getArticleDetail__(self,newsUrl):#获取不带id参数的资讯url内容
        """
        :param newsUrl:新闻页面的html地址，而不是js格式的请求地址
        :return: 一个包含了这篇新闻的各种信息的字典对象
        """
        jsUrlTemp = newsUrl.rsplit('/')
        jsUrl = "http:" + '//' + jsUrlTemp[2] + '/' + jsUrlTemp[3] + '/data' + jsUrlTemp[4].replace('html', 'js')
        unitInfObj = requests.get(url=jsUrl,headers=self.headers)
        unitInfObj.encoding = 'utf-8'
        articleDict={}
        if unitInfObj.text!='empty':
            for key,value in json.loads(unitInfObj.text.lstrip('globalCache = ').rstrip(';'),encoding="utf-8").items():
                if key == 'sysQuery':
                    pass
                elif key!= 'sysQuery':
                    try:
                        if len(json.loads(unitInfObj.text.lstrip('globalCache = ').rstrip(';')))<=3:
                            #if ('detail' in value)&&len(value['detail'])!=0:
                            if ('detail' in value):
                                articleDict['frst_name'] =value['detail']['frst_name']
                                articleDict['source']=value['detail']['source']
                                articleDict['editor']=value['detail']['editor']
                                articleDict['original_time']=value['detail']['original_time']
                                #print(type(value['detail']['cate_id'][0]))
                                articleDict['cate_id']=value['detail']['cate_id']
                                articleDict['article_url']=newsUrl
                                articleDict['page_id']=value['detail']['_id']
                                articleDict['content']=value['detail']['content']
                                #print(value['detail']['_id'])
                                return articleDict
                                # return json.dumps(result, encoding="UTF-8", ensure_ascii=False)
                            elif 'list' in value:
                                if value['list']['ossUrl']!='':
                                    print('该文章可能为视频')
                                    break
                            else:
                                print('该栏目不是视频也不是资讯，可能是资讯视频的列表，请检查')
                        else:
                            print('该栏目不是视频也不是资讯，请检查')#这里如果key有多个就打印多个，需要完善
                            break
                    except:
                        pass
        else:
            print('该文章内容可能为空，请检查：'+jsUrl)
    def __getArticleDetail_id__(self,newsUrl,type):#获取带id参数的资讯url内容,一个参数是资讯url，一个参数是由文章列表传来的资讯类型
        jsUrlTemp=newsUrl.split('?id=')
        jsUrl='https://boot-source.xuexi.cn/data/app/'+jsUrlTemp[1]+'.js'#带id参数的详情url地址
        unitInfObj = requests.get(url=jsUrl,headers=self.headers)
        #print(jsUrl)
        #print(unitInfObj.text)
        unitInfObj.encoding = 'utf-8'
        articleDict={}
        res=json.loads(unitInfObj.text.lstrip("callback(").rstrip(')'),encoding="utf-8")
        #print(res)
        try:
            articleDict['frst_name'] =res['title']
            articleDict['source']=res['source']
            articleDict['editor']=res['audit_setting']['specified_audit']['send_person_name']
            articleDict['original_time']=res['publish_time']
            articleDict['cate_id']=type #从__getPercolumn_allUrl_Id____返回的内容类别
            articleDict['article_url']=newsUrl
            articleDict['page_id']=res['identity']['item_id']
            articleDict['content']=res['normalized_content']
            return articleDict
        except:
            pass
    def __getPercolumn_allUrl_Id____(self,columnUrl):
        response = requests.get(url=columnUrl,headers=self.headers)
        response.encoding='utf-8'
        if(len(json.loads(response.text))>=60):
            res=json.loads(response.text)[0:60]#由于内容太多，只取前60条内容
        else:
            res=json.loads(response.text)
        #urlList=[]#资讯详情url列表
        for value in res:#res是列表，value是字典
            if 'url' in value:
                self.urlList.append(value['url'])
        return self.urlList,res[0]['channelNames'][0]  #返回两个，一个是资讯的url，一个是资讯的类别，在url带id的资讯字典里没有类别字段，所以从这返回到内容获取函数里，存到mysql
    def __getPercolumn_allUrl__(self,columnUrl):#获取所有栏目的资讯url
        """
        :param：columnUrl，栏目的网址
        :return:urlList，单个栏目中所有新闻的网址
        """
        jsUrlTemp = columnUrl.rsplit('/')
        jsUrl = "http:" + '//' + jsUrlTemp[2] + '/' + jsUrlTemp[3] + '/data' + jsUrlTemp[4].replace('html', 'js')
        print(jsUrl)
        res = requests.get(url=jsUrl,headers=self.headers)
        res.encoding = 'utf-8'
        #urlList = []
        for key,value in json.loads(res.text.lstrip('globalCache = ').rstrip(';'),encoding="utf-8").items():
            if key != 'sysQuery':
                if len(value['list'])>=60:
                    for item in  value['list'][0:60]:#资讯详情有两种，一种是带id参数的，一种不带，两个if处理
                        if 'art_id' in item:
                            self.urlList.append(item['art_id'])#urlList为链接列表
                        if 'static_page_url' in item:
                            self.urlList.append(item['static_page_url'])#urlList为链接列表
                        #time.sleep(1)
                        #print(static_page_url)
                else:
                    for item in value['list']:
                        if 'art_id' in item:
                            self.urlList.append(item['art_id'])
                        if 'static_page_url' in item:
                            self.urlList.append(item['static_page_url'])
            #print(urlList)
        return self.urlList #返回的是文章详情url列表

    def __firstTime__(self):
        # newstotal = []
        db = pymysql.connect("172.17.1.4", "emspapp", "emspapp", "QIANGGUO", charset='utf8')
        cursor = db.cursor()
        for columnUrl in self.__columnUrlDict.values():
            for url in self.__getPercolumn_allUrl__(columnUrl):
                # newsItemList = []
                newsItemdict = self.__getArticleDetail__(url)
                # newstotal.append(result)
                # data = pandas.DataFrame(newsItemList)
                # pandas.io.sql.write_frame(data,"qiangguoNews",engine)
                # data.to_sql('qiangguoNews', con=engine,if_exists='replace')
                #直接使用DB-API把数据存进去↓
                insertsql = "INSERT INTO QGNews(article_id,article_title,article_url,article_date,article_editor,article_source,column_id) VALUES('%s','%s','%s','%s','%s','%s','%s')"%(newsItemdict['page_id'],newsItemdict['frst_name'],newsItemdict['article_url'],newsItemdict['original_time'],newsItemdict['editor'],newsItemdict['source'],newsItemdict['cate_id'])
                try:
                    cursor.execute(insertsql)
                    db.commit()
                    print (insertsql)
                except:
                    print ("这一次错误")
        cursor.close()
    def __CheckMysql__(self,columnUrl):
        #global count
        count =0
        cursor=self.db.cursor()
        if '.html' in columnUrl:#不带id参数的
            for url in self.__getPercolumn_allUrl__(columnUrl):#不带id参数的，主要是“学习重点”栏目
                print('  '+'检查第{}个栏目的第{}篇资讯'.format(self.columnNum,self.countContent))
                print('  '+url)
                try:
                    if '.html' in url:
                        content_dic = self.__getArticleDetail__(url)
                    if '?id=' in url:
                        content_dic = self.__getArticleDetail_id__(url,contentType)
                    selectsql = "select * from QGNews where article_id = '%s'"%(content_dic['page_id'])
                    cursor.execute(selectsql)
                    if cursor.rowcount != 0:
                        if count < 20:
                            selectResult = cursor.fetchone()
                            print ("名称为《%s》的文章已存在，不需要更新" % (selectResult[2]))
                            count +=1
                        else:
                            print ("第%s个栏目的文章已经不需要更新了"%(self.columnNum))
                            #self.columnNum = self.columnNum+1
                            break
                    else:
                        insertsql = "INSERT INTO QGNews(article_id,article_title,article_url,article_date,article_editor,article_source,column_id,article_content) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                        content_dic['page_id'], content_dic['frst_name'], content_dic['article_url'],
                        content_dic['original_time'], content_dic['editor'], content_dic['source'],
                        content_dic['cate_id'],content_dic['content'])
                        #self.__insertData__(content_dic)
                        try:
                            cursor.execute(insertsql)
                            self.db.commit()
                            print ("【新文章提醒】这是一则新的文章，名称为《%s》，已为您更新到数据库" % (content_dic['frst_name']))
                        except:
                            print ("这一次插入数据错误")
                    #self.countContent=self.countContent+1
                except:
                    count += 1
                self.countContent=self.countContent+1#下一条资讯内容
            count=0
            self.countContent=1#该栏目的资讯已遍历完，进行下个栏目遍历时，该值清零
            self.columnNum=self.columnNum+1#下个栏目的序号
            self.urlList=[]#每次遍历完一个栏目都要清空，否则会存在已遍历过的栏目的资讯url
        if '.json?' in columnUrl:#带id参数的
            contentUrlList,contentType=self.__getPercolumn_allUrl_Id____(columnUrl)
            for url in contentUrlList:
                print('  '+'检查第{}个栏目的第{}篇资讯'.format(self.columnNum,self.countContent))
                print(url)
                try:
                    if url[-5:]=='.html':
                        content_dic = self.__getArticleDetail__(url)
                    if '?id=' in url:
                        content_dic = self.__getArticleDetail_id__(url,contentType)
                    #print(content_dic['page_id'])
                    selectsql = "select * from QGNews where article_id = '%s'"%(content_dic['page_id'])
                    cursor.execute(selectsql)
                    if cursor.rowcount != 0:
                        if count < 20:
                            selectResult = cursor.fetchone()
                            print ("名称为《%s》的文章已存在，不需要更新" % (selectResult[2]))
                            count +=1
                        else:
                            print ("第%s个栏目的文章已经不需要更新了"%(self.columnNum))
                            #self.columnNum = self.columnNum+1
                            break
                    else:
                        insertsql = "INSERT INTO QGNews(article_id,article_title,article_url,article_date,article_editor,article_source,column_id,article_content) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                        content_dic['page_id'], content_dic['frst_name'], content_dic['article_url'],
                        content_dic['original_time'], content_dic['editor'], content_dic['source'],
                        content_dic['cate_id'],content_dic['content'])
                        #self.__insertData__(content_dic)
                        try:
                            cursor.execute(insertsql)
                            self.db.commit()
                            print ("【新文章提醒】这是一则新的文章，名称为《%s》，已为您更新到数据库" % (content_dic['frst_name']))
                        except:
                            print ("这一次插入数据错误")
                except:
                    count += 1
                self.countContent=self.countContent+1
            count=0
            self.countContent=1
            self.columnNum=self.columnNum+1
            self.urlList=[]#每次遍历完一个栏目都要清空，否则会存在已遍历过的栏目的资讯url
    def __insertData__(self,dic):
        insertsql = "INSERT INTO QGNews(article_id,article_title,article_url,article_date,article_editor,article_source,column_id,article_content) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (
        dic['page_id'], dic['frst_name'], dic['article_url'],
        dic['original_time'], dic['editor'], dic['source'],
        dic['cate_id'],dic['content'])
        return insertsql
    def __ConnectMysql__(self):
        db.pymysql.connect("172.17.1.4","emspapp","emspapp","QIANGGUO",charset='utf-8')
        cursor=db.cursor()
        return cursor
    def __Maintain__(self):
        # newstotal = []
        #db = pymysql.connect("172.17.1.4", "emspapp", "emspapp", "QIANGGUO", charset='utf8')
        #cursor = db.cursor()
        for columnUrl in self.__columnUrlDict.values():#遍历所有的栏目链接,__init__初始化里的链接
            #count =0
            print ("现在对第%s个栏目进行检测" % (self.columnNum))
            print('\n栏目地址:'+columnUrl)
            self.__CheckMysql__(columnUrl)
            '''if '.html' in columnUrl:#不带id参数的
                for url in self.__getPercolumn_allUrl__(columnUrl):#不带id参数的，主要是“学习重点”栏目
                    print(url)
                    try:
                        newsItemdict = self.__getArticleDetail__(url)
                        slef.__CheckMysql__(newsItemdict)
                    except:
                        count += 1
            if '.json?' in columnUrl:#带id参数的
                contentUrlList,contentType=self.__getPercolumn_allUrl_Id____(columnUrl)
                for url in contentUrlList:
                    print(url)
                    try:
                        newsItemdict = self.__getArticleDetail_id__(columnUrl)
                        slef.__CheckMysql__(newsItemdict)
                    except:
                        count += 1
                #print(url)
                try:
                    newsItemdict = self.__getArticleDetail__(url)
                    selectsql = "select * from QGNews where article_id = '%s'"%(newsItemdict['page_id'])
                    cursor.execute(selectsql)
                    if cursor.rowcount != 0:
                        if count < 20:
                            selectResult = cursor.fetchone()
                            print ("名称为《%s》的文章已存在，不需要更新" % (selectResult[2]))
                            count +=1
                        else:
                            print ("第%s个栏目的文章已经不需要更新了"%(columnNum))
                            columnNum = columnNum+1
                            break
                    else:
                        insertsql = "INSERT INTO QGNews(article_id,article_title,article_url,article_date,article_editor,article_source,column_id) VALUES('%s','%s','%s','%s','%s','%s','%s')" % (
                        newsItemdict['page_id'], newsItemdict['frst_name'], newsItemdict['article_url'],
                        newsItemdict['original_time'], newsItemdict['editor'], newsItemdict['source'],
                        newsItemdict['cate_id'])
                        try:
                            cursor.execute(insertsql)
                            db.commit()
                            print ("【新文章提醒】这是一则新的文章，名称为《%s》，已为您更新到数据库" % (newsItemdict['frst_name']))
                        except:
                            print ("这一次插入数据错误")
            '''        
        else:
            print ("本日的更新已完成")

        self.db.cursor.close()

if __name__ == '__main__':
    scrapy = news_scrapy()
    # scrapy.__firstTime__()
    scrapy.__Maintain__()
    # scrapy.decorateUrlDict()
