import numpy as np
import matplotlib.pyplot as plt
import matplotlib

SIG_AMPLITUDE = 10; SIG_OFFSET = 2; SIG_PERIOD = 100
NOISE_AMPLITUDE = 3
N_SAMPLES = 5 * SIG_PERIOD
INSETRUMENT_RANGE = 9

times = np.arange(N_SAMPLES).astype(float)
signal = SIG_AMPLITUDE * np.sin(2 * np.pi * times /SIG_PERIOD) + SIG_OFFSET
noise = NOISE_AMPLITUDE * np.random.normal(size=N_SAMPLES)
signal += noise

signal[signal > INSETRUMENT_RANGE] = INSETRUMENT_RANGE
signal[signal < -INSETRUMENT_RANGE] = -INSETRUMENT_RANGE

matplotlib.style.use("ggplot")
plt.plot(times, signal)
plt.title("Synthetic sine wave signal")
plt.xlabel("Time")
plt.ylabel("Signal + noise")
plt.ylim(ymin = - SIG_AMPLITUDE, ymax = SIG_AMPLITUDE)

# plt.savefig("signal.pdf")