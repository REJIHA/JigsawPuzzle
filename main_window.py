"""
AUTHOR: Hyoseo Kwag
SUBJECT: Jigsaw Puzzle It
DATE: August 23 2023 - 
DESCRIPTION: This program allows user to upload their image, or image provided already to play
            game of jigsaw puzzle. User can also select level (which enhances difficulty by
            slicing in smaller pieces) to their like.
"""
from genericpath import isfile
from tkinter import *

window = Tk()                               # make window from tkinter
scr_width = window.winfo_screenwidth()      # user's current screen width in pixels
scr_height = window.winfo_screenheight()    # user's current screen height in pixels
ai_level = int(1)                           # integer value of level; user can change level
is_fullscreen = False                       # boolean whether current window is full screened


# make a gui window using tkinter geometry; window size depends on user's screen size
def initialize():
    # window.geometry("650x650")
    window.geometry(f'{int(scr_width/1.6)}x{int(scr_height/1.3)}')
    window.resizable(width=False, height=False)
    window.title("Jigsaw Puzzle It")

# main lobby of the game that displays buttons that user can click
def main_lobby():
    # window.update_idletasks()
    # win_width = window.winfo_width()
    # win_height = window.winfo_height()
    Label(window, text="Jigsaw Puzzle It", fg='white', bg='blue').place(relx=0.5, rely=0.1, anchor=CENTER)
    Button(window, text="PLAY").place(relx=0.5, rely=0.25, anchor=CENTER)
    Label(window, text="CURRENT LEVEL: "+str(ai_level)).place(relx=0.5, rely=0.35, anchor=CENTER)
    Button(window, text="SELECT LEVEL", command=select_level_window).place(relx=0.5, rely=0.4, anchor=CENTER)
    Button(window, text="SETTING", command=setting_window).place(relx=0.5, rely=0.5, anchor=CENTER)
    Button(window, text="QUIT", command=window.destroy).place(relx=0.5, rely=0.6, anchor=CENTER)

# when "SELECT LEVEL" button is clicked, this level selection window opens
def select_level_window():
    lev_size = int(400)
    level_win = Toplevel(window)
    level_win.geometry(str(lev_size)+"x"+str(lev_size))
    level_win.resizable(width=False, height=False)
    level_win.title("Level Select")
    level_win.grab_set()

    # open the level selection window in the middle of the screen
    x_coordinate = int((scr_width/2) - (lev_size/2))
    y_coordinate = int((scr_height/2) - (lev_size/2))
    level_win.geometry("{}x{}+{}+{}".format(lev_size, lev_size, x_coordinate, y_coordinate))

    # setting window design
    Label(level_win, text='SELECT LEVEL', fg='white', bg='green').place(relx=0.5, rely=0.1, anchor=CENTER)

# when "SETTING" button is clicked, this setting window opens. while it's open,
# user cannot interact with main lobby window
def setting_window():
    # create setting window
    sett_size = int(300)
    setting_win = Toplevel(window)
    setting_win.geometry(str(sett_size)+"x"+str(sett_size))
    setting_win.resizable(width=False, height=False)
    setting_win.title("Setting")
    setting_win.grab_set()

    # open the setting window in the middle of the screen
    x_coordinate = int((scr_width/2) - (sett_size/2))
    y_coordinate = int((scr_height/2) - (sett_size/2))
    setting_win.geometry("{}x{}+{}+{}".format(sett_size, sett_size, x_coordinate, y_coordinate))

    # setting window design
    Label(setting_win, text='SETTING', fg='white', bg='orange').place(relx=0.5, rely=0.1, anchor=CENTER)
    resize_butt = Button(setting_win, text="FULLSCREEN", command=change_win_size).place(relx=0.5, rely=0.25, anchor=CENTER)

# TODO:change button text upon click
def change_win_size():
    global is_fullscreen    
    if is_fullscreen==False:
        window.attributes('-fullscreen', True)
        is_fullscreen = True
        # resize_butt['text'] = 'WINDOWED'
    else:
        window.attributes('-fullscreen', False)
        is_fullscreen = False
        # resize_butt['text'] = 'FULLSCREEN'

def main():
    # window = tk.Tk()
    initialize()
    main_lobby()


    window.mainloop()

main()