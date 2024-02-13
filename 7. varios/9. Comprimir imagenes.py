# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image

import os 

downloadsFolder = "/Users/HP/Downloads/"
picturesFolder = "/Users/HP/Downloads/imgs/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder+filename)
        
        if extension in [".jpg", ".jpeg",".png"]:
            picture = Image.open(downloadsFolder+filename)
            picture.save(downloadsFolder+"compressed_"+filename,optimize=True,quality=60)
            os.remove(downloadsFolder+filename)
            print(name+": "+extension)
        
        if extension in [".mp3"]:
            musicFolder = "/Users/HP/Downloads/Music/"
            os.rename(downloadsFolder+filename,musicFolder+filename)
            
        if extension in [".rar",".zip"]:
            compressedFolder = "/Users/HP/Downloads/Compressed/"
            os.rename(downloadsFolder+filename,compressedFolder+filename)
           
