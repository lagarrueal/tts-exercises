import soundfile
import numpy as np
import matplotlib.pyplot as plt

def read_audio(path: str = './data/f1.wav'):
    '''
    Uses soundfile to read a PCM file and returns
    a numpy array containing samples and the sample rate

    Input arguments:
    * path (str='./data/f1.wav'): A path to a .wav file
    '''
    return soundfile.read(path)

def save_audio(wave: np.ndarray, sr: int, path: str):
    '''
    Save a waveform to file using soundfile
    Input arguments:
    * wave (np.ndarray): An array carrying the waveform
    * sr (int): The sample rate of the signal
    * path (str): Where the new file will be stored
    '''
    soundfile.write(path, wave, sr)


def plot_f(wave, sr):
    plt.magnitude_spectrum(2*wave, sr)
    plt.show()
