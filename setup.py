#!/usr/bin/python
import os
import subprocess
import sys

subprocess.call(['virtualenv', 'myenv'])
if sys.platform == 'win32':
  bin = 'Scripts'
else:
  bin = 'bin'

subprocess.call([os.path.join('myenv', bin, 'pip'), 'install', '--upgrade', 'numpy'])
subprocess.call([os.path.join('myenv', bin, 'pip'), 'install', '--upgrade', 'scipy'])
subprocess.call([os.path.join('myenv', bin, 'pip'), 'install', '--upgrade', 'matplotlib'])
subprocess.call([os.path.join('myenv', bin, 'pip'), 'install', '--upgrade', 'pandas'])
subprocess.call([os.path.join('myenv', bin, 'pip'), 'install', '--upgrade', 'sklearn'])
