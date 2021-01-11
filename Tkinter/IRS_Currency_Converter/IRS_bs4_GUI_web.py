#Import packages
import pandas as pd
import requests
import bs4
import tkinter as tk
from tkinter import ttk

class bs4df:
    url_link = 'https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates'

    @classmethod
    def get(cls):
        res = requests.get(cls.url_link)
        res.raise_for_status()
        bs4Soup = bs4.BeautifulSoup(res.text, 'html.parser')
        bs4Soup.find_all('tr')
        irs_list = []
        for tag in bs4Soup.find_all('tr'):
            irs_list.append(tag.getText().replace('\n','-').replace('--','-')
                        .replace('--','-').replace('--','-').strip('-'))
        irs_data = pd.DataFrame(irs_list)
        irs_data = irs_data.join(irs_data[0].str.split('-', expand=True).add_prefix(0))
        irs_data = irs_data.drop(columns=[0, '08'])
        irs_data.columns = irs_data.iloc[0]
        irs_data = irs_data.drop([0])
        irs_data['National_Currency'] = irs_data['Country'] + ' - ' + irs_data['Currency']
        irs_data = irs_data.drop(columns=['Country', 'Currency'])
        irs_data.set_index(['National_Currency'],inplace=True)
        irs_data = irs_data.stack()
        irs_data = irs_data.rename_axis(['National_Currency','Annual_Year']).reset_index()
        irs_data = irs_data.rename(columns={0: "Data"})
        return irs_data

class IRSQuery(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("USD Currency Converter")

        container = ttk.Frame(self)
        container.grid(padx=10, pady=10, sticky="EW")

        frame = IRSQueryGUI(container)  
        frame.grid(row=0, column=0, sticky="NSEW")


class IRSQueryGUI(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.currency_selected = tk.StringVar()
        self.year_selected = tk.StringVar()
        self.data_label_value = tk.StringVar()

#        currency_list = ['Afghanistan - Afghani','Algeria - Dinar','Argentina - Peso','Australia - Dollar',
#                         'Bahrain - Dinar','Brazil - Real','Canada - Dollar','Cayman Islands - Dollar',
#                         'China - Yuan','Denmark - Krone','Egypt - Pound','Euro Zone - Euro','Hong Kong - Dollar',
#                         'Hungary - Forint','Iceland - Krona','India - Rupee','Iraq - Dinar','Israel - New Shekel',
#                         'Japan - Yen','Lebanon - Pound','Mexico - Peso','Morocco - Dirham','New Zealand - Dollar',
#                         'Norway - Kroner','Qatar - Rial','Russia - Rouble','Saudi Arabia - Riyal','Singapore - Dollar',
#                         'South Africa - Rand','South Korean - Won','Sweden - Krona','Switzerland - Franc',
#                         'Taiwan - Dollar','Thailand - Baht','Tunisia - Dinar','Turkey - New Lira',
#                         'United Arab Emirates - Dirham','United Kingdom - Pound']
#        year_list = [2013,2014,2015,2016,2017,2018]

        Currency_Data = bs4df.get()
        self.df = Currency_Data
        currency_list = Currency_Data['National_Currency'].tolist()
        currency_list = list(dict.fromkeys(currency_list))
        year_list = Currency_Data['Annual_Year'].tolist()
        year_list = list(dict.fromkeys(year_list))

        currency_label = ttk.Label(self, text="Select currency")
        currency_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
        currency = ttk.Combobox(self, width=30, textvariable=self.currency_selected, 
                                values = currency_list, state='readonly')
        currency.grid(column=1, row=0, sticky="EW", padx=5, pady=5)

        year_label = ttk.Label(self, text="Select year")
        year_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
        year = ttk.Combobox(self, width=30, textvariable=self.year_selected, 
                                values = year_list, state='readonly')
        year.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

        data_button = ttk.Button(self, text="Convert currency", command=self.calculate_data)
        data_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)
        
        data_label = ttk.Label(self, textvariable = self.data_label_value)
        self.data_label_value.set("<currency exchange rate printed here>")
        data_label.grid(column=0, row=3, columnspan=2, sticky="EW", padx=5, pady=5)
        
    def calculate_data(self, *args):
        try:
            Currency_Selected = self.currency_selected.get()
            Year_Selected = self.year_selected.get()
            Currency_Data = self.df
            df = Currency_Data[(Currency_Data['National_Currency']==Currency_Selected) & 
                               (Currency_Data['Annual_Year']==Year_Selected)]
            self.data_label_value.set('Currency units in terms of USD: ' + '%.3f' % float(df.iat[0,2]))
        except:
            self.data_label_value.set('<Please select a currency and a year>')

root = IRSQuery()
root.mainloop()
