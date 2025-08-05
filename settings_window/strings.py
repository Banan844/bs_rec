window_geometry = (370, 280)
window_borderwidth = 10
window_geometry_bw = (window_geometry[0] - (window_borderwidth * 2), window_geometry[1] - (window_borderwidth * 2))



class font:
    font = "Segoe UI"
    label = (font, 14)
    entry = (font, 14)
    btn = (font, 12)
    save_settings_button = (font, 13)



class text:
    window_title = "BS Rec ‒ Settings"

    save_settings_fail = "Failed to save settings"
    settings_incorrect_message = "This settings are entered incorrect: {incorrect_settings}. Try to change this settings."
    some_settings_incorrect_message = "Some settings are incorrect =("

    rec_hotkey_label = "Record hotkey: "
    fps_label = "FPS: "
    rec_folder_label = "Records folder: "
    video_format_label = "Video format: "
    video_card_label = "Video card num: "
    filename_format_label = "Filename format: "
    colorspace_label = "Colorspace: "

    mp4 = "mp4"
    avi = "avi"

    btn_padx = 33

    save_settings_button = "Save this settings"



class color:
    window_bg = "#101010"
    window_fg = "#f0f0f0"

    entry_bg = "#222"
    entry_fg = window_fg

    btn_bg = entry_bg
    btn_fg = entry_fg
    btn_sbg = "#009655"

    btn_abg = "#444"
    btn_afg = btn_fg

    save_settings_button_fg = "#2a333a"
    save_settings_button_bg = "#fff"