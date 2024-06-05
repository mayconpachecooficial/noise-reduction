import sounddevice as sd
import numpy as np
import noisereduce as nr
import tkinter as tk
from tkinter import ttk

# Configurações de áudio
fs = 44100  # taxa de amostragem (Hz)
duration = 0.5  # duração do bloco de gravação em segundos

class NoiseReductionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Noise Reduction App")

        self.noise_reduction_level = tk.DoubleVar(value=50)

        self.create_widgets()
        self.start_audio_stream()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Noise Reduction Level:").grid(row=0, column=0, sticky=tk.W)
        self.slider = ttk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, variable=self.noise_reduction_level)
        self.slider.grid(row=0, column=1, sticky=(tk.W, tk.E))

        self.start_button = ttk.Button(frame, text="Start", command=self.start_audio_stream)
        self.start_button.grid(row=1, column=0, sticky=tk.W)

        self.stop_button = ttk.Button(frame, text="Stop", command=self.stop_audio_stream)
        self.stop_button.grid(row=1, column=1, sticky=tk.E)

    def start_audio_stream(self):
        self.stream = sd.Stream(callback=self.callback, channels=2, samplerate=fs, blocksize=int(duration * fs),
                                device=('CABLE Output (VB-Audio Virtual Cable)', 'CABLE Input (VB-Audio Virtual Cable)'))
        self.stream.start()

    def stop_audio_stream(self):
        if hasattr(self, 'stream'):
            self.stream.stop()

    def callback(self, indata, outdata, frames, time, status):
        if status:
            print(status)
        # Converter áudio para mono
        audio_mono = np.mean(indata, axis=1)
        # Reduzir o ruído com base no nível de redução ajustado
        reduction_level = self.noise_reduction_level.get() / 100
        reduced_noise = nr.reduce_noise(y=audio_mono, sr=fs, prop_decrease=reduction_level)
        # Repassar o áudio processado para a saída
        outdata[:] = np.tile(reduced_noise, (2, 1)).T

def main():
    root = tk.Tk()
    app = NoiseReductionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
