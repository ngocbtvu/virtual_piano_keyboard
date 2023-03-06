#!/usr/bin/env python
# coding: utf-8

# In[4]:


#import libraries

import numpy as np
import pandas as pd
from scipy.io.wavfile import read
from IPython.display import Audio, Image
from PIL import Image, ImageDraw
import math
import random


# # <h1><center><span style="color:#E97777">Data Overview</span></center></h1>

# In[5]:


triads = pd.read_csv("C:\\Users\\phamt\\Downloads\\OneDrive\\Documents\\project\\piano_triad_prj\\triads.csv")
triads.head(3)


# # <h1><center><span style="color:#E97777">Build a Piano Keyboard</span></center></h1>

# In[7]:


def make_keyboard(chord):
    key_width = 15
    key_height = 100
    octaves = 7
    
    white_keys = ["C","D","E","F","G","A","B"]
    black_keys = ['Cs',"Eb","Fs","Gs","Bb"]
    
    notes2 = []
    notes2.append([str(chord['Note1'].values[0]).split("_")[0], str(chord['Note1'].values[0]).split("_")[1]])
    notes2.append([str(chord['Note2'].values[0]).split("_")[0], str(chord['Note2'].values[0]).split("_")[1]])
    notes2.append([str(chord['Note3'].values[0]).split("_")[0], str(chord['Note3'].values[0]).split("_")[1]])
    
    img_width = (key_width) * 7 * (octaves + 1)
    img_height = key_height + 5

    img = Image.new("RGB", (img_width, img_height), color=(230,230,230))
    img1 = ImageDraw.Draw(img)

    # Draw the white keys
    for i in range(2, octaves + 2):
        offset = (i * (key_width + 2) * 7) - ((key_width + 2) * 7 * 2)
        
        j = 1
        for note in white_keys:
            fill_color = "FFFFFF"
            if (note == notes2[0][0] and str(i) == notes2[0][1]) or (note == notes2[1][0] and str(i) == notes2[1][1]) or (note == notes2[2][0] and str(i) == notes2[2][1]):
                fill_color = "FF0000"
            x = j * (key_width + 2) + offset - key_width
            w = j * (key_width + 2) + key_width + offset - key_width
            img1.rectangle([(x, 0), (w, key_height)], fill = "#" + fill_color, outline ="#555555")
            j += 1

    # Draw the black keys
    for i in range(2, octaves + 2):
        offset = (i * (key_width + 2) * 7) - ((key_width + 2) * 7 * 2)
        j = 1
        for note in black_keys:
            fill_color = "444444"
            if (note == notes2[0][0] and str(i) == notes2[0][1]) or (note == notes2[1][0] and str(i) == notes2[1][1]) or (note == notes2[2][0] and str(i) == notes2[2][1]):
                fill_color = "FF0000"

            if (j == 3):
                j += 1   
            x = j * (key_width + 2) + offset - key_width + (key_width / 2) + 4
            w = j * (key_width + 2) + key_width + offset - key_width  + (key_width / 2)
            img1.rectangle([(x , 0), (w, key_height * .65)], fill = "#" + fill_color, outline = "#555555")
                
            j += 1

    display(img)


# # <h1><center><span style="color:#E97777">User Input</span></center></h1>

# In[8]:


# The chord we want to get (all chord names are uppercase, maj/min is in lowercase)
chord_input = input("Enter the chord name (e.g. C_maj): ")

# The Octave
octave = input("Enter the octave (1 to 7): ")

# Inversion (Root = 0, First Inversion = 1)
inversion = input("Enter the inversion (Root = 0, First Inversion = 1): ")

# Load the wav and make a player
filename = chord_input + "_" + octave + "_" + inversion
print(filename)


# # <h1><center><span style="color:#E97777">Display the Chord and Play Sound</span></center></h1>

# In[9]:


# Get the note names/positions from the data
chord = triads[triads['Chord'] == filename]
print(chord)

# Display the notes on the keyboard
make_keyboard(chord)


# In[11]:


# Read the wav with IPython and make a player
sample_rate, wav_data = read("C:\\Users\\phamt\\Downloads\\OneDrive\\Documents\\project\\piano_triad_prj\\piano_triads\\" + filename + ".wav")
Audio(wav_data, rate=sample_rate)

