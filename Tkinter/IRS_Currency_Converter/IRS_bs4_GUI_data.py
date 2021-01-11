#Import packages
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk

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

        currency_list = ['Afghanistan - Afghani','Algeria - Dinar','Argentina - Peso','Australia - Dollar',
                         'Bahrain - Dinar','Brazil - Real','Canada - Dollar','Cayman Islands - Dollar',
                         'China - Yuan','Denmark - Krone','Egypt - Pound','Euro Zone - Euro','Hong Kong - Dollar',
                         'Hungary - Forint','Iceland - Krona','India - Rupee','Iraq - Dinar','Israel - New Shekel',
                         'Japan - Yen','Lebanon - Pound','Mexico - Peso','Morocco - Dirham','New Zealand - Dollar',
                         'Norway - Kroner','Qatar - Rial','Russia - Rouble','Saudi Arabia - Riyal','Singapore - Dollar',
                         'South Africa - Rand','South Korean - Won','Sweden - Krona','Switzerland - Franc',
                         'Taiwan - Dollar','Thailand - Baht','Tunisia - Dinar','Turkey - New Lira',
                         'United Arab Emirates - Dirham','United Kingdom - Pound']
        year_list = [2013,2014,2015,2016,2017,2018]

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
            National_Currency = ['Afghanistan - Afghani','Afghanistan - Afghani','Afghanistan - Afghani','Afghanistan - Afghani','Afghanistan - Afghani','Afghanistan - Afghani','Algeria - Dinar','Algeria - Dinar','Algeria - Dinar','Algeria - Dinar','Algeria - Dinar','Algeria - Dinar','Argentina - Peso','Argentina - Peso','Argentina - Peso','Argentina - Peso','Argentina - Peso','Argentina - Peso','Australia - Dollar','Australia - Dollar','Australia - Dollar','Australia - Dollar','Australia - Dollar','Australia - Dollar','Bahrain - Dinar','Bahrain - Dinar','Bahrain - Dinar','Bahrain - Dinar','Bahrain - Dinar','Bahrain - Dinar','Brazil - Real','Brazil - Real','Brazil - Real','Brazil - Real','Brazil - Real','Brazil - Real','Canada - Dollar','Canada - Dollar','Canada - Dollar','Canada - Dollar','Canada - Dollar','Canada - Dollar','Cayman Islands - Dollar','Cayman Islands - Dollar','Cayman Islands - Dollar','Cayman Islands - Dollar','Cayman Islands - Dollar','Cayman Islands - Dollar','China - Yuan','China - Yuan','China - Yuan','China - Yuan','China - Yuan','China - Yuan','Denmark - Krone','Denmark - Krone','Denmark - Krone','Denmark - Krone','Denmark - Krone','Denmark - Krone','Egypt - Pound','Egypt - Pound','Egypt - Pound','Egypt - Pound','Egypt - Pound','Egypt - Pound','Euro Zone - Euro','Euro Zone - Euro','Euro Zone - Euro','Euro Zone - Euro','Euro Zone - Euro','Euro Zone - Euro','Hong Kong - Dollar','Hong Kong - Dollar','Hong Kong - Dollar','Hong Kong - Dollar','Hong Kong - Dollar','Hong Kong - Dollar','Hungary - Forint','Hungary - Forint','Hungary - Forint','Hungary - Forint','Hungary - Forint','Hungary - Forint','Iceland - Krona','Iceland - Krona','Iceland - Krona','Iceland - Krona','Iceland - Krona','Iceland - Krona','India - Rupee','India - Rupee','India - Rupee','India - Rupee','India - Rupee','India - Rupee','Iraq - Dinar','Iraq - Dinar','Iraq - Dinar','Iraq - Dinar','Iraq - Dinar','Iraq - Dinar','Israel - New Shekel','Israel - New Shekel','Israel - New Shekel','Israel - New Shekel','Israel - New Shekel','Israel - New Shekel','Japan - Yen','Japan - Yen','Japan - Yen','Japan - Yen','Japan - Yen','Japan - Yen','Lebanon - Pound','Lebanon - Pound','Lebanon - Pound','Lebanon - Pound','Lebanon - Pound','Lebanon - Pound','Mexico - Peso','Mexico - Peso','Mexico - Peso','Mexico - Peso','Mexico - Peso','Mexico - Peso','Morocco - Dirham','Morocco - Dirham','Morocco - Dirham','Morocco - Dirham','Morocco - Dirham','Morocco - Dirham','New Zealand - Dollar','New Zealand - Dollar','New Zealand - Dollar','New Zealand - Dollar','New Zealand - Dollar','New Zealand - Dollar','Norway - Kroner','Norway - Kroner','Norway - Kroner','Norway - Kroner','Norway - Kroner','Norway - Kroner','Qatar - Rial','Qatar - Rial','Qatar - Rial','Qatar - Rial','Qatar - Rial','Qatar - Rial','Russia - Rouble','Russia - Rouble','Russia - Rouble','Russia - Rouble','Russia - Rouble','Russia - Rouble','Saudi Arabia - Riyal','Saudi Arabia - Riyal','Saudi Arabia - Riyal','Saudi Arabia - Riyal','Saudi Arabia - Riyal','Saudi Arabia - Riyal','Singapore - Dollar','Singapore - Dollar','Singapore - Dollar','Singapore - Dollar','Singapore - Dollar','Singapore - Dollar','South Africa - Rand','South Africa - Rand','South Africa - Rand','South Africa - Rand','South Africa - Rand','South Africa - Rand','South Korean - Won','South Korean - Won','South Korean - Won','South Korean - Won','South Korean - Won','South Korean - Won','Sweden - Krona','Sweden - Krona','Sweden - Krona','Sweden - Krona','Sweden - Krona','Sweden - Krona','Switzerland - Franc','Switzerland - Franc','Switzerland - Franc','Switzerland - Franc','Switzerland - Franc','Switzerland - Franc','Taiwan - Dollar','Taiwan - Dollar','Taiwan - Dollar','Taiwan - Dollar','Taiwan - Dollar','Taiwan - Dollar','Thailand - Baht','Thailand - Baht','Thailand - Baht','Thailand - Baht','Thailand - Baht','Thailand - Baht','Tunisia - Dinar','Tunisia - Dinar','Tunisia - Dinar','Tunisia - Dinar','Tunisia - Dinar','Tunisia - Dinar','Turkey - New Lira','Turkey - New Lira','Turkey - New Lira','Turkey - New Lira','Turkey - New Lira','Turkey - New Lira','United Arab Emirates - Dirham','United Arab Emirates - Dirham','United Arab Emirates - Dirham','United Arab Emirates - Dirham','United Arab Emirates - Dirham','United Arab Emirates - Dirham','United Kingdom - Pound','United Kingdom - Pound','United Kingdom - Pound','United Kingdom - Pound','United Kingdom - Pound','United Kingdom - Pound']
            Annual_Year = [2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013,2018,2017,2016,2015,2014,2013]
            Data_Value = [73.598,71.086,70.645,63.653,59.771,57.822,117.409,115.876,114.431,104.883,84.242,83.339,28.167,17.227,15.359,9.617,8.448,5.704,1.34,1.358,1.4,1.345,1.154,1.078,0.395,0.395,0.395,0.395,0.394,0.395,3.655,3.322,3.632,3.468,2.451,2.249,1.297,1.35,1.379,1.329,1.149,1.071,0.833,0.884,0.886,0.885,0.883,0.873,6.62,7.03,6.91,6.489,6.394,6.446,6.319,6.864,7,6.991,5.844,5.843,17.809,18.586,10.462,8.044,7.399,7.185,0.848,0.923,0.94,0.937,0.784,0.783,7.838,8.105,8.073,8.062,8.065,8.067,270.441,285.583,293.083,290.638,242.076,232.771,116.379,111.231,126.256,137.471,121.574,127.323,68.422,67.809,69.956,66.768,63.469,60.936,1193.478,1241.677,1236.453,1231.234,1228.786,1225.266,3.596,3.746,3.997,4.052,3.723,3.759,110.424,116.667,113.138,125.911,110.101,101.517,1511.677,1593.969,1593.639,1588.88,1591.284,1589.155,19.227,19.679,19.435,16.505,13.84,13.275,9.389,10.23,10.279,10.206,8.828,8.829,1.447,1.465,1.494,1.492,1.255,1.27,8.143,8.606,8.745,8.392,6.558,6.117,3.642,3.85,3.791,3.79,3.794,3.796,62.845,60.692,69.685,63.659,40.118,33.165,3.753,3.903,3.903,3.903,3.902,3.901,1.349,1.437,1.437,1.43,1.318,1.302,13.258,13.859,15.319,13.281,11.286,10.037,1100.587,1178.585,1211.121,1179.128,1098.233,1142.933,8.703,8.894,8.91,8.775,7.138,6.78,0.979,1.024,1.025,1.001,0.952,0.964,30.152,31.683,33.586,33.089,31.566,30.945,32.317,35.372,36.778,35.679,33.841,32.027,2.71,2.513,2.237,2.044,1.771,1.695,4.849,3.794,3.146,2.834,2.276,1.982,3.673,3.821,3.821,3.821,3.821,3.821,0.75,0.808,0.77,0.681,0.632,0.665]
            Currency_Tuples = list(zip(National_Currency,Annual_Year,Data_Value))
            Currency_Data = pd.DataFrame(Currency_Tuples, columns = ['National_Currency','Annual_Year','Data_Value'])
#            df = Currency_Data[(Currency_Data['National_Currency']==Currency_Selected) & 
#                               (Currency_Data['Annual_Year']==Year_Selected)]
            df = Currency_Data[(Currency_Data['National_Currency']==Currency_Selected) & 
                               (Currency_Data['Annual_Year']==int(Year_Selected))]
            self.data_label_value.set('Currency units in terms of USD: ' + '%.3f' % df.iat[0,2])
        except:
            self.data_label_value.set('<Please select a currency and a year>')

root = IRSQuery()
root.mainloop()
