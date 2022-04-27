import numpy as np
import matplotlib.pyplot as plt

from tools import save_audio

def sample_to_time(sample_ind: int, sr: int):
    '''
    takes in a sample index and sample rate and returns
    the time value in seconds that correspond to the index
    '''
    return sample_ind / sr


def samples_to_time(sample_inds: np.ndarray, sr: int):
    '''
    achieves the same as sample_to_time() but for an 1-D array
    of sample indices
    '''
    temp = []
    for i in range(sample_inds.shape[0]):
        temp.append(sample_to_time(sample_inds[i], sr))
    times=np.asarray(temp)    
    return times
    

def gen_time(duration: int, sr: int):
    '''
    Returns time stamps in seconds for the given duration (in seconds!)
    at the given sample rate.
    '''
    return np.linspace(0, duration, duration * sr)




def single_period(sr: int):
    '''
    takes in a sample rate and returns values linearly spaced
    between 0 and the value at which the sine function completes
    one cycle.
    '''
    return np.linspace(0, 2 * np.pi, sr)


def single_sine(sr: int):
    '''
    Return the results of the sine function for a single cycle
    at the given sample rate.
    '''
    # In this function we should use single_period() to generate the x-axis that the sine function takes as input. Return the results of the sine function
    x = single_period(sr)
    return np.sin(x)
    


def sine5(sine_hz: int, sr: int):
    '''
    returns a sine wave with a 5 second duration sampled with the
    given sample rate and at a given frequency
    '''
    # returns a sine wave with a 5 second duration sampled with the given `sr` and a frequency corresponding to `sine_hz`
    return np.sin(gen_time(5, sr) * sine_hz * 2 * np.pi)


def sine(sine_hz: int, sr: int, duration: int):
    '''
    Returns a sine wave of a given frequency, of a given duration
    sampled at a given sample rate.
    '''
    return np.sin(gen_time(duration, sr) * sine_hz * 2 * np.pi)


def save_sine():
    '''
    Use your sine function to generate a 5 second sine wave with
    a frequency of 500 Hz, sampled at 16K Hz. Your file will be
    stored at `./data/my_sine.wav`
    '''
    sr = 16000

    sine_wave = sine(500, sr, 5)
    save_audio(sine_wave, sr, './data/my_sine.wav')


def low_sine():
    sr = 48000
    sine_wave = sine(20, sr, 1)
    save_audio(sine_wave, sr, './data/low_sine.wav')


def high_sine():
    sr = 48000
    sine_wave = sine(20000, sr, 1)
    save_audio(sine_wave, sr, './data/high_sine.wav')


if __name__ == "__main__":
    print(samples_to_time(np.arange(0, 22050, 512), 22050))
    print(gen_time(1,10))
    print(single_period(10))
    print(single_sine(10))

    #==========================================================
    # 2.3
    #==========================================================
    plt.plot(samples_to_time(single_period(10),10), single_sine(10) )
    plt.title('Sine wave with a sample rate of 10Hz')
    plt.show()
    plt.plot(samples_to_time(single_period(50),50), single_sine(50) )
    plt.title('Sine wave with a sample rate of 50Hz')
    plt.show()
    plt.plot(samples_to_time(single_period(100),100), single_sine(100) )
    plt.title('Sine wave with a sample rate of 100Hz')
    plt.show()
    
    #==========================================================
    # 2.4
    #==========================================================
    plt.plot(gen_time(5,5), sine5(1, 5), label="sine5(1,5)", color="red" )
    plt.plot(gen_time(5,10), sine5(1, 10), label="sine5(1,10)", color="green" )
    plt.plot(gen_time(5,100), sine5(1, 100), label="sine5(1,100)", color="orange" )
    plt.title("Sine wave with different frequencies")
    plt.legend(['5Hz','10Hz','100Hz'])
    plt.show()
    
    #==========================================================
    # 2.5
    #==========================================================
    plt.plot(gen_time(2,1000), sine(1, 1000, 2), label="sine(1, 1000, 2)", color="red" )
    plt.plot(gen_time(2,1000), sine(5, 1000, 2), label="sine(5, 1000, 2)", color="green" )
    plt.plot(gen_time(2,1000), sine(20, 1000, 2), label="sine(20, 1000, 2)", color="orange" )
    plt.title("Sine waves with different frequencies")
    plt.legend(['1Hz, sr=1000, duration=2','5Hz, sr=1000, duration=2','20Hz, sr=1000, duration=2'])
    plt.show()
    
    
    #==========================================================
    # 3. LISTEN TO THE SINE WAVE
    # 3.1
    #==========================================================
    save_sine()
    
    #==========================================================
    # 3.2
    # We can only represent frequencies up to half the sample # rate. This is called the Nyquist frequency.
    #==========================================================
    low_sine()
    high_sine()