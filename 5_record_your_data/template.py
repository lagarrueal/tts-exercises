import os
import numpy as np
import json

from tools import read_audio, save_audio


def time_to_sample(time_stamp: float, sr):
    '''
    Convert a float value time stamp to the corresponding sample
    index, given the sample rate.
    '''

def trim_wave(wave: np.ndarray, start:int, stop:int):
    '''
    Trims a waveform such that the output only contains the
    samples from <start> to <stop>, inclusive. This function
    should just return the new trimmed waveform, not save it.
    '''

def trim_archive(archive_path:str):
    '''
    Trims all recordings in a dataset archive at the given path.
    '''
    # 1. Load the info.json file into memory
    # 2. Iterate all recordings in your archive
        # 3. Convert trim time stamps to samples
        # 4. Call trim_wave()
        # 5. save the trimmed waveform to the same path as the original