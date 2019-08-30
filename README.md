# myQingguo
一、学习强国，每个栏目的前60条数据内容
二、栏目链接分两种：
  1、如https://www.xuexi.cn/cc72a0454287bdedb7e2c156db55e818/71eb7214c6c0c1f5e6ec6e29564decb4.html，是md5加密的名字，没有参数，只需将".html"换
  成".js",然后在md5加密后的名字前加上data，即为该栏目所有的文章地址，即https://www.xuexi.cn/cc72a0454287bdedb7e2c156db55e818/data71eb7214c6c0c1f5e6ec6e29564decb4.js
  内容需要经过简单处理，就是json。
  2、需要注意，如果只用上面那个连接，是获取不到最新内容的，但是有些更新慢的栏目只能通过上个链接获取，估计是强国网站后期改动过，所以分析http请求的数据可以发现到一个带有参数json数据，如https://www.xuexi.cn/lgdata/u1ght1omn2.json?_st=26119288
  这个可以获取到所有的内容，因为内容太多，所以只抓了前60条内容。
三、文章内容链接分为两种：
  1、和栏目地址类似，如https://www.xuexi.cn/7d959ee7b3aee3d155e7da142cdec713/e43e220633a65f9b6d8b53712cba9caa.html，这类一般都是很早的内容，有些更新慢
  的内容链接就必须用这个抓取，只需将".html"换成".js",然后在md5加密后的名字前加上data即可获取文章内容，需要经过处理才是json。
  2、带有参数的html地址，一般都是最新的内容，如https://www.xuexi.cn/lgpage/detail/index.html?id=10981378426592497568，这个分析http的请求可以知道需要
  将后面的id参数（其实是md5加密后的）拼接一个地址，即https://boot-source.xuexi.cn/data/app/10981378426592497568.js，即可获取内容，也需要经过处理才是
  json。具题请看代码处理。
 四、mysql表结构
 CREATE TABLE QGNews(
article_index INT NOT NULL AUTO_INCREMENT,
article_id CHAR(100),
article_title CHAR(100),
article_url CHAR(100),
article_date CHAR(50),
article_editor CHAR(50),
article_content longtext,
article_source CHAR(50),
column_id CHAR(100),
PRIMARY KEY(article_index))DEFAULT CHARSET=utf8;
五、有问题请联系：
  qq：541095024
  微信：lqq_1228
