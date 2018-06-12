#coding:utf8
#python编写的百度熊掌号资源提交工具GUI,url一行一个，需单独填appid和token
import requests,time,wx,re
def xiongzhang(event):
    type="realtime" #对提交内容的数据类型说明，新增内容参数：realtime
    content_url=content3.GetValue()  #获取content3里的内容  获取到所有的URL
    content_url=content_url+'\nhttp'  #为了正则匹配到最后一个URL，在最后加上一个换行和http
    urls=re.findall('(.*?)\s+',content_url)  #正则获取所有URL为一个列表
    tuisong_urls='\n'.join(urls)  #把这个列表中所有的URL以换行做分隔。
    # print tuisong_urls
    appid=content1.GetValue()  #获取content1里的内容即：appid
    appid=str(appid).strip()  #如果前后有空格去掉空格
    token=content2.GetValue() #获取content2里的内容即：token
    token=str(token).strip()  #如果前后有空格去掉空格
    post_url="http://data.zz.baidu.com/urls?appid=%s&token=%s&type=%s"%(appid,token,type)  #接口调用地址 熊掌号-资讯提交页面获取
    # filecontents={'file':open('urls.txt','r')}  #如果把所有urls放到本地的urls.txt里每行一个，则用这种方法来推送
    # r=requests.post(post_url,files=filecontents)
    r=requests.post(post_url,data=tuisong_urls)  #开始推送
    if r:
        result=r.text.decode('utf8')
        # print result
        if 'success' in result:
            x=re.findall('"success_realtime":(\d+),"remain_realtime":(\d+)',result)
            success_realtime=str(x[0][0]) #成功推送的url条数
            remain_realtime=str(x[0][1])  #今天剩余可推送的url条数
            result_content='\n推送完成：\n成功推送的url条数:'+success_realtime+'\n今天剩余可推送的url条数:'+remain_realtime
            print result_content
            # content3.Clear() #清空内容
            # content3.SetValue(result_content)   #结果填充到content3中，覆盖式的
            wx.MessageBox(result_content)  #弹出消息
            # content3.AppendText(result_content)  #结果填充到content3中，非覆盖，在最后一行添加
        else:
            print result
    else:
        result_erro='\n推送失败,请检查 appid 和 token是否正确'
        # content3.SetValue(result_erro)
        wx.MessageBox(result_erro)   #弹出消息

if __name__=="__main__":
    app=wx.App()
    win=wx.Frame(None,title="【百度熊掌号URL批量提交工具】    开发者:李亚涛 私人微信:841483350".decode('utf8'),size=(850,700))
    icon=wx.Icon('favicon.ico',wx.BITMAP_TYPE_ICO)
    win.SetIcon(icon)
    win.Show()
    wx.StaticText(win,label="appid（您的熊掌号唯一识别ID）:",pos=(5,10),size=(200,30))
    content1=wx.TextCtrl(win,pos=(210,5),size=(150,30),style = wx.TE_MULTILINE | wx.TE_RICH)

    wx.StaticText(win,label="token(推送准入密钥):",pos=(370,10),size=(120,30))
    content2=wx.TextCtrl(win,pos=(500,5),size=(200,30),style=wx.TE_MULTILINE|wx.TE_RICH)


    wx.StaticText(win,label="请在下方填入URL，一行一个:",pos=(100,40),size=(200,30))
    content3=wx.TextCtrl(win,pos=(100,70),size=(590,600),style=wx.TE_MULTILINE|wx.TE_RICH)
    loadButton=wx.Button(win,label='提交'.decode('utf8'),pos=(710,5),size=(50,30))
    loadButton.Bind(wx.EVT_BUTTON,xiongzhang)  #这个按钮绑定xiongzhang这个函数

    app.MainLoop()
    # appid="xxx"  #在站长平台后台获取appid 	是 	stringo类型 	您的熊掌号唯一识别ID
    # token="xxx"  #在搜索资源平台申请的推送用的准入密钥
    # type="realtime" #对提交内容的数据类型说明，新增内容参数：realtime
    xiongzhang()
    # raw_input()



