import soundfile
import numpy as np

def save_audio(wave: np.ndarray, sr: int, path: str):
    '''
    Save a waveform to file using soundfile
    Input arguments:
    * wave (np.ndarray): An array carrying the waveform
    * sr (int): The sample rate of the signal
    * path (str): Where the new file will be stored
    '''
    soundfile.write(path, wave, sr)
