import numpy as np
import matplotlib.pyplot as plt

from tools import save_audio

def sample_to_time(sample_ind: int, sr: int):
    '''
    takes in a sample index and sample rate and returns
    the time value in seconds that correspond to the index
    '''
    return sample_ind * sr


def samples_to_time(sample_inds: np.ndarray, sr: int):
    '''
    achieves the same as sample_to_time() but for an 1-D array
    of sample indices
    '''

def gen_time(duration: int, sr: int):
    '''
    Returns time stamps in seconds for the given duration (in seconds!)
    at the given sample rate.
    '''




def single_period(sr: int):
    '''
    takes in a sample rate and returns values linearly spaced
    between 0 and the value at which the sine function completes
    one cycle.
    '''


def single_sine(sr: int):
    '''
    Return the results of the sine function for a single cycle
    at the given sample rate.
    '''


def sine5(sine_hz: int, sr: int):
    '''
    returns a sine wave with a 5 second duration sampled with the
    given sample rate and at a given frequency
    '''


def sine(sine_hz: int, sr: int, duration: int):
    '''
    Returns a sine wave of a given frequency, of a given duration
    sampled at a given sample rate.
    '''


def save_sine():
    '''
    Use your sine function to generate a 5 second sine wave with
    a frequency of 500 Hz, sampled at 16K Hz. Your file will be
    stored at `./data/my_sine.wav`
    '''
    sr = ...

    sine_wave = ...
    save_audio(sine_wave, sr, './data/my_sine.wav')


def low_sine():
    sr = ...
    sine_wave = ...
    save_audio(sine_wave, sr, './data/low_sine.wav')


def high_sine():
    sr = ...
    sine_wave = ...
    save_audio(sine_wave, sr, './data/high_sine.wav')


if __name__ == "__main__":
    print(samples_to_time(10, 100))