
'''

BasePage: 3
1) We added a button to the start page that moves to page one.
    2) Now we will add a new (page one) to this TK dictionary.

        If you create a new page, you need to add it to our tuple in the for loop.
            for loop in the:    class SeaofBTCapp

        Initially a page class below can be copied/pasted.
            You need to change specifics in the copy, and can add anything.
            If you copy and paste a page, and change attributes remember to add that page
                to the for loop.
'''
import tkinter as tk

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
        container = tk.Frame(self)
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
        for F in (StartPage, PageOne, PageTwo, ClosePage):
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
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)


        button1 = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

# ==================================================
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        pageOne_homeButton = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        pageOne_homeButton.pack()

        pageOne_pageTwoButton = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        pageOne_pageTwoButton.pack()

# ==================================================
# You can see that these are basic pages, and can begin with a copy/paste
# Details/attributes need to be changed but they follow the same format from the beginning.
#
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        pageTwo_pageOneButton = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        pageTwo_pageOneButton.pack()

        pageTwo_homeButton = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        pageTwo_homeButton.pack()

        pageTwo_closePageButton = tk.Button(self, text="To Close Page",
                            command=lambda: controller.show_frame(ClosePage))
        pageTwo_closePageButton.pack()

# ==================================================
# You can see that these are basic pages, and can begin with a copy/paste
# Details/attributes need to be changed but they follow the same format from the beginning.
#
class ClosePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Close Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        closePage_pageTwoButton = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        closePage_pageTwoButton.pack()

        closePage_closeButton = tk.Button(self, text="Close",
                            command=exit)
        closePage_closeButton.pack()

# ==================================================


app = SeaofBTCapp()
app.geometry("200x300")
app.mainloop()


