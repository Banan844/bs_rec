from typing import Literal, get_args
import dxcam
import cv2
import screeninfo as scr
from lib import fix_primary_monitor, makedirs_safe
from os.path import join as joinpath, realpath


supporting_formats = Literal["avi", "mp4"]



# Record class
class record:

    # Working state
    working = False
    
    # Formatted filename
    filename = ""

    # Start recording
    def start(self, filename: str, folder: str, monitor: int=0, device_idx: int=0, output_color: str="BGR", format: supporting_formats="avi", target_fps: int=30):

        # Adding extension to filename
        filename_formatted = f"{filename}.{format}"
        self.filename = filename_formatted

        monitors = scr.get_monitors() # Get monitors

        monitors = fix_primary_monitor(monitors) # Fix primary monitor
        
        output_idx = monitor

        geometry = (monitors[monitor].width, monitors[monitor].height) # Video file geometry

        camera = dxcam.create(output_idx=output_idx, device_idx=device_idx, output_color=output_color) # Creating the camera...
        camera.start(target_fps=target_fps, video_mode=True) # Starting camera...

        # Real folder path
        folder = realpath(folder)
        self.folder = folder

        # Create folder
        makedirs_safe(folder)
        
        # Filename with folder
        filename_formatted = realpath(joinpath(folder, filename_formatted))
        self.path = filename_formatted

        if format == "avi": # Record in AVI format
            fourcc = cv2.VideoWriter_fourcc(*'XVID') # Video writer format
            writer = cv2.VideoWriter(
                filename_formatted, fourcc, target_fps, geometry # Creating file writer
            )
        elif format == "mp4": # Record in MP4 format
            fourcc = cv2.VideoWriter_fourcc(*"mp4v") # Video writer format
            writer = cv2.VideoWriter(
                filename_formatted, fourcc, target_fps, geometry # Creating file writer
            )
        else: # Unsupported format
            supporting_formats_str = "" # Converting supported formats to string, for display it
            for i in get_args(supporting_formats):
                supporting_formats_str = supporting_formats_str + i + " "

            raise Exception(f"Incorrect or unsupported format: \"{format}\". Supported: {supporting_formats_str}.") # Display error with incorrect or unsupported format

        self.working = True # Working state

        while self.working: # Write frames when working
            writer.write(camera.get_latest_frame())
        
        # When stopping
        camera.stop() # Stopping camera
        writer.release() # Releasing file
    

    # Stop recording
    def stop(self):
        if self.working: self.working = False






if __name__ == "__main__":
    import threading
    
    this_record = record()
    monitor = int(input("Monitor: "))
    device_idx = int(input("Device index (video card), default 0: "))
    format = input("Format: ")
    fps = int(input("FPS: "))
    threading.Thread(target=lambda: this_record.start("test_processor", monitor, device_idx, format=format, target_fps=fps)).start()
    
    print("Record started, press ENTER to stop.")

    input()

    print("ENTER was pressed, stopping record...")
    this_record.stop()


