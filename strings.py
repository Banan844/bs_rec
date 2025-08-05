window_geometry = (320, 240)
active_cursor = "hand2"


class font:
    font = "Segoe UI"

    monitor_icon = (font, 13)
    info_label = (font, 14)
    statuslabel = (font, 28)
    recbutton = (font, 15)
    settings_button = (font, 15)



class text:
    window_title = "BS Rec"
    window_title_recording = f"{window_title} ‒ Recording"

    monitor_icon = "🖥"

    statuslabel_disabled = "Idle"
    statuslabel_enabled = "Recording..."

    recbutton_recording = "Stop"
    recbutton_idle = "Start"

    rec_hotkey = "Record hotkey"
    fps = "FPS"
    monitor = "Monitor"
    rec_folder = "Records folder"
    video_format = "Video format"
    video_card = "Video card"
    filename_format = "Filename format"
    colorspace = "Colorspace"

    rec_hotkey_thread_error_title = "Record hotkey thread error"

    failed_to_load_setting = "Failed to load {setting} setting"
    setting_is_not_integer = "Setting {setting} is not integer!"
    setting_is_not_digital = "Setting {setting} is not digital!"
    setting_is_not_correct = "Setting {setting} is not correct!"


class color:
    window_bg = "#101010"

    statuslabel_disabled = "#aaa"
    statuslabel_enabled = "#fff"

    recbutton_bg = "#222"
    recbutton_fg = "#eee"
    recbutton_abg = "#282828"
    recbutton_afg = recbutton_fg

    settings_button_fg = recbutton_fg
    settings_button_bg = "#282828"

    filenamelabel = "#aaa"
    info_label_fg = "#eee"
    info_label_bg = "#222"

    monitor_icon_bg = window_bg
    monitor_icon_fg = "#f0f0f0"


