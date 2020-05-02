import win32com.client



instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
print(instCpStockCode.GetCount())

stock_list = []
instCpStockCode =win32com.client.Dispatch("CpUtil.CpStockCode")

for i in range(instCpStockCode.GetCount()):

    if instCpStockCode.GetData(1,i) == 'NAVER':
        print(instCpStockCode.GetData(1,i))
        print(instCpStockCode.GetData(0,i))
        print(i)
    #print(instCpStockCode.GetData(1,i))

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
codeList = instCpCodeMgr.GetStockListByMarket(1)

kosip = {}
for code in codeList:
    name = instCpCodeMgr.CodeToName(code)
    kosip[code] = name

f= open('kospi_list.csv','w')
for key, value in kosip.items():
    f.write("%s,%s\n" %(key, value))

f.close()




