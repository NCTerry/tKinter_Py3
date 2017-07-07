
'''
This is a primary page. We have create a start page and a dictionary that holds pages.
This is a good initial format.
We can basically start here for any tKinter and create what we need from here...
We can add numerous pages to our dictionary of pages.


BasePage: We have our base pages and buttons created in 1-5
    On 5, we added a graph page and created a plot on the page (page3).
    We added that graph page to our dictionary
    Here will will make this a live graph that we can adjust and pull from.

    1) We import the animation sub-library from matplotlib
    2) We imported the style function from matplotlib to adjust style on plot
    3) Cut 3 lines from the graph page that initializes the data for the plot, & paste up top
    4) We have a txt file with   x,y   data points. animate method pulls and puts in plot format
    5) Keep the graph page the same other than pulling those 3 lines
    6) Create an animation object in main.
    7) When user goes to GraphPage it will show plot with data from txt file.
    8) While you are on the GraphPage, if you pull up the txt file and change it
        EX:
1,6
2,7
3,2
4,6
and we hit enter to drop one line and add  5,8 and save
        then the plot if still running will automatically adjust and add that new point.
5,8
'''
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



#*****NEW******#*****NEW******#*****NEW******#*****NEW******#*****NEW******
#*****NEW******#*****NEW******#*****NEW******#*****NEW******#*****NEW******
#*****NEW******#*****NEW******#*****NEW******#*****NEW******#*****NEW******
import matplotlib.animation as animation
from matplotlib import style
style.use("dark_background")


# These 3 lines were created in part5, but now we cut them from the graph page and put them here
f = Figure(figsize=(5,5), dpi=100)  # Cut from GraphPage
a = f.add_subplot(111)   # Cut from GraphPage   # 111 means 1x1 on chart 1
#a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])  # Cut from GraphPage


def animate(i): #animate function with  'i' for interval
    pullData1 = open("6sampleData.txt", "r").read()
    dataList1 = pullData1.split("\n")
    xList1 = []
    ylist1 = []
    for eachLine1 in dataList1:
        if len(eachLine1) > 1:
            x, y = eachLine1.split(',')
            xList1.append(int(x))
            ylist1.append(int(y))

    a.clear() # This gets rid of subplot so it doesnt draw over-and-over and take up RAM
    a.plot(xList1, ylist1)
#*****NEW******#*****NEW******#*****NEW******#*****NEW******#*****NEW******
#*****NEW******
#*****NEW******



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

    #****NEW********
    # We created these 3 lines in part5, we are cutting these and putting them
    #       with our animate function up top that we just made.
        #f = Figure(figsize=(5,5), dpi=100) # Not sure details
        #a = f.add_subplot(111) #111 means 1x1 on chart 1
        #a.plot([1,2,3,4,5,6,7,8], [5,6,1,3,8,9,3,5]) # Simple chart
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

#******NEWNEW********
# using our f-object from the top, animate-function, and 1000 milliseconds
ani1 = animation.FuncAnimation(f, animate, interval=1000)
#******NEWNEW********


app.mainloop()



