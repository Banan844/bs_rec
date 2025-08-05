import tkinter as tk
from settings import *
from settings_window.strings import *
import strings as mstr
from processor import supporting_formats
from tkinter import messagebox as msgbox




class SettingsWindow:
    video_format = ""
    closed = False
    settings_saved = False

    # Initialization
    def __init__(self, settings: setting):
        # Setting settings to class variable
        self.settings = settings

        self.root = tk.Tk() # Initializing gui
        self.root.geometry(f"{window_geometry[0]}x{window_geometry[1]}") # Window resolution
        self.root.resizable(False, False) # Making window unresizable
        self.root.title(text.window_title) # Title
        self.root.configure(bg=color.window_bg, borderwidth=10) # Configuring window


        #### Parameters


        # Record hotkey frame
        self.rec_hotkey_frame = tk.Frame(self.root, bg=color.window_bg)
        self.rec_hotkey_frame.place(x=window_geometry_bw[0], y=0, anchor="ne")

        # Record hotkey label to entry
        tk.Label(self.rec_hotkey_frame, text=text.rec_hotkey_label, fg=color.window_fg, bg=color.window_bg, font=font.label).grid(row=0, column=0)

        # Record hotkey entry
        self.rec_hotkey_entry = tk.Entry(self.rec_hotkey_frame, bg=color.entry_bg, fg=color.entry_fg, insertbackground=color.entry_fg, borderwidth=0, font=font.entry)
        self.rec_hotkey_entry.grid(row=0, column=1)


        # FPS frame
        self.fps_frame = tk.Frame(self.root, bg=color.window_bg)
        self.fps_frame.place(x=window_geometry_bw[0], y=30, anchor="ne")

        # FPS label to entry
        tk.Label(self.fps_frame, text=text.fps_label, fg=color.window_fg, bg=color.window_bg, font=font.label).grid(row=0, column=0)

        # FPS entry
        self.fps_entry = tk.Entry(self.fps_frame, bg=color.entry_bg, fg=color.entry_fg, insertbackground=color.entry_fg, borderwidth=0, font=font.entry)
        self.fps_entry.grid(row=0, column=1)


        # Record folder frame
        self.rec_folder_frame = tk.Frame(self.root, bg=color.window_bg)
        self.rec_folder_frame.place(x=window_geometry_bw[0], y=60, anchor="ne")

        # Record folder label to entry
        tk.Label(self.rec_folder_frame, text=text.rec_folder_label, fg=color.window_fg, bg=color.window_bg, font=font.label).grid(row=0, column=0)

        # Record folder entry
        self.rec_folder_entry = tk.Entry(self.rec_folder_frame, bg=color.entry_bg, fg=color.entry_fg, insertbackground=color.entry_fg, borderwidth=0, font=font.entry)
        self.rec_folder_entry.grid(row=0, column=1)


        # Video format frame
        self.video_format_frame = tk.Frame(self.root, bg=color.window_bg)
        self.video_format_frame.place(x=window_geometry_bw[0], y=90, anchor="ne")

        # Video format label to entry
        tk.Label(self.video_format_frame, text=text.video_format_label, fg=color.window_fg, bg=color.window_bg, font=font.label).grid(row=0, column=0)

        # Video format mp4 button
        self.video_format_mp4_btn = tk.Button(self.video_format_frame, bg=color.btn_bg, fg=color.btn_fg, borderwidth=0, font=font.btn, text=text.mp4,
                                              cursor=mstr.active_cursor, padx=text.btn_padx, command=lambda: self.change_video_format("mp4"),
                                              activebackground=color.btn_abg, activeforeground=color.btn_afg)
        self.video_format_mp4_btn.grid(row=0, column=1)
        # Video format avi button
        self.video_format_avi_btn = tk.Button(self.video_format_frame, bg=color.btn_bg, fg=color.btn_fg, borderwidth=0, font=font.btn, text=text.avi,
                                              cursor=mstr.active_cursor, padx=text.btn_padx, command=lambda: self.change_video_format("avi"),
                                              activebackground=color.btn_abg, activeforeground=color.btn_afg)
        self.video_format_avi_btn.grid(row=0, column=2)

        
        # Video card frame
        self.video_card_frame = tk.Frame(self.root, bg=color.window_bg)
        self.video_card_frame.place(x=window_geometry_bw[0], y=120, anchor="ne")

        # Video card label to entry
        tk.Label(self.video_card_frame, text=text.video_card_label, fg=color.window_fg, bg=color.window_bg, font=font.label).grid(row=0, column=0)

        # Video card entry
        self.video_card_entry = tk.Entry(self.video_card_frame, bg=color.entry_bg, fg=color.entry_fg, insertbackground=color.entry_fg, borderwidth=0, font=font.entry)
        self.video_card_entry.grid(row=0, column=1)


        # Filename format frame
        self.filename_format_frame = tk.Frame(self.root, bg=color.window_bg)
        self.filename_format_frame.place(x=window_geometry_bw[0], y=150, anchor="ne")

        # Filename format label to entry
        tk.Label(self.filename_format_frame, text=text.filename_format_label, fg=color.window_fg, bg=color.window_bg, font=font.label).grid(row=0, column=0)

        # Filename format entry
        self.filename_format_entry = tk.Entry(self.filename_format_frame, bg=color.entry_bg, fg=color.entry_fg, insertbackground=color.entry_fg, borderwidth=0, font=font.entry)
        self.filename_format_entry.grid(row=0, column=1)

        
        # Colorspace frame
        self.colorspace_frame = tk.Frame(self.root, bg=color.window_bg)
        self.colorspace_frame.place(x=window_geometry_bw[0], y=180, anchor="ne")

        # Colorspace label to entry
        tk.Label(self.colorspace_frame, text=text.colorspace_label, fg=color.window_fg, bg=color.window_bg, font=font.label).grid(row=0, column=0)

        # Colorspace entry
        self.colorspace_entry = tk.Entry(self.colorspace_frame, bg=color.entry_bg, fg=color.entry_fg, insertbackground=color.entry_fg, borderwidth=0, font=font.entry)
        self.colorspace_entry.grid(row=0, column=1)



        #### Save button


        self.save_settings_button = tk.Button(self.root, text=text.save_settings_button, borderwidth=0, cursor="hand2", font=font.save_settings_button,
                                              fg=color.save_settings_button_fg, bg=color.save_settings_button_bg, command=self.save_settings)
        self.save_settings_button.place(x=window_geometry_bw[0], y=window_geometry_bw[1], anchor="se")



        #### Load settings
        self.load_settings()



        #### When closing, making closed state
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    
    # Make window state closed
    def close(self):
        self.root.destroy()
        self.closed = True


    # Tkinter gui mainloop
    def mainloop(self):
        self.root.mainloop()


    # Load settings to parameters
    def load_settings(self):
        self.filename_format_entry.delete(0, tk.END)
        self.filename_format_entry.insert(0, self.settings.filename_format)

        self.rec_hotkey_entry.delete(0, tk.END)
        self.rec_hotkey_entry.insert(0, self.settings.rec_hotkey)

        self.rec_folder_entry.delete(0, tk.END)
        self.rec_folder_entry.insert(0, self.settings.rec_folder)

        self.fps_entry.delete(0, tk.END)
        self.fps_entry.insert(0, self.settings.fps)

        self.video_card_entry.delete(0, tk.END)
        self.video_card_entry.insert(0, self.settings.video_card)

        self.colorspace_entry.delete(0, tk.END)
        self.colorspace_entry.insert(0, self.settings.colorspace)

        self.change_video_format(self.settings.video_format)
        

    # Save settings
    def save_settings(self):

        # Create settings class
        settings = setting()

        # Get values from entries
        settings.filename_format = self.filename_format_entry.get()
        settings.rec_hotkey = self.rec_hotkey_entry.get()
        settings.rec_folder = self.rec_folder_entry.get()
        settings.fps = self.fps_entry.get()
        settings.video_card = self.video_card_entry.get()
        settings.colorspace = self.colorspace_entry.get()
        settings.video_format = self.video_format
        settings.monitor = self.settings.monitor

        # Check for incorrect settings
        incorrect_settings = self.incorrect_settings(settings)

        # If settings is incorrect, showing error
        if incorrect_settings:
            msgbox.showerror(text.save_settings_fail, text.settings_incorrect_message.format(incorrect_settings=incorrect_settings))
        
        # If settings is correct, saving
        else:
            # Converting to integer
            settings.fps = int(settings.fps)
            settings.video_card = int(settings.video_card)
            settings.monitor = int(settings.monitor)

            # Saving this settings
            self.settings = settings
            self.settings_saved = True
            self.close()


    # Change video format setting
    def change_video_format(self, video_format: supporting_formats):
        
        # Change video format to mp4
        if video_format == "mp4":
            self.video_format_mp4_btn.configure(bg=color.btn_sbg) # Make mp4 button background active
            self.video_format_avi_btn.configure(bg=color.btn_bg) # Make avi button background unactive
        
        # Change video format to avi
        elif video_format == "avi":
            self.video_format_avi_btn.configure(bg=color.btn_sbg) # Make avi button background active
            self.video_format_mp4_btn.configure(bg=color.btn_bg) # Make mp4 button background unactive
        
        # Unknown video format
        else: return
        
        # Change video format in variable
        self.video_format = video_format
    
    
    # Returns incorrect settings
    def incorrect_settings(self, settings: setting) -> list:
        incorrect_settings_list = []

        # If incorrect filename
        if not settings.isCorrect.filename_format(settings.filename_format): incorrect_settings_list.append(mstr.text.filename_format)
        # If incorrect fps value
        if not settings.isCorrect.fps(settings.fps): incorrect_settings_list.append(mstr.text.fps)
        # If incorrect record folder
        if not settings.isCorrect.rec_folder(settings.rec_folder): incorrect_settings_list.append(mstr.text.rec_folder)
        # If incorrect video card
        if not settings.isCorrect.video_card(settings.video_card): incorrect_settings_list.append(mstr.text.video_card)
        # If incorrect record hotkey
        if not settings.isCorrect.rec_hotkey(settings.rec_hotkey): incorrect_settings_list.append(mstr.text.rec_hotkey)
        # If incorrect video format
        if not settings.isCorrect.video_format(settings.video_format): incorrect_settings_list.append(mstr.text.video_format)

        # Return list of incorrect settings
        return incorrect_settings_list


