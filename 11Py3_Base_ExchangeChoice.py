'''
BasePage 11:

In file 10 we continued with out live plot from a bitcoin trading website.
    File 10 was simple, we added a popup window that came up when you selected a choice from a dropdown menu.

Here in file 11

1) In the class SeaofBTCapp we added a new main selection to the menu bar, and 4 sub selections to that
        Our initial plot uses data from a U.S. bitcoin trader
        The new 4 sub selections will be used to plot foreign bitcoin traders.
        That will be tied together in later files.

2) The sub selections will be using a global method that we need to create up top
3) Created the     changeExchange     method, and several global variables that will be user later.

4) What we have created was simple, and does not do anything yet in this file.

'''

import urllib
import json
# Terminal/CMD (we are on mac)
#   pip install pandas
#   pip install numpy
import pandas as pd
import numpy as np

# ==================================================
import tkinter as tk
from tkinter import ttk
'''
Terminal/CMD     pip install matplotlib
'''
import matplotlib
# This (below) lets us "change the back ground"
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

from matplotlib import pyplot as plt

# ==================================================
style.use("ggplot")
LARGE_FONT = ("Verdana", 12)  # Base font that we want to use and will call
NORM_FONT = ("Verdana", 10)  # Base font that we want to use and will call
SMALL_FONT = ("Verdana", 18)  # Base font that we want to use and will call

# ==================================================
# This will change the size of the graph. Customize based on data and wants
f = Figure(figsize=(10, 6), dpi=100)  # Cut from GraphPage
a = f.add_subplot(111)  # Cut from GraphPage   # 111 means 1x1 on chart 1



# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-

exchange = "BTC-e"
datCounter = 9000
programName = "btce"

def changeExchange(toWhat, pn):
    global exchange
    global datCounter
    global programName

    exchange = toWhat
    programName = pn
    datCounter = 9000

# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-
# -NEW-NEW-NEW-


# To get the popup window:
#       Run program: StartPage:  TradingPage:   Agree:  File:  Save Settings
def popupmsg(msg):
    # Create popup window, and set it's geometry
    popup = tk.Tk()
    popup.geometry("400x100")

    # Set the popup window title
    popup.wm_title("Title on top of File: Save Settings: popup")
    # Set a label in the popup window
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    # Set a button in the popup window with a command to destroy popup window
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()

# ==================================================
# This is the new animate function which pulls live trading data from btc-e.com for our plot
# Specific directions up top ^^^
# This is the direct link, but we want to add a parameter, how many trades.
#       The site limit is 2000 for us to capture
#       To add a parameter use:     ' ?parameterName=parameterValue '
# datalink1 = "https://btc-e.com/api/3/trades/btc_usd"

def animate(i):  # animate function with  'i' for interval
    # Note: The request is giving us a pseudo error. It works, but pycharm is overreacting.

    dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
    data = urllib.request.urlopen(dataLink)
    data = data.readline().decode("utf-8")
    data = json.loads(data)

    data = data["btc_usd"]  # Refers to the whole data set read in (seen below)
    # Now use pandas to organize the 2000 rows of data we are bringing in.
    data = pd.DataFrame(data)

    # Separating our json data being pulled in (seen below).
    buys1 = data[(data["type"] == "bid")]
    # Now need to convert the unix timestamp. matplotlib does not recognize this.
    buys1["datestamp"] = np.array(buys1["timestamp"]).astype("datetime64[s]")
    buyDates1 = (buys1["datestamp"]).tolist()

    # Separating our json data being pulled in (seen below).
    sells1 = data[(data["type"] == "ask")]
    # Now need to convert the unix timestamp. matplotlib does not recognize this.
    sells1["datestamp"] = np.array(sells1["timestamp"]).astype("datetime64[s]")
    sellDates1 = (sells1["datestamp"]).tolist()

    a.clear()
    # Plot the data points, and turn them into colored-labeled lines.
    a.plot_date(buyDates1, buys1["price"], "g", label="buys")
    a.plot_date(sellDates1, sells1["price"], "#00A3E0", label="sells")
    # Legend lets us specifically place our line labels in the top left
    # Default they are put on the graph and will be covered up if the lines go over them.
    a.legend(bbox_to_anchor=(0,1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
    # Plot title with a live update of the last price from the most recent data set.
    title = "BTC-e BTCUSD Prices\nLast Price: " + str(data["price"][1999])
    a.set_title(title)
    # -------------------------------------------------------

'''
-------------------------------------------------------
    THESE ARE REAL DAILY BIDS 12:16PM 7/7/2017
    THIS IS THE JSON info that we will be pulling from.
    It has a unix timestamp
-------------------------------------------------------
    {"btc_usd":[{"type":"ask","price":2474.869,"amount":0.15496925,"tid":110941553,"timestamp":1499451300},{"type":"ask","price":2475.259,"amount":0.09,"tid":110941552,"timestamp":1499451300},
    {"type":"ask","price":2475.261,"amount":0.00527802,"tid":110941551,"timestamp":1499451300},
    {"type":"ask","price":2475.219,"amount":0.38974944,"tid":110941540,"timestamp":1499451285},
    {"type":"bid","price":2478.55,"amount":0.01653934,"tid":110941537,"timestamp":1499451283},
-------------------------------------------------------
'''

# ==================================================
# ==================================================
# ==================================================
class SeaofBTCapp(tk.Tk):
    '''
     __init__ implies that this will be run automatically if the class is called.
         other def methods will not run automatically.
            args = arguments = open ended, you can pass whatever you want through
            kwargs = key-word arguments, basically dictionaries.
     '''

    def __init__(self, *args, **kwargs):
        # Now initialize tkinter also.
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.title(self, "Nate's Title From SeaofBTCapp Class")
        tk.Tk.geometry(self, "1280x720")
        # Can't get the icon to show, now just a png icon
        # Resized to 12/16 pixels
        tk.Tk.iconbitmap(self, "icon.png")

        # /Users/Tracksta6/Dropbox/Computer Science/tkinter/Tkinter3


        container = ttk.Frame(self)
        # Making a quick window, use pack, for more detailed, use grid
        # side= What side do you want this on.
        # fill= Fill the entire space
        # expand= If there is any more white space in the window. Use it.
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # ----------------------------------------------------
        # Menubar block created in file 9
        # Create an overall menubar, and assign to this tkinter
        menuBar1 = tk.Menu(container)
        # Adding a tearoff divider into the menu that drops down
        fileMenu1 = tk.Menu(menuBar1, tearoff=0)
        # Now actually place a literal piece on the menubar
        menuBar1.add_cascade(label="File", menu=fileMenu1)
        # Create a subpiece under the File Tab
        fileMenu1.add_command(label="Save Settings",
                              command=lambda: popupmsg("Msg sent from class SeaofBTCapp"))
        # Create a separator under the File Tab
        fileMenu1.add_separator()
        # Create a 2nd subpiece under the File Tab
        fileMenu1.add_command(label="Exit", command=quit)

        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-

        # We are adding a new choice, and then 4 subchoices to the menubar options
        # Create the main new choice, will be on the main menu bar
        # Label the new menubar choice, "Exchange", and set its command to the new method.
        exchangeChoice1 = tk.Menu(menuBar1, tearoff=1)
        menuBar1.add_cascade(label="Echange", menu=exchangeChoice1)

        # -----Start Sub Choices-------------
        # These are tied to the global changeExchange method that we are creating up top.
        # We have our plot since File 8 tied to a U.S. bitcoin trader.
        # Eventually these 4 sub-choices will produce plots tied to foreign bitcoin traders.
        # We are sending two parts to the method, one is a label
        #       and the other is used by the program which can only use lowercase.
        exchangeChoice1.add_command(label="BTC-e",
                                    command=lambda: changeExchange("BTC-e", "btce"))

        exchangeChoice1.add_command(label="Bitfinex",
                                    command=lambda: changeExchange("Bitfinex", "bitfinex"))

        exchangeChoice1.add_command(label="Bitstamp",
                                    command=lambda: changeExchange("Bitstamp", "bitstamp"))

        exchangeChoice1.add_command(label="Huobi",
                                    command=lambda: changeExchange("Huobi", "huobi"))
        #-----End Sub Choices-------------


        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-
        # -NEW-NEW-NEW-

        tk.Tk.config(self, menu=menuBar1)
        # ----------------------------------------------------

        # Specify a dictionary here
        self.frames = {}
        # We will have numerous windows, and either click/button will bring another.
        # One application with numerous windows.


        # For loop that ranges in our page limits
        # Make sure to add any new page to our tuple for loop
        for F in (StartPage, TradingPage, BTCePage):
            # Use F so that we can progress through our pages.
            frame = F(container, self)
            self.frames[F] = frame
            # grid is more specific compared to pack.
            # sticky is using North/South/East/West -->
            #    will stretch to the size of the window.
            #       if you just use ew then it will stretch all to the sides.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


    # ==================================================
    def show_frame(self, controller1):
        # self.frames is looking at the frame dictionary that we created above.
        #       Controller is which frame we want to access
        frame = self.frames[controller1]
        # Then we will run a library function on the frame.
        frame.tkraise()


# ==================================================
class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # ----------------------------
        # ttk will give us a good looking button
        startPage_TradingPageButton = ttk.Button(self, text="Go To TradingPage",
                                                 command=lambda: controller.show_frame(TradingPage))
        startPage_TradingPageButton.pack()

        # ----------------------------
        # ttk will give us a good looking button
        startPage_CloseButton = ttk.Button(self, text="Close Program",
                                           command=quit)
        startPage_CloseButton.pack()


# ==================================================
class TradingPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Trading Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # ----------------------------
        label2 = ttk.Label(self, text="""Bitcoin Trading Application\n
        Use at your own risk.""", font=LARGE_FONT)
        label2.pack(padx=10, pady=10)

        # ----------------------------
        # ttk will give us a good looking button
        button1 = ttk.Button(self, text="Return to Home Page",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # ----------------------------
        bcte_label = ttk.Label(self, text="Click agree and you will be directed to the BTCe  Page", font=LARGE_FONT)
        bcte_label.pack(padx=10, pady=10)

        # ----------------------------
        # This is our only link to our bitcoin trading page
        tradingPage_agreeButton = ttk.Button(self, text="Agree",
                                             command=lambda: controller.show_frame(BTCePage))
        tradingPage_agreeButton.pack()

        # ----------------------------
        # This will auto-quit the program
        tradingPage_disagreeButton = ttk.Button(self, text="DisAgree",
                                                command=quit)
        tradingPage_disagreeButton.pack()
        # ----------------------------

        # *****NEW******#*****NEW******#*****NEW******#*****NEW******#*****NEW******
        # *****NEW******#*****NEW******#*****NEW******#*****NEW******#*****NEW******
        # *****NEW******#*****NEW******#*****NEW******#*****NEW******#*****NEW******


class BTCePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        # ----------------------------
        label = ttk.Label(self, text="BitCoin Trading Page"
                                     "\nThis is on live update based on site data.", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # ----------------------------
        # ttk will give us a good looking button
        pageTwo_homeButton = ttk.Button(self, text="Back to Home",
                                        command=lambda: controller.show_frame(StartPage))
        pageTwo_homeButton.pack()

        # ----------------------------
        # ----------------------------
        # ----------------------------
        # This set is needed for our plot.
        # Place this on the page you want the user to view the live plot
        # This is what is communicating with the main object call and the animate method
        canvas1 = FigureCanvasTkAgg(f, self)
        canvas1.show()
        canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # We have a graph with the above but we want a Nav Bar
        # Navigation bar
        toolbar1 = NavigationToolbar2TkAgg(canvas1, self)
        toolbar1.update()
        canvas1._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # Note we just added the standard tool bar to the graph but I
        #   i could not see it at first. I had to increase my y-height on page

        # ----------------------------

# ==================================================
# ==================================================


app = SeaofBTCapp()

# using our f-object from the top, animate-function, and 5000 milliseconds
# This means we will update our data every 5 seconds.
# This is what plotted to the graph page in file 6
ani1 = animation.FuncAnimation(f, animate, interval=5000)

app.mainloop()
