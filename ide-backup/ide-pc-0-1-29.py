# -*- coding: utf-8 -*-
"""Pynecone-colab-IDE of pc 0_1_29.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y7mCWlfc9cY8q6pHqVxXwdYudBOdDKa9
"""

#@title 你就仗著 pynecone 這點好學 這點全端 
# reviewed by PyCon TW 2023
# This colab file is contributed by https://github.com/milochen0418
# Let's student can open browser to developing pynecone webapp 
# in every computer without any installation. 
# Welcome to fork and star this GPLv3 open source project https://github.com/milochen0418/pynecone-colab-ide

#@title Import pynecone-colab-ide
!source <(curl -s https://raw.githubusercontent.com/milochen0418/pynecone-colab-ide/tag-pc-0-1-29/utils/init.sh)
from IPython.display import clear_output
clear_output()
import os
os.chdir('/content/app')
!echo "Because IDE Reset, please install pynecone environment. If you installed it before, please do it again"

# Commented out IPython magic to ensure Python compatibility.
#@title Install  (need 1.5 ~ 2 minutes)
from IPython.display import clear_output
# %load_ext autoreload
# %autoreload 2
!source /content/app/install.sh
clear_output()
!echo "Pynecone environment setup ready, Please get the link to watch your running result"

#@title Get Link & QRCode
from IPython.display import clear_output, Image, display
!source /content/app/tunnel.sh 
clear_output()
!python /content/app/qrshare.py
display(Image(filename="qr-code.png"))

# Commented out IPython magic to ensure Python compatibility.
#@title Terminal
# %reload_ext colabxterm
# %xterm

#@title Keep Run
!keeprun