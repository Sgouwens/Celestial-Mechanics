import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Define the signal parameters
fs = 3000  # Sampling frequency in Hz
t = np.arange(0, 1, 1/fs)  # Time vector from 0 to 1 second with 1/fs spacing

n_sigs = 2
f_signals = np.array([5.5])# np.random.randint(1,10,n_sigs)+0.5
amplitudes = np.array([8])# np.random.uniform(0,1,n_sigs)  # Signal amplitude

# Generate a simple sinusoidal signal
def tfun(t):
    return np.sum(amplitudes * np.sin(2 * np.pi * f_signals * t))
tfun_v = np.vectorize(tfun)
    
signal = tfun_v(t)#amplitude * np.sin(2 * np.pi * f_signal * t)

# Plot the generated signal
plt.figure(figsize=(10, 4))
plt.subplot(3, 1, 1)
plt.plot(t, signal)
plt.title('Generated Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Apply FFT to the signal
n = len(signal)  # Length of the signal
k = np.arange(n)
T = n/fs
frq = k/T  # Frequency range
frq = frq[range(n//2)]  # One side frequency range

# Apply FFT and normalize
Y = fft(signal)/n
Y = Y[range(n//2)]

# Plot the frequency domain representation
plt.subplot(3, 1, 2)
plt.stem(frq[:15], np.abs(Y)[:15])
plt.title('FFT of the Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')


def tfunREQ(t):
    return np.sum(Y * np.sin(2 * np.pi * FRQ * t))
tfun_v = np.vectorize(tfun)

signalreq = tfun_v(t)

plt.subplot(3, 1, 3)
plt.plot(t, signalreq)
plt.title('FFT of the Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

sqerror = np.sum((signal-signalreq)**2)
print("Error is", sqerror)

