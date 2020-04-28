

class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행':'A000100'}

    def GetCount(self): #주식 종목수를 리턴하는 메서
        return len(self.stocks)

    def NameToCode(self, name): #종목명을 입력하면 해당 종목에 대한 종목 코드를 리턴
        return self.stocks[name]





