import numpy as np
import subprocess

from tools import read_audio, save_audio


def say_phone(number: str, out_path:str, play: bool = False):
    '''
    Takes in e.g. "5812345" and saves a synthesized
    waveform for the phone number at <out_path>
    '''
    parts = []
    start, sr = read_audio('./data/start.wav')
    parts.append(start)
    for digit in number:
        parts.append(generate_digit(digit))

    output = splice(parts)

    save_audio(output, sr, out_path)
    if play:
        subprocess.call(['play', out_path])


def generate_digit(digit):
    part, _ = read_audio(f'./data/{digit}.wav')
    return part


def splice(parts):
    return np.hstack(parts)


if __name__ == '__main__':
    say_phone('58122345', './data/ex.wav')
    # you can also use the following if you have
    # sox installed on your system.
    # say_phone('5812345', './data/ex.wav', play=True)
