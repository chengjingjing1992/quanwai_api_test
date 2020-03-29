import requests

from jsonpath_rw import jsonpath,parse

if __name__ == '__main__':
    response_data={
    "code":0,
    "message":"Success",
    "result":[
        {
            "address":"",
            "audioRiseMember":None,
            "coreRiseMembers":None,
            "country":"",
            "email":"",
            "expireDate":None,
            "function":"",
            "headImgUrlCheckTime":None,
            "headimgurl":"https://thirdwx.qlogo.cn/mmopen/A1epQTdErlH04iaVCDdHtUdsPKrKgDr1BCM5mzhlQDRKHHI5cI9M0BPK40WHkkS2ZrqjjSQKtIOBUFNSVibLwMvTRLbTlNdnhO/132",
            "id":196597,
            "industry":"",
            "isFull":0,
            "learningNotify":None,
            "memberId":"Q1911014",
            "mobileNo":"",
            "nickname":"手",
            "openApplication":None,
            "openConsolidation":None,
            "openNavigator":None,
            "openRise":None,
            "openWelcome":None,
            "openid":"",
            "partner":None,
            "point":0,
            "realName":"",
            "receiver":"",
            "requestCommentCount":0,
            "riseId":"5z5x5c",
            "riseMember":0,
            "role":0,
            "signature":"",
            "unionid":"",
            "weMini2OpenId":"",
            "weMiniOpenId":"",
            "weixinId":"",
            "workingLife":"",
            "workingYear":""
        }
    ]
}
    depend_data="result[0].id"
    json_exe = parse(depend_data)
    madle = json_exe.find(response_data)
    list = [math.value for math in madle]
    print(list)
    print("list=====", list[0])

# 本金
a=130000
# 期数
b=60
# 月综合利率
c=5.88/12/100
print((1/b+c)*a)
yu=3310
print((yu/130000-1/60)*100)

yue=3610
print((yue/610000-1/360)*100)
yue1=8029

print(print((yue1/90000-1/12)*100))

