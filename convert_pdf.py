import os
import glob
import subprocess
import shutil
from tqdm import tqdm 

INPUT_dir = "./data/raw"
OUTPUT_dir = "./data/processed"
BATCH_SIZE = 1000
WORKERS = 4 # you will have to reduce the size of the worker if the the RAM is less than 12 GB VRAM


