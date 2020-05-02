import win32com.client

class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행':'A000100'}


    def GetCount(self):
        return len(self.stocks)

    def NameToCode(self,name):
        return self.stocks[name]

def get_ItemName(code):
    instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

    for i in range(instCpStockCode.GetCount()):

        if instCpStockCode.GetData(0, i) == code:
            return instCpStockCode.GetData(1, i)

def input_stockItem():
        while True:

            str = input("종목명 입력하세요 : ")
            item = str.strip()

            instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

            for i in range(instCpStockCode.GetCount()):

                if instCpStockCode.GetData(1, i) == item:
                    item_num = instCpStockCode.GetData(0, i)


            Big_volume(item_num)


def Big_volume(stockItem):

    instStockCheart = win32com.client.Dispatch("CpSysDib.StockChart")


    instStockCheart.SetInputValue(0, stockItem) # 종목 코드
    instStockCheart.SetInputValue(1, ord('2'))
    instStockCheart.SetInputValue(4, 60) #최근 60일 거래 데이터
    #instStockCheart.SetInputValue(5, (0,2,3,4,5,8))#날짜,시가,고가,저가,종가,거래량 나타내기
    instStockCheart.SetInputValue(5, 8)
    instStockCheart.SetInputValue(6, ord('D'))
    instStockCheart.SetInputValue(9, ord('1'))

    # BlockRequest API 보내기
    instStockCheart.BlockRequest()

    #GetData
    volumes = []
    numData = instStockCheart.GetHeaderValue(3)
    numField = instStockCheart.GetHeaderValue(1)

    for i in range(numData):
        volume = instStockCheart.GetDataValue(0,i)
        volumes.append(volume)

    averageVolume = (sum(volumes) - volumes[0]) / (len(volumes) -1)

    if(volumes[0] > averageVolume *10):
        print("대박주 " )
    else:
        print("일반주 ", volumes[0] / averageVolume)

# 거래량 폭증한 종목 조회하기.
def CheckVolumn(instStockCheart, code):

    #SetInputValue
    instStockCheart.SetInputValue(0, code)
    instStockCheart.SetInputValue(1, ord('2'))
    instStockCheart.SetInputValue(4, 60)
    instStockCheart.SetInputValue(5, 8)
    instStockCheart.SetInputValue(6, ord('D'))
    instStockCheart.SetInputValue(9, ord('1'))

    # BlockRequest API 보내기
    instStockCheart.BlockRequest()

    #GetData
    volumes = []
    numData = instStockCheart.GetHeaderValue(3)
    for i in range(numData):
        volume = instStockCheart.GetDataValue(0,i)
        volumes.append(volume)

    averageVolume = (sum(volumes) - volumes[0]) / (len(volumes) - 1)

    if (volumes[0] > averageVolume * 10):
        return 1
    else:
        return 0

#PER, EPS 조회 함수
def get_Stock_Info(codeName):

    instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
    instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")
    for i in range(instCpStockCode.GetCount()):

        if instCpStockCode.GetData(1, i) == codeName:
            item_num = instCpStockCode.GetData(0, i)

    instMarketEye.setInputValue(0, (4, 67, 70, 111))
    instMarketEye.setInputValue(1, item_num)

    instMarketEye.BlockRequest()

    print("현재가: ", instMarketEye.GetDataValue(0, 0))
    print("PER: ", instMarketEye.GetDataValue(1, 0))
    print("EPS: ", instMarketEye.GetDataValue(2, 0))
    print("최근분기년월: ", instMarketEye.GetDataValue(3, 0))