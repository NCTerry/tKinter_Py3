
'''
This is a primary page. We have create a start page and a dictionary that holds pages.
This is a good initial format.
We can basically start here for any tKinter and create what we need from here...
We can add numerous pages to our dictionary of pages.

'''
import tkinter as tk

LARGE_FONT = ("Verdana", 12)

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

        # Specify a dictionary
        # We have numerous frames, and either click/button will bring another frame.
        # One application with numerous windows.
        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        # grid is more specific compared to pack.
        # sticky is using North/South/East/West --> will stretch to the size of the window.
        #       if you just use ew then it will stretch all to the sides.
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)


    def show_frame(self, controller1):
        # self.frames is looking at the frame dictionary that we created above.
        #       Controller is which frame we want to access
        frame = self.frames[controller1]
        # Then we will run a library function on the frame.
        frame.tkraise()

# ======Everything outside of this and below is a copy of the PythonIntro.py file.=======
# We just added a button/method to our start page
def qf(param):
    print(param)
# ======Everything outside of this and below is a copy of the PythonIntro.py file.=======


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

#======Everything outside of this and (qf() method) is a copy of the PythonIntro.py file.=======
# We just added a button/method to our start page
        button1 = tk.Button(self, text="Visit Page 1",
                            command=lambda: qf("See this worked"))
        button1.pack()
#======Everything outside of this and (qf() method) is a copy of the PythonIntro.py file.=======




app = SeaofBTCapp()
app.geometry("200x300")
app.mainloop()


