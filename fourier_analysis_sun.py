import matplotlib.pyplot as plt
from scipy.fft import fft

# Extracting suns position and correcting for slope
pos_sun_x = pos_sun[:,0]
steps = len(pos_sun_x)
slope, intercept = np.polyfit(list(range(len(pos_sun_x))), pos_sun_x, 1)
pos_sun_x -= [slope*x-intercept for x in list(range(len(pos_sun_x)))]

sec_per_year = 60*60*24*365.25

# Define the necessary constants
fs = sec_per_year/3600  # Sampling frequency in Hz
t = np.arange(0, steps*3600, 3600)  # Time vector from 0 to 1 second with 1/fs spacing

# Plot movement of sun.
plt.figure(figsize=(10, 4))
plt.subplot(3, 1, 1)
plt.plot(t, pos_sun_x)
plt.title('Generated Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Apply FFT to the signal
k = np.arange(steps)
T = steps/fs
frq = k/T  # Frequency range
frq = frq[range(steps//2)]  # One side frequency range

pos_sun_fft = fft(pos_sun_x)

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
plt.stem(frq[:100], np.abs(Y)[:100])
plt.title('FFT of the Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')


def tfunREQ(t):
    return np.sum(Y * np.sin(2 * np.pi * frq * t))
tfun_v = np.vectorize(tfun)

signalreq = tfun_v(t)

plt.subplot(3, 1, 3)
plt.plot(t, signalreq)
plt.title('FFT of the Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

sqerror = np.sum((signal-signalreq)**2)
print("Error is", sqerror)