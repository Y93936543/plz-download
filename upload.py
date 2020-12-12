# -*- coding:utf-8 -*-
import os
from webdav3.client import Client

driver_prefix = os.getenv("driver")

if driver_prefix==None or driver_prefix=="Home":
    print("请先新建Wiki页面，详情请参考项目Readme!")
    exit(-1)

driver_prefix = driver_prefix[:-3]

webdav_url = "https://dav.jianguoyun.com/dav/download"
webdav_username = "mrleaf@vip.qq.com"
webdav_password = "aif9f4pca2vv66gv"

print(webdav_url+"\n"+webdav_username+"\n"+webdav_password)

options = {
 'webdav_hostname': webdav_url,
 'webdav_login':    webdav_username,
 'webdav_password': webdav_password,
 'disable_check': True
}

client = Client(options)

os.chdir("download")

for it in os.listdir():
    if os.path.isfile(it):
        client.upload(remote_path=it,local_path=it)

print("✨ All file uploaded")
