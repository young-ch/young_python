import win32com.client

class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행':'A000100'}


    def GetCount(self):
        return len(self.stocks)

    def NameToCode(self,name):
        return self.stocks[name]

instStockCheart = win32com.client.Dispatch("CpSysDib.StockChart")


instStockCheart.SetInputValue(0, "A005930") # 종목 코드
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

print(averageVolume)
print(sum(volumes))

if(volumes[0] > averageVolume *10):
    print("대박주")
else:
    print("일반주", volumes[0]/ averageVolume)



#날짜,시가,고가,저가,종가,거래량 출력
#for i in range(numData):
#    for n in range(numField):
#        print(instStockCheart.GetDataValue(n,i), end=' ')
#    print("")

#PER, EPS 데이터 구하기
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")

instMarketEye.setInputValue(0,(4,67,70,111))
instMarketEye.setInputValue(1, 'A035720')

instMarketEye.BlockRequest()

print("현재가: ", instMarketEye.GetDataValue(0, 0))
print("PER: ", instMarketEye.GetDataValue(1, 0))
print("EPS: ", instMarketEye.GetDataValue(2, 0))
print("최근분기년월: ", instMarketEye.GetDataValue(3, 0))

