"""
AUTHOR: Hyoseo Kwag
SUBJECT: Jigsaw Puzzle It
DATE: August 23 2023 - 
DESCRIPTION: This program allows user to upload their image, or image provided already to play
            game of jigsaw puzzle. User can also select level (which enhances difficulty by
            slicing in smaller pieces) to their like.
"""
from genericpath import isfile
import tkinter as tk
# from playsound import playsound
import pygame

window = tk.Tk()                            # make window from tkinter
scr_width = window.winfo_screenwidth()      # user's current screen width in pixels
scr_height = window.winfo_screenheight()    # user's current screen height in pixels
RELX_MIDDLE = 0.5                           # float value to place elements in middle of coordinates
curr_level = int(1)                         # integer value of level; user can change level
is_fullscreen = False                       # boolean whether current window is full screened


"""
make a gui window using tkinter geometry; window size depends on user's screen size
"""
def initialize():
    window.geometry(f'{int(scr_width/1.6)}x{int(scr_height/1.3)}')
    window.resizable(width=False, height=False)
    window.title("Jigsaw Puzzle It")
# TODO: play music using pygame module
    pygame.init()               # initialize pygame module for sound
    bkgd_music = pygame.mixer.Sound(r"jigsaw puzzle\resources\music\just-relax-11157.mp3")
    bkgd_music.play()

"""
main lobby of the game that displays options that user can use by clicking
"""
def main_lobby_window():
    tk.Label(window, text="Jigsaw Puzzle It", fg='white', bg='blue').place(relx=RELX_MIDDLE, rely=0.1, anchor=tk.CENTER)
    tk.Button(window, text="PLAY").place(relx=RELX_MIDDLE, rely=0.25, anchor=tk.CENTER)
    tk.Label(window, text="CURRENT LEVEL: "+str(curr_level)).place(relx=RELX_MIDDLE, rely=0.35, anchor=tk.CENTER)
    tk.Button(window, text="SELECT LEVEL", command=select_level_window).place(relx=RELX_MIDDLE, rely=0.4, anchor=tk.CENTER)
    tk.Button(window, text="SETTING", command=setting_window).place(relx=RELX_MIDDLE, rely=0.5, anchor=tk.CENTER)
    tk.Button(window, text="QUIT", command=window.destroy).place(relx=RELX_MIDDLE, rely=0.6, anchor=tk.CENTER)

"""
when "SELECT LEVEL" button is clicked, this level selection window opens
"""
def select_level_window():
    LEV_SIZE = int(400)
    level_win = tk.Toplevel(window)
    level_win.geometry(str(LEV_SIZE)+"x"+str(LEV_SIZE))
    level_win.resizable(width=False, height=False)
    level_win.title("Level Select")
    level_win.grab_set()

    # open the level selection window in the middle of the screen
    x_coordinate = int((scr_width/2) - (LEV_SIZE/2))
    y_coordinate = int((scr_height/2) - (LEV_SIZE/2))
    level_win.geometry("{}x{}+{}+{}".format(LEV_SIZE, LEV_SIZE, x_coordinate, y_coordinate))

    # setting window design
    tk.Label(level_win, text='SELECT LEVEL', fg='white', bg='green').place(relx=RELX_MIDDLE, rely=0.1, anchor=tk.CENTER)

""""
when "SETTING" button is clicked, this setting window opens. while it's open,
user cannot interact with main lobby window
"""
def setting_window():
    # create setting window
    SETT_SIZE = int(300)
    setting_win = tk.Toplevel(window)
    setting_win.geometry(str(SETT_SIZE)+"x"+str(SETT_SIZE))
    setting_win.resizable(width=False, height=False)
    setting_win.title("Setting")
    setting_win.grab_set()

    # open the setting window in the middle of the screen
    x_coordinate = int((scr_width/2) - (SETT_SIZE/2))
    y_coordinate = int((scr_height/2) - (SETT_SIZE/2))
    setting_win.geometry("{}x{}+{}+{}".format(SETT_SIZE, SETT_SIZE, x_coordinate, y_coordinate))

    # setting window design
    tk.Label(setting_win, text='SETTING', fg='white', bg='orange').place(relx=RELX_MIDDLE, rely=0.1, anchor=tk.CENTER)
    tk.Button(setting_win, text="CHANGE SCREEN SIZE", command=change_win_size).place(relx=RELX_MIDDLE, rely=0.25, anchor=tk.CENTER)
    tk.Label(setting_win, text='Click Again to Revert').place(relx=RELX_MIDDLE, rely=0.325, anchor=tk.CENTER)

"""
when user clicks this button, it changes screen size from windowed to full screen, and vice versa
"""
def change_win_size():
    global is_fullscreen
    if is_fullscreen==False:
        window.attributes('-fullscreen', True)
        is_fullscreen = True
    else:
        window.attributes('-fullscreen', False)
        is_fullscreen = False


def main():
    initialize()                # initialize window using TKinter module
    main_lobby_window()         # put TKinter elements inside for interactivity

    window.mainloop()           # continue execution until quit or close

main()