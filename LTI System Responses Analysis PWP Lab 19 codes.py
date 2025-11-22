# untitled0.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# Ensure inline backend when running inside Spyder/IPython
matplotlib.use('module://matplotlib_inline.backend_inline')

from scipy.signal import freqz

def pole_zero_plot(zeros, poles, title='Pole-Zero Plot'):
    fig, ax = plt.subplots(figsize=(6,6))
    # unit circle
    theta = np.linspace(0, 2*np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), linestyle='--', linewidth=0.8, label='Unit circle')

    if zeros.size > 0:
        ax.scatter(zeros.real, zeros.imag, marker='o', facecolors='none', edgecolors='C0', s=80, label='Zeros')
    if poles.size > 0:
        ax.scatter(poles.real, poles.imag, marker='x', color='C3', s=80, label='Poles')

    ax.axhline(0, linewidth=0.5)
    ax.axvline(0, linewidth=0.5)
    ax.set_title(title)
    ax.set_xlabel('Real(z)')
    ax.set_ylabel('Imag(z)')
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, linestyle=':', linewidth=0.6)
    ax.legend()
    plt.tight_layout()
    return fig, ax

def analyze_z_transfer_function(num, den, worN=2048):

    # compute zeros and poles (roots of polynomials)
    zeros = np.roots(num) if len(num) > 0 else np.array([])
    poles = np.roots(den) if len(den) > 0 else np.array([])

    # Print basic info
    print("Zeros:", zeros)
    print("Poles:", poles)

    # Stability: all poles strictly inside unit circle
    stable = np.all(np.abs(poles) < 1) if poles.size > 0 else True
    print("Stability:", "Stable (all |p| < 1)" if stable else "Unstable (some |p| >= 1)")

    # Causality: proper system (degree numerator <= degree denominator)
    causal = (len(num) <= len(den))
    print("Causality:", "Causal (proper or strictly proper)" if causal else "Non-causal (improper)")

    # Typical ROC (informal)
    if causal and poles.size > 0:
        roc = f"|z| > {np.max(np.abs(poles)):.6f}  (causal ROC outside outermost pole)"
    elif (not causal) and poles.size > 0:
        roc = f"|z| < {np.min(np.abs(poles)):.6f}  (anticausal ROC inside innermost pole)"
    else:
        roc = "ROC depends on sequence (not determined from rational function alone)"
    print("Typical ROC (informal):", roc)

    print("Time Invariance: Assumed LTI (time invariant)")

    # Pole-zero plot
    pole_zero_plot(zeros, poles)

    # Frequency response (discrete-time) over [0, pi]
    w, h = freqz(num, den, worN=worN)          # w is rad/sample from 0..pi
    mag_db = 20.0 * np.log10(np.abs(h) + 1e-20)  # dB (tiny epsilon to avoid log(0))
    phase_deg = np.unwrap(np.angle(h)) * 180.0 / np.pi

    # Magnitude & Phase plots
    fig, ax = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    ax[0].plot(w, mag_db)
    ax[0].set_ylabel('Magnitude (dB)')
    ax[0].set_title('Frequency Response')
    ax[0].grid(True, linestyle=':')

    ax[1].plot(w, phase_deg)
    ax[1].set_ylabel('Phase (degrees)')
    ax[1].set_xlabel('Frequency (rad/sample)')
    ax[1].grid(True, linestyle=':')

    plt.tight_layout()
    plt.show()

    # Return data for further use
    return {
        "zeros": zeros,
        "poles": poles,
        "stable": stable,
        "causal": causal,
        "roc": roc,
        "w": w,
        "h": h
    }

if __name__ == '__main__':

    num = [1, 0, 0.5]
    den = [1, -1.5, 0.5]

    print("Running analysis for example transfer function...")
    result = analyze_z_transfer_function(num, den)

