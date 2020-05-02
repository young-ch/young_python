import win32com.client

#업종별 코드에 해당하는 업종명 출력
def get_All_COB():
    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    industryCodeList = instCpCodeMgr.GetIndustryList()

    for industryCode in industryCodeList:
        print(industryCode, instCpCodeMgr.GetIndustryName(industryCode))

    COB_NUM = int(input("조회하실 업종 선택 : "))
    get_Cotegory_codeName(COB_NUM)

def get_Cotegory_codeName(COB_NUM):
    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")


    tarketCodeList = instCpCodeMgr.GetGroupCodeList(COB_NUM)

    #Get PER
    instMarketEye.SetInputValue(0, 67)
    instMarketEye.SetInputValue(1, tarketCodeList)

    instMarketEye.BlockRequest()

    # GetHeaderValue
    numStock = instMarketEye.GetHeaderValue(2)



    # Get Data
    sumPer = 0

    for i in range(sumPer):
        sumPer += instMarketEye.GetDataValue(0,i)

        print("Average PER : ", sumPer/numStock)

    #for code in tarketCodeList:
     #   print(code, instCpCodeMgr.CodeToName(code))


