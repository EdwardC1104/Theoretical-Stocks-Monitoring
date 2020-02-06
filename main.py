import yfinance as yf
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.font as tkFont
from datetime import datetime

class mainWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.customFont = tkFont.Font(family="Helvetica", size=12)

        self.title = tk.Label(self.frame, font=self.customFont, text="Your Stock Performance")
        self.title.grid(column=0, row=0, sticky ='WE', pady=2, padx=3)

        self.columnHeader1 = tk.Label(self.frame, font=self.customFont, text="Stock Name")
        self.columnHeader1.grid(column=1, row=0, sticky ='WE', pady=2, padx=3)

        self.columnHeader2 = tk.Label(self.frame, font=self.customFont, text="Shares")
        self.columnHeader2.grid(column=2, row=0, sticky ='WE', pady=2, padx=3)

        self.columnHeader3 = tk.Label(self.frame, font=self.customFont, text="Share Price")
        self.columnHeader3.grid(column=3, row=0, sticky ='WE', pady=2, padx=3)

        self.columnHeader4 = tk.Label(self.frame, font=self.customFont, text="% Growth")
        self.columnHeader4.grid(column=4, row=0, sticky ='WE', pady=2, padx=3)

        self.graph = tk.Label(self.frame, font=self.customFont, text="[GRAPH]")
        self.graph.grid(column=0, row=1, sticky='WE', pady=2, padx=3, rowspan=4)



        self.stockAName = tk.Label(self.frame, font=self.customFont, text="[NAME]")
        self.stockAName.grid(column=1, row=1, sticky='WE', pady=2, padx=3)

        self.stockANumber = tk.Entry(self.frame, font=self.customFont)
        self.stockANumber.insert(0, '[NUMBER]')
        self.stockANumber.grid(column=2, row=1, sticky='WE', pady=2, padx=3)

        self.stockAValue = tk.Label(self.frame, font=self.customFont, text="[VALUE]")
        self.stockAValue.grid(column=3, row=1, sticky='WE', pady=2, padx=3)

        self.stockAGrowth = tk.Label(self.frame, font=self.customFont, text="[GROWTH]")
        self.stockAGrowth.grid(column=4, row=1, sticky='WE', pady=2, padx=3)



        self.stockBName = tk.Label(self.frame, font=self.customFont, text="[NAME]")
        self.stockBName.grid(column=1, row=2, sticky='WE', pady=2, padx=3)

        self.stockBNumber = tk.Entry(self.frame, font=self.customFont)
        self.stockBNumber.insert(0, '[NUMBER]')
        self.stockBNumber.grid(column=2, row=2, sticky='WE', pady=2, padx=3)

        self.stockBValue = tk.Label(self.frame, font=self.customFont, text="[VALUE]")
        self.stockBValue.grid(column=3, row=2, sticky='WE', pady=2, padx=3)

        self.stockBGrowth = tk.Label(self.frame, font=self.customFont, text="[GROWTH]")
        self.stockBGrowth.grid(column=4, row=2, sticky='WE', pady=2, padx=3)



        self.stockCName = tk.Label(self.frame, font=self.customFont, text="[NAME]")
        self.stockCName.grid(column=1, row=3, sticky='WE', pady=2, padx=3)

        self.stockCNumber = tk.Entry(self.frame, font=self.customFont)
        self.stockCNumber.insert(0, '[NUMBER]')
        self.stockCNumber.grid(column=2, row=3, sticky='WE', pady=2, padx=3)

        self.stockCValue = tk.Label(self.frame, font=self.customFont, text="[VALUE]")
        self.stockCValue.grid(column=3, row=3, sticky='WE', pady=2, padx=3)

        self.stockCGrowth = tk.Label(self.frame, font=self.customFont, text="[GROWTH]")
        self.stockCGrowth.grid(column=4, row=3, sticky='WE', pady=2, padx=3)



        self.stockDName = tk.Label(self.frame, font=self.customFont, text="[NAME]")
        self.stockDName.grid(column=1, row=4, sticky='WE', pady=2, padx=3)

        self.stockDNumber = tk.Entry(self.frame, font=self.customFont)
        self.stockDNumber.insert(0, '[NUMBER]')
        self.stockDNumber.grid(column=2, row=4, sticky='WE', pady=2, padx=3)

        self.stockDValue = tk.Label(self.frame, font=self.customFont, text="[VALUE]")
        self.stockDValue.grid(column=3, row=4, sticky='WE', pady=2, padx=3)

        self.stockDGrowth = tk.Label(self.frame, font=self.customFont, text="[GROWTH]")
        self.stockDGrowth.grid(column=4, row=4, sticky='WE', pady=2, padx=3)



        self.profitLabel = tk.Label(self.frame, font=self.customFont, text="Profit: £" + str(0))
        self.profitLabel.grid(column=0, row=5, sticky='W', pady=2, padx=3)

        self.currentAccountLabel = tk.Label(self.frame, font=self.customFont, text="Current Account: £" + str(0))
        self.currentAccountLabel.grid(column=0, row=6, sticky='W', pady=2, padx=3)

        self.originalInvestmentLabel = tk.Label(self.frame, font=self.customFont, text="Original Investment: £" + str(1000))
        self.originalInvestmentLabel.grid(column=0, row=7, sticky='W', pady=2, padx=3)



        self.refreshButton = tk.Button(self.frame, font=self.customFont, text='Refresh', command=self.refresh)
        self.refreshButton.grid(column=3, row=7, sticky ='WE', pady=2, padx=3)

        self.resetButton = tk.Button(self.frame, font=self.customFont, text='Reset', command=self.reset)
        self.resetButton.grid(column=4, row=7, sticky='WE', pady=2, padx=3)

    def refresh(self):
        print('Refresh')

    def reset(self):
        print('Reset')

def main():
    root = tk.Tk()
    root.title("Theoretical Stocks Monitoring")
    app = mainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()

"""
today = datetime.today().strftime('%Y-%m-%d')
stockAData = yf.download('AMD', '2020-01-01', today)
stockBData = yf.download('INTC', '2020-01-01', today)
stockCData = yf.download('MSFT', '2020-01-01', today)
stockDData = yf.download('FB', '2020-01-01', today)

plt.style.use('seaborn-darkgrid')

plt.plot(stockAData.Close, marker='o', markerfacecolor='red', markersize=5, color='red', linewidth=2, label="AMD")
plt.plot(stockBData.Close, marker='o', markerfacecolor='blue', markersize=5, color='blue', linewidth=2, label="Intel")
plt.plot(stockCData.Close, marker='o', markerfacecolor='skyblue', markersize=5, color='skyblue', linewidth=2, label="Microsoft")
plt.plot(stockDData.Close, marker='o', markerfacecolor='purple', markersize=5, color='purple', linewidth=2, label="FaceBook")

plt.legend()
plt.show()
"""