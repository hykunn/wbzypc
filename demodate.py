import urllib.request
import time
def jsps(file1,str1):#函数 传入 页面 和查询得到人名字
   jzhnum = str(file1).find(str1)#查找人名在的位置
   jzhdg = file1[jzhnum:jzhnum + 100] #截取人名字附件的字符串，这里可以在浏览器f12查看截取的长度应该是多少，这里取100，下面也都是截取的部分
   jzhbegin = jzhdg.find('</em>')
   jzhend = jzhdg.find('票</span>')
   jzh = jzhdg[int(jzhbegin) + 5:int(jzhend) + 1]#最后把截取的部分输出出来。
   print (jzh)
   return jzh
while(1):
    try:#有的时候获取不到页面，导致程序崩溃，这里监控起来。
        response =urllib.request.urlopen('https://huodong.weibo.com/netchina2019#d97fa6785bf6cc8f1ca2d093fe851001_weiboad')#获取微博年度文物页面
        file1 = response.read().decode()#转码
        jzhp=jsps(file1,'简自豪')#调用函数，函数返回票数，传入获取的文件和需要查询的人物
        wybp=jsps(file1,'王一博')
        with open("data.txt","a+") as f:#把时间和两个数据写进data.txt文件里
            f.write(time.ctime())
            f.write("   ")
            f.write(jzhp)
            f.write("   ")
            f.write(wybp)
            f.write('\n')
        # jzhnum=str(file1).find('简自豪')
        # jzhdg=file1[jzhnum:jzhnum+100]
        # jzhbegin=jzhdg.find('</em>')
        # jzhend=jzhdg.find('票</span>')
        # jzh=jzhdg[int(jzhbegin)+5:int(jzhend)+1]
        # print(jzh)
            time.sleep(60)#每隔一分钟调用一次
    except:
        continue
