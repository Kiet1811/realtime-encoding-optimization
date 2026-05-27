import subprocess
import time

def encode_video(input_file, output_file,
                 preset="fast",
                 crf=23):

    start = time.time()

    command = [
        "ffmpeg",
        "-y",
        "-i", input_file,
        "-c:v", "libx264",
        "-preset", preset,
        "-crf", str(crf),
        output_file
    ]

    subprocess.run(command)

    end = time.time()

    return end - start
