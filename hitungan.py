sample_rates = [8000, 44100, 48000]
bit_depths = [8, 16, 24]
channels = [1, 2]
durasi = 10  # detik

for sr in sample_rates:
    for bit in bit_depths:
        for channel in channels:

            # Menghitung ukuran audio dalam byte
            ukuran = sr * (bit / 8) * channel * durasi

            # Menentukan jenis channel
            jenis_channel = "Mono" if channel == 1 else "Stereo"

            print(
                f"{sr} Hz | "
                f"{bit} bit | "
                f"{jenis_channel} | "
                f"{ukuran:.0f} byte"
            )
