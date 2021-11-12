
import sys
import json
import requests
import time
import os
import datetime
from local_to_afs import load_file_to_mart

'''
Author:jiaoxiaolong
Date：2020-03-13
Des:获取云游戏包名和游戏名
'''


reload(sys)
sys.setdefaultencoding('utf8')

sys.path.append("../../utils")

date=sys.argv[1]




def log(msg):
    """
    log
    :param msg:  msg
    :return:  return
    """
    msg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' ' + msg
    os.system('echo ' + msg)


def execute(url):
    """
    execute
    :param url: url
    :param channel:  channel
    :param date_str: str
    :return:  return
    """
    response=requests.get(url).text.decode("unicode-escape")
#    print result

    #先把字典转成json
    result=json.loads(response)
    print 'url:', url


    print "B"
    return True


url='https://yunapp-ws-sandbox.baidu.com/v1/open/apps?appkey=xPLHWwUCDBiVa4QrZyT2g73M&start=0'

local_file = os.path.dirname(os.path.abspath('get_cloudgame_pkg_name.py')) + "/get_cloudgame_pkg_name_" + date
file_name = "get_cloudgame_pkg_name_" + date
taskinfo = open(file_name, 'w')


if __name__ == "__main__":
	execute(url)
    log('pkg && name  is done'  )
    taskinfo.close()
   
    #load_file_to_mart(startDate, local_file, file_name, "getChannelAppList")
    #os.system("rm %s" % (file_name))
  print "program end"
