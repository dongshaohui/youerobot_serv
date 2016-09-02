#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'youerobotServ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # 用户服务相关路由
    url(r'^user_serv/upload_android_id','userServ.views.upload_android_id'), # 上传android_id，创建家庭账户
    url(r'^user_serv/choose_wake_up_word','userServ.views.choose_wake_up_word'), # 选择唤醒词
    url(r'^user_serv/choose_voice','userServ.views.choose_voice'), # 选择声音
   	url(r'^user_serv/create_member','userServ.views.create_member'), # 创建家庭成员
    # 天气相关路由
    # 闹钟相关路由

)
