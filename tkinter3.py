'''
BUILT FOR PYTHON 3+ .

###We have the very basics for a GUI window in this block comment.
    It will pop up, in the top left corner with nothing.
        But it was created with just this.
This is included in our program, but just wanted to state the basics.
---------------------------------------------------------------
from tkinter import *   #import everthing from tkinter library
# Make the Window Class
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)    # Just referencing the initial
        self.master = master    # Stating the master widget
root = Tk()     # Stating our root window
app = Window(root)
root.mainloop()
---------------------------------------------------------------
'''
'''
This is a very simple initial program.
We create a Window class that creates the Window class.

Any object (Window) that we create as seen here in main, will have a primary
    method self.init_window()  (our name by the way).

    init_window() we will define below to hold a button and a menu bar
        The button will just exit.
        The menu bar will have:     | File | Edit |
            File will have:     | Exit |
            Edit will have:     | Undo | Show Image | Show Text |

    Undo will simply print("Undo") below.
    Show Image will display a photo in our tkinter window.
    Show Text will display a new text line in our tkinter window.
'''

from tkinter import *   #import everthing from tkinter library
from PIL import Image, ImageTk

# Make the Window Class
# We create a Window from main.
# Ex. Window will have a button, which uses a defined method.
class Window(Frame):

    # When you call a class, an _init_ will always run regardless.
    def __init__(self, master = None):
        Frame.__init__(self, master)    # Just referencing the initial
        self.master = master    # Stating the master widget
        self.init_window()      # We must create this method.
# ----------------------------------------------
# ----------------------------------------------
    # The method that will create the Window, called right above
    def init_window(self):
        self.master.title("GUI")    # State title
        self.pack(fill=BOTH, expand=1)
        # ------------Create button from Tkinter library.
        # Note client_exit command is not in the library. We will create this Below.
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0) # Place button at the upper left of the Window

# ----------------------------------------------
# ----------------------------------------------
        # ------------Create menu bar-------------------
        # We will only create a:
        #       File: Exit
        #       Edit:
        '''If you have:     command=self.showImg()
        then the image will automatically be called.
        The parenthesis will tell python to run regardless if you click.'''

        # ------Menu Object
        menu123 = Menu(self.master)
        self.master.config(menu=menu123)

        # ------Create File tab, with one cascade tab to exit.
        # Exit can be set up front, but we will use methods that we create below

        file123 = Menu(menu123)
        menu123.add_cascade(label="File", menu=file123)
        file123.add_command(label="Exit", command=self.client_exit)

        # ------Create Edit tab, with one cascade tab to print 'Undo' thru method
        # Will use methods that we create below
        edit123 = Menu(menu123)
        menu123.add_cascade(label="Edit", menu=edit123)
        edit123.add_command(label='Print Undo', command=self.print_undo)

        # ------Add 2 parts to the Edit cascade tab
        # Will use methods that we create below
        edit123.add_command(label='Show Image', command=self.showImg)
        edit123.add_command(label='Show Text', command=self.showTxt)

# ----------------------------------------------
# ----------------------------------------------
        # Display text if the edit tab option is selected
    def showTxt(self):
        text123 = Label(self, text="Fancy seeing you here!?!")
        text123.pack()

# ----------------------------------------------
# ----------------------------------------------
    # Display image: This method will be called from the edit menu tab
    # When selected it will display the image on the window.
    # Pillow is the external image command library
    #       Terminal/CMD:   pip install pillow
    # Now up top we need:
    #       from PIL import Image, ImageTk
    #
    def showImg(self):
        # Load the image. Image must be in the file directory
        load123 = Image.open("Photo123.jpg")    # Open the image
        render123 = ImageTk.PhotoImage(load123) # Render the image
        # Label is in the Tkinter library. We are saying that we want
        #       our label to be an imported photo.
        img123 = Label(self, image=render123)
        img123.image = render123
        img123.place(x=30, y=30)
        #
# ----------------------------------------------
# ----------------------------------------------
    # Method to catch event for button to quit the window.
    # We could state this in command=, but we want to have a method.
    # This command is used from the button, and the File menu
    def client_exit(self):
        exit()

    # This is a simple print command tied to one of the edit menu bar options.
    def print_undo(self):
        print("Undo")





# This is our main area ------------------------
# ----------------------------------------------
# ----------------------------------------------
root = Tk()     # Stating our root window
root.geometry("800x800") # State the Window Size
app = Window(root)
root.mainloop()
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------


