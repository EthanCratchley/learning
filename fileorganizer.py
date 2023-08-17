import os
import shutil

# Defining Audio Files
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

# Defining Video Files
video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

# Defining Image Files
img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif", ".heic")

# Defining Document Files
documents = (".pdf", ".doc", ".docx", ".dox", ".htm", ".html", ".txt", ".xls", ".xlsx")

def is_audio(file):
    # Check if the file extension is in the audio list
    return os.path.splitext(file)[1] in audio

def is_video(file):
    # Check if the file extension is in the video list
    return os.path.splitext(file)[1] in video

def is_image(file):
    # Check if the file extension is in the image list
    return os.path.splitext(file)[1] in img

def is_document(file):
    # Check if the file extension is in the documents list
    return os.path.splitext(file)[1] in documents

def is_screenshot(file):
    # Check if the file extension is in the image list and if "screenshot" is in the filename
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()

# Set the working directory to the Desktop
os.chdir("/Users/USER/Desktop/")

# Loop through files in the current directory
for file in os.listdir():
    if is_audio(file):
        # Move audio files to the "audio" directory
        shutil.move(file, "/Users/USER/Desktop/audio")
    elif is_video(file):
        # Move video files to the "video" directory
        shutil.move(file, "/Users/USER/Desktop/video")
    elif is_image(file):
        if is_screenshot(file):
            # Move screenshot images to the "screenshots" directory
            shutil.move(file, "/Users/USER/Desktop/screenshots")
        else:
            # Move other images to the "images" directory
            shutil.move(file, "/Users/USER/Desktop/images")
    else:
        # Move files with unknown extensions to the "Documents" directory
        shutil.move(file, "/Users/USER/Desktop/Documents")