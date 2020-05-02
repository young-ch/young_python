import Big_volume_algorithm
import PER_Analysis_COB
import win32com.client
import time



def run():
    instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

    codeList = instCpCodeMgr.GetStockListByMarket(1)

    buyList = []

    while True:
        print("1. 거래량 급등 조회")
        print("2. 종목 PER,EPS 조회")
        print("3. 종목으로 거래량(60일) 확인")
        print("4. 업종별 Per")


        Gubun = int(input("사용하실 목록 선택 : "))
        if Gubun == 1:
            for code in codeList:
                if Big_volume_algorithm.CheckVolumn(instStockChart, code) == 1:
                    buyList.append(code)
                    print(code, Big_volume_algorithm.get_ItemName(code))
                time.sleep(1)

        elif Gubun == 2:
            str = input("조회하실 종목명 : ")
            codeName = str.strip()
            Big_volume_algorithm.get_Stock_Info(codeName)

        elif Gubun == 3:
            Big_volume_algorithm.input_stockItem()

        elif Gubun == 4:
            PER_Analysis_COB.get_All_COB()


        elif Gubun == 10:
            print("사용 종료.")
            break











if __name__ == "__main__":
    run()
