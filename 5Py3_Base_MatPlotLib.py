
'''
This is a primary page. We have create a start page and a dictionary that holds pages.
This is a good initial format.
We can basically start here for any tKinter and create what we need from here...
We can add numerous pages to our dictionary of pages.


BasePage: We have our base pages and buttons created in 1-4
    We are adding in a new page (page3) with a matplotlib based plot.
    For this, we can easily use plot.show and the matplotlib library to plot, but these will
        bring up plots on top of our tkinter windows. We want to add a plot TO the windows.

1) We imported the matplotlib and several specifics seen below
2) Created a GraphPage (page3), changed linked details on page2 and closepage, added GraphPage to dictionary
3) Added a button on startpage to access  GraphPage  directly
4) Added a simple graph plot to the graph page
5) Added a standard toolbar to the graph plot
6) Had to increase the y-height to view the toolbar.

'''
import tkinter as tk
from tkinter import ttk
# ***NEW***
# ***NEW***
#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***
'''
Terminal/CMD     pip install matplotlib
'''
import matplotlib #***NEW***
from matplotlib import style #***NEW***
# This below lets us "change the back end"
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***


LARGE_FONT = ("Verdana", 12) # Base font that we want to use and will call
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
        tk.Tk.geometry(self, "500x800")
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


        # Specify a dictionary here
        self.frames = {}
        # We will have numerous windows, and either click/button will bring another.
        # One application with numerous windows.


        # For loop that ranges in our page limits
        # Make sure to add any new page to our tuple for loop
        for F in (StartPage, PageOne, PageTwo, GraphPage, ClosePage):
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

        # ttk will give us a good looking button
        button1 = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

        # ttk will give us a good looking button
        startPage_GraphPageButton = ttk.Button(self, text="Skip To GraphPage",
                            command=lambda: controller.show_frame(GraphPage))
        startPage_GraphPageButton.pack()

# ==================================================
class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # ttk will give us a good looking button
        pageOne_homeButton = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        pageOne_homeButton.pack()

        # ttk will give us a good looking button
        pageOne_pageTwoButton = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        pageOne_pageTwoButton.pack()

# ==================================================
# You can see that these are basic pages, and can begin with a copy/paste
# Details/attributes need to be changed but they follow the same format from the beginning.
#
class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # ttk will give us a good looking button
        pageTwo_pageOneButton = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        pageTwo_pageOneButton.pack()

        # ttk will give us a good looking button
        pageTwo_homeButton = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        pageTwo_homeButton.pack()

        # ttk will give us a good looking button
        pageTwo_GraphPageButton = ttk.Button(self, text="To Graph Page",
                            command=lambda: controller.show_frame(GraphPage))
        pageTwo_GraphPageButton.pack()

# ==================================================
class GraphPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # ttk will give us a good looking button
        GraphPage_pageTwoButton = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        GraphPage_pageTwoButton.pack()

        # ttk will give us a good looking button
        GraphPage_homeButton = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        GraphPage_homeButton.pack()

        # ttk will give us a good looking button
        GraphPage_closePageButton = ttk.Button(self, text="To Close Page",
                            command=lambda: controller.show_frame(ClosePage))
        GraphPage_closePageButton.pack()

        # ***NEW***
        # ***NEW***
        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***
        f = Figure(figsize=(5,5), dpi=100) # Not sure details
        a = f.add_subplot(111) #111 means 1x1 on chart 1
        a.plot([1,2,3,4,5,6,7,8], [5,6,1,3,8,9,3,5]) # Simple chart
        '''With the basic matplotlib we change just run plot.show and it would bring up a new
        chart on top of our tkinter window, but we want to add this TO our window. Continued....'''

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
        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***


# ==================================================
# You can see that these are basic pages, and can begin with a copy/paste
# Details/attributes need to be changed but they follow the same format from the beginning.
#
class ClosePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Close Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # ttk will give us a good looking button
        closePage_pageThreeButton = ttk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(GraphPage))
        closePage_pageThreeButton.pack()

        # ttk will give us a good looking button
        closePage_closeButton = ttk.Button(self, text="Close",
                            command=exit)
        closePage_closeButton.pack()

# ==================================================


app = SeaofBTCapp()
# This geomeotry works but is not from the class
#       app.geometry("200x300")
# This title works but is not from the class.
#       app.title("Nate's Title from main")
app.mainloop()



