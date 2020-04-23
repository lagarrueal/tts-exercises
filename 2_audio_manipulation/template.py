import numpy as np
import librosa


from tools import save_audio, read_audio, plot_spectrum, plot_spectrogram

'''
Put your sine function from assignment 1 here.
'''

def multi_sine(C, F, sr, duration):
    '''
    Returns a weighted sum of frequency components.
    C should be a list of relative ampltiudes and F
    is a list of frequencies.
    '''


def half_sr(wave):
    '''
    Given a waveform, half the number of samples by
    removing every second sample.
    '''


def zip_waves(a, b):
    '''
    Zip together two waveforms, a and b, by returning
    |a1|b1|a2|b2|a3|...
    '''


def mix_waves(a, b, c_a, c_b):
    '''
    a and b are waveforms and c_a and c_b are the relative
    amplitude scalars for each waveform. Return a mixed
    waveform where each sample is c_a*a_i + c_b*b_i.
    '''

def fade(wave, start_val, stop_val):
    '''
    fades a waveform such that the first sample has a scaling
    factor of start_val and the last has a scaling factor of
    stop_val where the scales increase linearly from start to
    finish.
    '''
