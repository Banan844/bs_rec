from datetime import datetime as dt
from lib import double_num, list_strokes, isFolderCorrect, isFilenameCorrect, isHotkeyCorrect, isInteger
import screeninfo as scr
from tkinter import messagebox as msgbox
from strings import *
from processor import supporting_formats
from typing import get_args


class setting:
    filename_format = "REC_{yyyy}-{MM}-{dd}_{hh}-{mm}-{ss}" # Standard format
    rec_hotkey = "ctrl+r" # Standard hotkey, example alt+esc+r or shift+r or ctrl+c+v
    rec_folder = "my_records/" # Standard rec folder, example C:/Userfolder/Videos/records/ or records/minecraft/
    fps = 30 # Standard fps
    monitor = 0 # Standard monitors, example 0 or 1 or 2
    video_card = 0 # Device index, example 0 or 1
    colorspace = "BGR" # Screen recording colorspace, example BGR or RGB
    video_format = "mp4" # Video file format, supporting mp4 and avi


    # Save all settings
    def save(self):

        # Create file variable
        file = ""

        file = f"{file}{self.filename_format}\n" # Saving filename format setting
        file = f"{file}{self.rec_hotkey}\n" # Saving record hotkey setting
        file = f"{file}{self.rec_folder}\n" # Saving record folder setting
        file = f"{file}{self.fps}\n" # Saving fps setting
        file = f"{file}{self.monitor}\n" # Saving monitor setting
        file = f"{file}{self.video_card}\n" # Saving video card setting
        file = f"{file}{self.colorspace}\n" # Saving colorspace setting
        file = f"{file}{self.video_format}\n" # Saving video format setting

        # Return settings file
        return file
    

    # Save all settings to file
    def save_to_file(self, filename: str):

        file = self.save() # Saving all settings
        open(filename, "w", encoding="utf-8").write(file) # Saving to file
    

    # Load settings from string
    def load(self, file: str):

        # Get this settings
        filename_format = self.filename_format
        rec_hotkey = self.rec_hotkey
        rec_folder = self.rec_folder
        fps = self.fps
        monitor = self.monitor
        video_card = self.video_card
        colorspace = self.colorspace
        video_format = self.video_format

        strokes = list_strokes(file) # Convert all strokes to list
        stroke_num = 1 # Stroke number

        # Apply strokes
        for stroke in strokes:

            # If stroke skipped, skipping
            if not stroke.strip():
                stroke_num += 1
                continue

            match stroke_num:
                case 1:
                    # Filename format stroke
                    parameter = text.filename_format # Parameter name
                    filename_format_ = stroke.strip() # Get filename format

                    # If setting is not correct, showing error
                    if not self.isCorrect.filename_format(filename_format_):
                        msgbox.showerror(
                            text.failed_to_load_setting.format(setting=parameter), # Getting title and pasting setting
                            text.setting_is_not_correct.format(setting=parameter) # Getting error contains and pasting setting
                        )

                    # If setting is correct
                    else: filename_format = filename_format_

                case 2:
                    # Record hotkey stroke
                    parameter = text.rec_hotkey # Parameter name
                    rec_hotkey_ = stroke.strip() # Get record hotkey

                    # If setting is not correct, showing error
                    if not self.isCorrect.rec_hotkey(rec_hotkey_):
                        msgbox.showerror(
                            text.failed_to_load_setting.format(setting=parameter), # Getting title and pasting setting
                            text.setting_is_not_correct.format(setting=parameter) # Getting error contains and pasting setting
                        )

                    # If setting is correct
                    else: rec_hotkey = rec_hotkey_
                
                case 3:
                    # Record folder stroke
                    parameter = text.rec_folder # Parameter name
                    rec_folder_ = stroke.strip() # Get record folder

                    # If setting is not correct, showing error
                    if not self.isCorrect.rec_folder(rec_folder_):
                        msgbox.showerror(
                            text.failed_to_load_setting.format(setting=parameter), # Getting title and pasting setting
                            text.setting_is_not_correct.format(setting=parameter) # Getting error contains and pasting setting
                        )

                    # If setting is correct
                    else: rec_folder = rec_folder_

                case 4:
                    # FPS stroke
                    parameter = text.fps # Parameter name
                    fps_ = stroke.strip() # Get fps value

                    # If setting is not correct, showing error
                    if not self.isCorrect.fps(fps_):
                        msgbox.showerror(
                            text.failed_to_load_setting.format(setting=parameter), # Getting title and pasting setting
                            text.setting_is_not_correct.format(setting=parameter) # Getting error contains and pasting setting
                        )

                    # If setting is correct
                    else: fps = int(fps_)

                case 5:
                    # Monitor stroke
                    parameter = text.monitor # Parameter name
                    monitor_ = stroke.strip() # Get monitor

                    # If setting is not correct, showing error
                    if not self.isCorrect.monitor(monitor_):
                        msgbox.showerror(
                            text.failed_to_load_setting.format(setting=parameter), # Getting title and pasting setting
                            text.setting_is_not_correct.format(setting=parameter) # Getting error contains and pasting setting
                        )

                    # If setting is correct
                    else: monitor = int(monitor_)

                case 6:
                    # Video card stroke
                    parameter = text.video_card # Parameter name
                    video_card_ = stroke.strip() # Get video card

                    # If setting is not correct, showing error
                    if not self.isCorrect.video_card(video_card_):
                        msgbox.showerror(
                            text.failed_to_load_setting.format(setting=parameter), # Getting title and pasting setting
                            text.setting_is_not_correct.format(setting=parameter) # Getting error contains and pasting setting
                        )

                    # If setting is correct
                    else: video_card = int(video_card_)

                case 7: colorspace = stroke.strip() # Colorspace stroke
                case 8:
                    # Video format stroke
                    parameter = text.video_format # Parameter name
                    video_format_ = stroke.strip() # Get video format

                    # If setting is not correct, showing error
                    if not self.isCorrect.video_format(video_format_):
                        msgbox.showerror(
                            text.failed_to_load_setting.format(setting=parameter), # Getting title and pasting setting
                            text.setting_is_not_correct.format(setting=parameter) # Getting error contains and pasting setting
                        )

                    # If setting is correct
                    else: video_format = video_format_

                case _: break
            
            stroke_num += 1

        # Applying this settings
        self.filename_format = filename_format
        self.rec_hotkey = rec_hotkey
        self.rec_folder = rec_folder
        self.fps = fps
        self.monitor = monitor
        self.video_card = video_card
        self.colorspace = colorspace
        self.video_format = video_format
    

    # Load settings from file
    def load_from_file(self, filename: str):
        file = open(filename, "r").read()
        self.load(file)


    class isCorrect:
        # Check if record folder is correct
        def rec_folder(rec_folder: str) -> bool: return isFolderCorrect(rec_folder)

        # Check if fps value is correct
        def fps(fps: str | int) -> bool:
            # If value is not integer - incorrect
            if not isInteger(fps): return False
            
            # Else
            else:
                # Making value integer
                fps = int(fps)

                # If fps value smaller than 0 or 0 - incorrect
                if fps <= 0: return False

                # If is correct
                else: return True

        # Check if video card value is correct
        def video_card(video_card: str | int) -> bool: return isInteger(video_card)

        # Check if monitor is correct
        def monitor(monitor: str | int) -> bool:

            # If value is not integer - incorrect
            if not isInteger(monitor): return False

            # Else
            else:
                # Make value integer
                monitor = int(monitor)

                # If monitor value is incorrect
                if monitor > len(scr.get_monitors()) or monitor < 0: return False

                # If is correct
                else: return True

        # Check if filename format is correct
        def filename_format(filename_format: str) -> bool:
            filename = generate_filename(filename_format)
            return isFilenameCorrect(filename)

        # Check if record hotkey is correct
        def rec_hotkey(rec_hotkey: str) -> bool: return isHotkeyCorrect(rec_hotkey)

        # Check if video format is correct and supported
        def video_format(video_format: str) -> bool:

            # List supported formats
            for format in get_args(supporting_formats):
                # If video format is supported, correct
                if video_format == format: return True
            
            # If incorrect
            return False



# Generate record file name by formatting
def generate_filename(format: str):
    n = dt.now()
    dn=double_num

    # Get datetime
    d=n.day
    M=n.month
    y=n.year
    yyyy = y
    s=n.second
    m=n.minute
    h=n.hour

    # Convert datetime to 2 length
    dd=dn(d)
    MM=dn(M)
    yy=dn(y)
    ss=dn(s)
    mm=dn(m)
    hh=dn(h)

    result = format.format(d=d, M=M, y=y, yyyy=y, s=s, m=m, h=h, dd=dd, MM=MM, yy=yy, ss=ss, mm=mm, hh=hh)

    return result


