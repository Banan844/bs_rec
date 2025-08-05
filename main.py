import tkinter as tk
import threading
from strings import *
from settings import *
from processor import *
import keyboard
from time import sleep
from functools import partial
import settings_window
from tkinter import messagebox as msgbox
from os.path import isfile, exists
from os import rmdir




recording = False
this_record = record()
this_setting = setting()
this_record_th = ...
this_settings_window = ...

settings_file_name = "bs_rec_settings"
settings_file_ext = "txt"
settings_filename = f"{settings_file_name}.{settings_file_ext}"




class MainWindow:
    # Initialization
    def __init__(self):

        self.root = tk.Tk() # Initializing gui
        self.root.geometry(f"{window_geometry[0]}x{window_geometry[1]}") # Window resolution
        self.root.resizable(False, False) # Making window unresizable
        self.root.title(text.window_title) # Title
        self.root.configure(background=color.window_bg) # Configuring window

        # Registering status label
        self.statuslabel = tk.Label(self.root, text=text.statuslabel_disabled, bg=color.window_bg, fg=color.statuslabel_disabled, font=font.statuslabel)
        # Placing status label
        self.statuslabel.place(anchor="nw", x=10, y=10)

        # Registering filename label. It's showing when recording is started
        self.filenamelabel = tk.Label(self.root, fg=color.filenamelabel, bg=color.window_bg, text="")
        self.filenamelabel.place(anchor="nw", x=10, y=60) # Placing this

        # Registering record hotkey label.
        self.record_hotkey_label = tk.Label(self.root, fg=color.info_label_fg, bg=color.info_label_bg, font=font.info_label, text=this_setting.rec_hotkey)
        self.record_hotkey_label.place(anchor="nw", x=10, y=100, width=130)

        # Registering video format label.
        self.video_format_label = tk.Label(self.root, fg=color.info_label_fg, bg=color.info_label_bg, font=font.info_label, text=this_setting.video_format)
        self.video_format_label.place(anchor="nw", x=142, y=100, width=60)

        # Registering fps label.
        self.fps_label = tk.Label(self.root, fg=color.info_label_fg, bg=color.info_label_bg, font=font.info_label, text=this_setting.fps)
        self.fps_label.place(anchor="nw", x=204, y=100, width=60)

        # Monitor icon
        tk.Label(self.root, text=text.monitor_icon, font=font.monitor_icon, bg=color.monitor_icon_bg, fg=color.monitor_icon_fg).place(y=140, x=10)





        # Monitor buttons
        monitors = scr.get_monitors() # Get monitors

        monitor_btn_x = 50
        monitor_btn_y = 140
        monitor_btn_width = 30

        idx = 0

        # List all monitors
        for i in monitors:
            monitor = idx + 1 # Getting real monitor num for view on button

            # Monitor button
            tk.Button(self.root, text=monitor, bg=color.info_label_bg, fg=color.info_label_fg, font=(font.font, 12), cursor=active_cursor,
                      command=partial(self.ChangeState.change_monitor, this_setting, idx)).place(x=monitor_btn_x, y=monitor_btn_y, width=monitor_btn_width)
            

            monitor_btn_x = monitor_btn_x + monitor_btn_width + 2 # Calculate monitor button x position
            idx += 1





        # Registering rec button
        self.recbutton = tk.Button(self.root, text=text.recbutton_idle, fg=color.recbutton_fg, bg=color.recbutton_bg, cursor=active_cursor, font=font.recbutton, borderwidth=0,
                                   activebackground=color.recbutton_abg, activeforeground=color.recbutton_afg, command=lambda: ToggleRec(self))
        # Placing rec button
        self.recbutton.place(anchor="s", x=window_geometry[0]/2, y=window_geometry[1], width=window_geometry[0])


        # Registering settings button
        self.settings_button = tk.Button(self.root, text="🌣", fg=color.settings_button_fg, bg=color.settings_button_bg, cursor=active_cursor, font=font.settings_button, borderwidth=0,
                                         command=settings_button_click)
        # Placing settings button
        self.settings_button.place(x=0, y=window_geometry[1], anchor="sw", width=50)
    

    # Registering main loop function
    def mainloop(self):
        self.root.mainloop()
    

    # Registering change element state class
    class ChangeState:

        # Change status label state
        def statuslabel(self, enable: bool):
            if enable: self.statuslabel.configure(text=text.statuslabel_enabled, fg=color.statuslabel_enabled) # Enabling
            else: self.statuslabel.configure(text=text.statuslabel_disabled, fg=color.statuslabel_disabled) # Disabling
        
        def recbutton(self, recording: bool):
            if recording: self.recbutton.configure(text=text.recbutton_recording)
            else: self.recbutton.configure(text=text.recbutton_idle)
        
        def change_monitor(setting: setting, monitor: int): this_setting.monitor = monitor




# Open settings window
def settings_button_click():
    global this_settings_window
    global this_setting

    # If window is not opened
    if this_settings_window == ...: open_settings_window()
    
    else:
        # Open new window, if window is closed
        if this_settings_window.closed: open_settings_window()


# Open settings window function
def open_settings_window():
    global this_settings_window
    global this_setting

    # Open settings window
    this_settings_window = settings_window.SettingsWindow(this_setting)
    this_settings_window.mainloop()


# Listen to settings changing
def SettingsListener(main_window: MainWindow):
    global this_settings_window
    global this_setting


    while True:
        
        # If settings window initialized
        if this_settings_window != ...:

            # If settings changed
            if this_settings_window.settings_saved:

                # Applying this settings
                this_setting = this_settings_window.settings
                UpdateSettingsElem(main_window, this_setting)

                # Saving this settings
                this_setting.save_to_file(settings_filename)

                # Disable saved settings state
                this_settings_window.settings_saved = False

        sleep(0.1)


# Toggle record
def ToggleRec(self: MainWindow):
    global recording
    global this_record_th
    global this_setting

    if not recording: # Start record

        # Generate filename
        filename = generate_filename(this_setting.filename_format)
        
        # Starting record thread
        this_record_th = threading.Thread(target=lambda: this_record.start(filename, this_setting.rec_folder, this_setting.monitor, this_setting.video_card, this_setting.colorspace,
                                                                           this_setting.video_format, this_setting.fps))
        this_record_th.start()

        # Changing elements
        self.ChangeState.statuslabel(self, True) # Changing status label state
        self.ChangeState.recbutton(self, True) # Changing rec button state

        while this_record.filename == "": ... # Waiting for formatted filename

        self.filenamelabel.configure(text=this_record.filename) # Changing filename label text to this filename
        self.root.title(text.window_title_recording) # Changing window title to recording

    else: # End record

        # Stopping record
        this_record.stop()
        this_record_th.join()

        # Changing elements
        self.ChangeState.statuslabel(self, False) # Changing status label state
        self.ChangeState.recbutton(self, False) # Changing rec button state
        self.filenamelabel.configure(text="") # Removing filename label text
        self.root.title(text.window_title) # Changing window title to idle

    
    recording = not recording # Invert recording value


# Listen hotkey to toggle record in paralel thread
def ToggleRecHotkeyListener(self: MainWindow):
    global this_setting

    while True:
        try:
            hotkey_pressed = keyboard.is_pressed(this_setting.rec_hotkey)

            # Check if hotkey is pressed
            if hotkey_pressed:
                ToggleRec(self) # If pressed, toggling record
                sleep(0.3) # Sleep for detect key one time
        
            else: sleep(0.1)
        
        except Exception as error:
            msgbox.showerror(text.rec_hotkey_thread_error_title, error)
            sleep(1)


# Update elements with settings on main window after settings update
def UpdateSettingsElem(self: MainWindow, settings: setting):
    self.record_hotkey_label.configure(text=settings.rec_hotkey) # Change text of record hotkey label
    self.video_format_label.configure(text=settings.video_format) # Change text of video format label
    self.fps_label.configure(text=settings.fps) # Change text of fps label






# Start app
if __name__ == "__main__":
    # If settings file is exists, reading
    if isfile(settings_filename): this_setting.load_from_file(settings_filename)
    
    # If settings file is not exists
    else:
        # If is a folder, removing
        if exists(settings_filename): rmdir(settings_filename)
        this_setting.save_to_file(settings_filename)
        

    gui = MainWindow()

    # Start hotkey listener thread
    threading.Thread(target=lambda: ToggleRecHotkeyListener(gui), daemon=True).start()
    # Start settings listener thread
    threading.Thread(target=lambda: SettingsListener(gui), daemon=True).start()

    gui.mainloop()
    this_record.stop()

    this_setting.monitor = 0
    this_setting.save_to_file(settings_filename)

