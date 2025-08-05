from os.path import exists, realpath
from os import makedirs, remove, rmdir
import keyboard



# Set primary monitor to first
def fix_primary_monitor(monitors):
    idx = 0

    for i in monitors:
        if i.is_primary and idx != 0:
            monitors_ = monitors.copy()
            monitors_[0] = monitors[idx]
            monitors_[idx] = monitors[0]
            monitors = monitors_

            break

        idx += 1
    
    return monitors


# Convert num 1 length to 2 length
def double_num(value: str | int) -> str:
    value = str(value)

    if len(value) < 2:

        while len(value) < 2:
            value = "0" + value
    
    elif len(value) > 2:

        value = value[len(value)-2:]
    
    return value


# Check if folder is correct
def isFolderCorrect(folder: str) -> bool:

    # Make folder if is not exists
    if not exists(folder):
        try: makedirs(folder)
        # If failed to make folder
        except: return False
    
    # If already exists
    else: return True


    # Folder is created status
    is_exists = exists(folder)

    # If folder is created, removing
    if is_exists: rmdir(folder)


    # Return result
    return is_exists


# Check if file is correct
def isFilenameCorrect(filename: str) -> bool:

    filename = realpath(filename)

    # Make file if is not exists
    if not exists(filename):
        try: open(filename, "w").write("")
        # If failed to make file
        except: return False
    
    # If already exists
    else: return True
    

    # Filename exists status
    is_exists = exists(filename)

    # If exists, removing
    if is_exists: remove(filename)


    # Return result
    return is_exists


# Check if integer is correct
def isInteger(value: str) -> bool:
    try:
        int(value)
        return True
    except:
        return False


# Check hotkey for correct
def isHotkeyCorrect(hotkey: str) -> bool:
    try:
        keyboard.is_pressed(hotkey)
        return True
    except:
        return False


# Make dirs safe
def makedirs_safe(path: str) -> None | str:
    try:
        makedirs(path)
        return None
    
    except Exception as error:
        return error


# List all strokes in string
def list_strokes(string: str) -> list:

    result = []
    idx = 0

    for sym in string:
        if sym == "\n":
            result.append(string[:idx])
            string = string[idx+1:]
            
            idx = 0

            continue
        
        idx += 1
    
    result.append(string)

    return result
