import wave as wave
import scipy.signal as sp
import numpy as np
import matplotlib.pyplot as plt

DATA_DIR = 'src/static/data/'
SAVE_DIR = 'src/static/image/'
NPERSEG = 512
NOVERLAP = NPERSEG // 2


def fourier(dt_txt):
    fname = '{}{}.wav'.format(DATA_DIR, dt_txt)
    wav = wave.open(fname, 'rb')
    data = wav.readframes(wav.getnframes())
    data = np.frombuffer(data, dtype=np.int16)

    f, t, stft_data = sp.stft(data, fs=wav.getframerate(), window='hann',
                              nperseg=NPERSEG, noverlap=NOVERLAP)

    return f, t, stft_data


def make_fourier_graph(f, t, stft_data, dt_txt):
    plt.switch_backend('agg')
    plt.figure(figsize=(8, 4))
    stft_data = 10 * np.log(np.abs(stft_data))
    plt.pcolormesh(t, f, stft_data, cmap='jet')
    plt.colorbar().set_label('Intensity [dB]')
    plt.xlabel('Time [sec]')
    plt.ylabel('Frequency [Hz]')
    plt.savefig('{}{}.png'.format(SAVE_DIR, dt_txt))


def main(dt_txt):
    f, t, stft_data = fourier(dt_txt)
    make_fourier_graph(f, t, stft_data, dt_txt)


if __name__ == '__main__':
    main()
