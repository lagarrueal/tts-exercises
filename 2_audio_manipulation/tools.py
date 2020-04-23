import soundfile
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

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


def plot_spectrum(wave, sr):
    plt.magnitude_spectrum(wave, sr, sides='twosided')
    plt.show()


def plot_spectrogram(wave, sr):
    S = librosa.feature.melspectrogram(y=wave, sr=sr, fmax=8000)
    plt.figure(figsize=(10, 4))
    S_dB = librosa.power_to_db(S, ref=np.max)
    librosa.display.specshow(S_dB, x_axis='time',
        y_axis='mel', sr=sr, fmax=8000)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-frequency spectrogram')
    plt.tight_layout()
    plt.show()