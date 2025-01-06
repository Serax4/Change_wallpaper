import os
import random
import ctypes

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def get_next_wallpaper(directory):

    wallpapers = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    if not wallpapers:
        raise FileNotFoundError("No valid image files found in the directory.")
    return random.choice(wallpapers)


next_wallpaper = get_next_wallpaper(r"C:\Users\user\Images\wallpaper")
set_wallpaper(next_wallpaper)