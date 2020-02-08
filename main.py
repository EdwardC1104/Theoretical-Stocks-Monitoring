import yfinance as yf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import tkinter.font as tkFont
from datetime import datetime
import json

with open('settings.json') as settings:
    input_data = json.load(settings)
    stockA = input_data["stockA"]
    stockB = input_data["stockB"]
    stockC = input_data["stockC"]
    stockD = input_data["stockD"]

today = datetime.today().strftime('%Y-%m-%d')
stockAData = yf.download(stockA[1], '2020-01-01', today)
stockBData = yf.download(stockB[1], '2020-01-01', today)
stockCData = yf.download(stockC[1], '2020-01-01', today)
stockDData = yf.download(stockD[1], '2020-01-01', today)

originalInvestment = int(stockA[2]) * stockAData.Close[0] + int(stockB[2]) * stockBData.Close[0]
originalInvestment += int(stockC[2]) * stockCData.Close[0] + int(stockD[2]) * stockDData.Close[0]

profit = int(stockA[2]) * stockAData.Close[-1] + int(stockB[2]) * stockBData.Close[-1]
profit += int(stockC[2]) * stockCData.Close[-1] + int(stockD[2]) * stockDData.Close[-1] - originalInvestment

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


        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame)
        self.canvas.get_tk_widget().grid(column=0, row=1, sticky='WE', pady=2, padx=3, rowspan=4)
        ax.plot(stockAData.Close, marker='o', markerfacecolor=stockA[3], markersize=5, color=stockA[3], linewidth=2, label=stockA[0])
        ax.plot(stockBData.Close, marker='o', markerfacecolor=stockB[3], markersize=5, color=stockB[3], linewidth=2, label=stockB[0])
        ax.plot(stockCData.Close, marker='o', markerfacecolor=stockC[3], markersize=5, color=stockC[3], linewidth=2, label=stockC[0])
        ax.plot(stockDData.Close, marker='o', markerfacecolor=stockD[3], markersize=5, color=stockD[3], linewidth=2, label=stockD[0])
        ax.legend()
        fig.autofmt_xdate()


        self.stockAName = tk.Label(self.frame, font=self.customFont, text=stockA[0])
        self.stockAName.grid(column=1, row=1, sticky='WE', pady=2, padx=3)

        self.stockANumber = tk.Entry(self.frame, font=self.customFont)
        self.stockANumber.insert(0, stockA[2])
        self.stockANumber.grid(column=2, row=1, sticky='WE', pady=2, padx=3)

        self.stockAValue = tk.Label(self.frame, font=self.customFont, text=str(round(stockAData.Close[-1],2)))
        self.stockAValue.grid(column=3, row=1, sticky='WE', pady=2, padx=3)

        self.stockAGrowth = tk.Label(self.frame, font=self.customFont, text=str(round((stockAData.Close[-1]/stockAData.Close[0]*100-100),2)) + "%")
        self.stockAGrowth.grid(column=4, row=1, sticky='WE', pady=2, padx=3)



        self.stockBName = tk.Label(self.frame, font=self.customFont, text=stockB[0])
        self.stockBName.grid(column=1, row=2, sticky='WE', pady=2, padx=3)

        self.stockBNumber = tk.Entry(self.frame, font=self.customFont)
        self.stockBNumber.insert(0, stockB[2])
        self.stockBNumber.grid(column=2, row=2, sticky='WE', pady=2, padx=3)

        self.stockBValue = tk.Label(self.frame, font=self.customFont, text=str(round(stockBData.Close[-1],2)))
        self.stockBValue.grid(column=3, row=2, sticky='WE', pady=2, padx=3)

        self.stockBGrowth = tk.Label(self.frame, font=self.customFont, text=str(round((stockBData.Close[-1]/stockBData.Close[0]*100-100),2)) + "%")
        self.stockBGrowth.grid(column=4, row=2, sticky='WE', pady=2, padx=3)



        self.stockCName = tk.Label(self.frame, font=self.customFont, text=stockC[0])
        self.stockCName.grid(column=1, row=3, sticky='WE', pady=2, padx=3)

        self.stockCNumber = tk.Entry(self.frame, font=self.customFont)
        self.stockCNumber.insert(0, stockC[2])
        self.stockCNumber.grid(column=2, row=3, sticky='WE', pady=2, padx=3)

        self.stockCValue = tk.Label(self.frame, font=self.customFont, text=str(round(stockCData.Close[-1],2)))
        self.stockCValue.grid(column=3, row=3, sticky='WE', pady=2, padx=3)

        self.stockCGrowth = tk.Label(self.frame, font=self.customFont, text=str(round((stockCData.Close[-1]/stockCData.Close[0]*100-100),2)) + "%")
        self.stockCGrowth.grid(column=4, row=3, sticky='WE', pady=2, padx=3)



        self.stockDName = tk.Label(self.frame, font=self.customFont, text=stockD[0])
        self.stockDName.grid(column=1, row=4, sticky='WE', pady=2, padx=3)

        self.stockDNumber = tk.Entry(self.frame, font=self.customFont)
        self.stockDNumber.insert(0, stockD[2])
        self.stockDNumber.grid(column=2, row=4, sticky='WE', pady=2, padx=3)

        self.stockDValue = tk.Label(self.frame, font=self.customFont, text=str(round(stockDData.Close[-1],2)))
        self.stockDValue.grid(column=3, row=4, sticky='WE', pady=2, padx=3)

        self.stockDGrowth = tk.Label(self.frame, font=self.customFont, text=str(round((stockDData.Close[-1]/stockDData.Close[0]*100-100),2)) + "%")
        self.stockDGrowth.grid(column=4, row=4, sticky='WE', pady=2, padx=3)



        self.profitLabel = tk.Label(self.frame, font=self.customFont, text="Profit: £" + str(round(profit, 2)))
        self.profitLabel.grid(column=0, row=5, sticky='W', pady=2, padx=3)

        self.currentAccountLabel = tk.Label(self.frame, font=self.customFont, text="Current Account: £" + str(0))
        self.currentAccountLabel.grid(column=0, row=6, sticky='W', pady=2, padx=3)

        self.originalInvestmentLabel = tk.Label(self.frame, font=self.customFont, text="Original Investment: £" + str(round(originalInvestment, 2)))
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
