import numpy as np
import matplotlib.pyplot as plt
import librosa


from tools import save_audio, read_audio, plot_spectrum, plot_spectrogram

'''
Put your sine function from assignment 1 here.
'''
def gen_time(duration: int, sr: int):
    '''
    Returns time stamps in seconds for the given duration (in seconds!)
    at the given sample rate.
    '''
    return np.linspace(0, duration, duration * sr)

def sine(sine_hz: int, sr: int, duration: int):
    '''
    Returns a sine wave of a given frequency, of a given duration
    sampled at a given sample rate.
    '''
    return np.sin(gen_time(duration, sr) * sine_hz * 2 * np.pi)

def multi_sine(C, F, sr, duration):
    '''
    Returns a weighted sum of frequency components.
    C should be a list of relative ampltiudes and F
    is a list of frequencies.
    '''
    weighted_sum = 0
    for i in range(len(C)):
        weighted_sum += C[i] * sine(F[i], sr, duration)
    return weighted_sum


def half_sr(wave):
    '''
    Given a waveform, half the number of samples by
    removing every second sample.
    '''
    return wave[::2]


def zip_waves(a, b):
    '''
    Zip together two waveforms, a and b, by returning
    |a1|b1|a2|b2|a3|...
    '''
    # cut the longer recording to be equal in length to the shorter
    max_samples = min(a.shape[0], b.shape[0])
    a = a[:max_samples]
    b = b[:max_samples]
    ziped_wave = []
    for i in range(max_samples):
        ziped_wave.append(a[i])
        ziped_wave.append(b[i])
    return ziped_wave


def mix_waves(a, b, c_a, c_b):
    '''
    a and b are waveforms and c_a and c_b are the relative
    amplitude scalars for each waveform. Return a mixed
    waveform where each sample is c_a*a_i + c_b*b_i.
    '''
    max_samples = min(a.shape[0], b.shape[0])
    a = a[:max_samples]
    b = b[:max_samples]    
    mixed_wave = []
    for i in range(max_samples):
        mixed_wave.append(c_a*a[i] + c_b*b[i])
    return mixed_wave

def fade(wave, start_val, stop_val):
    '''
    fades a waveform such that the first sample has a scaling
    factor of start_val and the last has a scaling factor of
    stop_val where the scales increase linearly from start to
    finish.
    '''
    gradient = np.linspace(start_val, stop_val, wave.shape[0])
    for i in range(wave.shape[0]):
        wave[i] *= gradient[i]
    return wave
    
def main():
    c = [1, 0.5, 0.1, 0]
    f = [500, 1000, 2000, 5000] 
    save_audio(multi_sine(c, f, 16000, 5), 16000, './data/multi_sine.wav')
    print("Multi sine spectrum")
    plot_spectrum(multi_sine(c, f, 16000, 5), 16000)
    # plot spectrogram of the multi_sine
    print("Multisine spectrogramm")
    plot_spectrogram(multi_sine(c, f, 16000, 5), 16000)

    # plot spectrogram of the f1.wav file in ./data/f1.wav
    wave, sr = read_audio('./data/f1.wav')
    print("F1 spectrogramm")
    plot_spectrogram(wave, sr)
    
    # plot spectrogram of the f1.wav file
    wave2,sr2 = read_audio('./data/f1.wav')
    print("F1 spectrogramm")
    plot_spectrogram(wave2, sr2)
    
    #plot spectrogram of the f1.wav file with half samples
    half_wave = half_sr(wave)
    save_audio(half_wave, sr2, './data/half_sr.wav')
    print("Half F1 spectrogramm")
    plot_spectrogram(half_wave, sr)
    
    #plot spectrogram of the f1.wav file with half samples and half sample rate
    save_audio(half_wave, sr2//2, './data/half_sr2.wav')
    print("Half F1 half sr spectrogramm")
    plot_spectrogram(half_wave, sr//2)
    
    # Next repeat step two but remove ever more samples while
    # reducing the sample rate at an equal rate. Compare the 
    # output for sr, sr/2, sr/4, sr/8, sr/16. sr/32.
    # sr
    wave3,sr3 = read_audio('./data/m2.wav')
    print(f"sr {sr3}")
    # sr/2
    wave4,sr4 = half_sr(wave3), sr3//2
    save_audio(wave4, sr4, './data/sr_over_2_m2.wav')
    print(f"sr/2 {sr4}")
    # sr/4
    wave5,sr5 = half_sr(wave4), sr4//2
    save_audio(wave5, sr5, './data/sr_over_4_m2.wav')
    print(f"sr/4 {sr5}")
    # sr/8
    wave6,sr6 = half_sr(wave5), sr5//2
    save_audio(wave6, sr6, './data/sr_over_8_m2.wav')
    print(f"sr/8 {sr6}")
    # sr/16
    wave7,sr7 = half_sr(wave6), sr6//2
    save_audio(wave7, sr7, './data/sr_over_16_m2.wav')
    print(f"sr/16 {sr7}")
    # sr/32
    wave8,sr8 = half_sr(wave7), sr7//2
    save_audio(wave8, sr8, './data/sr_over_32_m2.wav')
    print(f"sr/32 {sr8}")
    
    # ziping waves
    wave9,sr9 = read_audio('./data/f1.wav')
    wave10, _ = read_audio('./data/f2.wav')
    ziped_wave = zip_waves(wave9, wave10)
    save_audio(ziped_wave, sr9, './data/ziped.wav')  
    plt.plot(ziped_wave)
    plt.title("Ziped wave")
    plt.show()
    save_audio(ziped_wave, sr9*2, './data/ziped_normal.wav')  
    
    # mixing waveforms
    mixed_wave = mix_waves(wave9, wave10, 4, 0.25)
    plt.plot(mixed_wave)
    plt.title("Mixed wave")
    plt.show()
    save_audio(mixed_wave, sr9, './data/mixed.wav')
    
    #fading waveform
    wave11, sr11 = read_audio('./data/m2.wav')
    fade_wave = fade(wave11, 0, 1)
    plt.plot(fade_wave)
    plt.title("Fade wave")
    plt.show()
    save_audio(fade_wave, sr11, './data/fade.wav')

    #4: COMBINE
    # 1. Open f1.wav and m2.wav
    # 2. Take the first 0 to 3 seconds of f1.wav and m2.wav
    # 3. Mix the segments together, with a coefficient of  
    #    2 for f1.wav and 0.25 for m2.wav
    # 4. Same step as 3. but with a coefficient of 0.25 
    #    for f1.wav and 2 for m2.wav
    # 5. Take the same segments from f1.wav and m2.wav and 
    #    zip them together while using half the sample rate
    #    so the sound is not distorded
    # 6. Fade f1.wav from 0 to 2 and m2.wav from 0 to 0
    # 7. Concatenate the different waves together to be    
    #    able to hear each transformation separatly
    # 8. Save the result as combination_f1m2.wav in ./data/
    wave_f1, rs_f1 = read_audio('./data/f1.wav')
    wave_m2, rs_m2 = read_audio('./data/m2.wav')
    
    f1_start1 = int (0 * rs_f1)
    f1_end1 = int (3 * rs_f1)
    f1_segment1 = wave_f1[f1_start1:f1_end1]
    m2_start1 = int (0 * rs_m2)
    m2_end1 = int (3 * rs_m2)
    m2_segment1 = wave_m2[m2_start1:m2_end1]
    first_mix = mix_waves(f1_segment1, m2_segment1, 2, 0.25)
    f1_start2 = int (0 * rs_f1)
    f1_end2 = int (3 * rs_f1)
    f1_segment2 = wave_f1[f1_start2:f1_end2]
    m2_start2 = int (0 * rs_m2)
    m2_end2 = int (3 * rs_m2)
    m2_segment2 = wave_m2[m2_start2:m2_end2]
    second_mix = mix_waves(f1_segment2, m2_segment2, 0.25, 2 )
    
    f1_start3 = int (0 * rs_f1 * 2)
    f1_end3 = int (3 * rs_f1 * 2)
    f1_segment3 = wave_f1[f1_start3:f1_end3]
    m2_start3 = int (0 * rs_m2 * 2)
    m2_end3 = int (3 * rs_m2 * 2)
    m2_segment3 = wave_m2[m2_start3:m2_end3]

    ziped = zip_waves(half_sr(f1_segment3), half_sr(m2_segment3))
    
    fade_f1 = fade(wave_f1, 0, 2)
    fade_m2 = fade(wave_m2, 2, 0)
    
    final_wave = np.concatenate((first_mix, second_mix, ziped, fade_f1, fade_m2))


    
    plt.plot(final_wave)
    plt.title("Ziped and faded segments from f1.wav and m2.wav")
    plt.show()
    save_audio(final_wave, sr11, './data/combination_f1m2.wav')
    
    

if __name__ == '__main__':
    main()