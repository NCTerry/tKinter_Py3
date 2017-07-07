
'''
This is a primary page. We have create a start page and a dictionary that holds pages.
This is a good initial format.
We can basically start here for any tKinter and create what we need from here...
We can add numerous pages to our dictionary of pages.


BasePage:
1) We changed all the tk.Frame    /tk.label   /tk.Button to  ttk for aesthetics.
                      ttk.Frame  /ttk.label  /ttk.Button
    These are through the whole program.
    It really just changed the button in the very basic way, but it is more pleasing.
2) We added a title (class SeaofBTCapp) to the entire program
3) We changed the geometry specs (class SeaofBTCapp) to the primary class
4) We tried to add an icon (class SeaofBTCapp) and it did not finalize.
    We ended up with a seeming unrecognized icon, it does not seem to comprehend the
        image we are trying to bring in. I tried a png and an ico, both are 12x16 pixels
        Both get the unrecognized icon image. They get it, so clearly the program is working
            just not enough to actually read what the image is or be able to accept it.
'''
import tkinter as tk
from tkinter import ttk #***NEW***
# ttk = allows to make changes and copy/replace function
# Specifically, ttk will make the buttons more aesthetic etc.
# Anywhere that we have a    tk.object    change to    ttk.object
# EX. tk.Frame ==> ttk.Frame
# ignore: tk.Tk.__init__(self, *args, **kwargs)

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


        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***
        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***
        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***
        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***
        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***
        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***

        tk.Tk.title(self, "Nate's Title From SeaofBTCapp Class") #***NEW***
        tk.Tk.geometry(self, "500x500") #***NEW***
        # Can't get the icon to show, now just has a pdf icon
        # Resized to 12/16 pixels
        tk.Tk.iconbitmap(self, "4icon.png")

        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***
        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***
        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***
        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***
        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***
        # ***NEW***#***NEW***#***NEW***#***NEW***#***NEW***#***NEW***

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
class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        # ttk will give us a good looking button
        button1 = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

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
        pageTwo_closePageButton = ttk.Button(self, text="To Close Page",
                            command=lambda: controller.show_frame(ClosePage))
        pageTwo_closePageButton.pack()

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
        closePage_pageTwoButton = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        closePage_pageTwoButton.pack()

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



