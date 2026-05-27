import streamlit as st
import os

from app.encoder import encode_video
from app.metrics import compression_ratio
from app.metrics import get_bitrate
from app.metrics import calculate_psnr

st.title("Real-Time Encoding Optimization")

uploaded_file = st.file_uploader(
    "Upload Video",
    type=["mp4", "mov", "avi"]
)

preset = st.selectbox(
    "Encoding Preset",
    ["ultrafast", "fast", "medium", "slow"]
)

crf = st.slider(
    "CRF Value",
    18,
    35,
    23
)

if uploaded_file:

    input_path = "datasets/input.mp4"

    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    st.subheader("Original Video")
    st.video(input_path)

    if st.button("Start Encoding"):

        output_path = "outputs/output.mp4"

        encoding_time = encode_video(
            input_path,
            output_path,
            preset,
            crf
        )

        ratio = compression_ratio(
            input_path,
            output_path
        )

        bitrate = get_bitrate(output_path)

        psnr = calculate_psnr(
            input_path,
            output_path
        )

        st.subheader("Compressed Video")
        st.video(output_path)

        st.subheader("Metrics")

        st.write(f"Encoding Time: {encoding_time:.2f} sec")
        st.write(f"Compression Ratio: {ratio:.2f}")
        st.write(f"Bitrate: {bitrate:.2f} kbps")
        st.write(f"PSNR: {psnr:.2f}")
