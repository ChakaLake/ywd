#python3运行
import re
import requests
import os
import json


class BiliBili(object,):
    def __init__(self,page_num,dir_name,file_name):
        self.base_url = "https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num={}".format(page_num)
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.count = file_name
        self.dir_name = dir_name
       
        #发送请求
    def send_request(self, url):
        resopnse = requests.get(url, headers=self.headers)
        data = resopnse.content.decode()
        json_data = json.loads(data)['data']['items']
        str_data = json.dumps(json_data)
        return str_data
       
        #发送图片链接请求
    def secend_request(self, url):
        resopnse = requests.get(url, headers=self.headers)
        data = resopnse.content
        return data
       
        #对基本url进行解析
    def analysis_url(self, data):
        pattern = re.compile('c": "(.*?)", "i')
        url = re.findall(pattern, data)
        return url
       
        #保存图片信息
    def save_file(self,dir_name,names,data,):
        with open( "{}/".format(dir_name)+ str(names) + '.jpg', 'wb') as f:
            f.write(data)
        #启动
    def run(self):
        try:
            os.mkdir(self.dir_name)
        except:
            pass
      
        data = self.send_request(self.base_url)
        url_list = self.analysis_url(data)
        
        for url in url_list:
            data = self.secend_request(url)
            self. save_file(self.dir_name,self.count,data,)
            print("正在下载第{}个图片".format(self.count))
            self.count += 1
        return "下载完毕"


if __name__ == '__main__':
    while True:
        page_num = int(input("请输入下载的页数"))
        dir_name = input("请输入想要存放的文件夹的名字")
        file_name = int(input("请输入文件的起始名字。仅限纯数字"))
        if type(file_name) == int:
            test = BiliBili(page_num,dir_name,file_name)
            test.run()