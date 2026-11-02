import cv2
import struct
import shutil
import tempfile
import streamlit as st
from pathlib import Path


def upload_video():
    uploaded_file = st.file_uploader(
        "Upload a video", type=["mp4", "mov", "insv"], max_upload_size=2000
    )

    if uploaded_file is None:
        st.write("Please upload a video.")
        st.stop()

    st.success("File uploaded.")
    st.write(f"**File name:** {uploaded_file.name}")
    st.write(f"**File size:** {uploaded_file.size / (1024 ** 2):.1f} MB")
    return uploaded_file


def read_metadata(uploaded_file):
    metadata = {}

    uploaded_file.seek(0, 2)
    file_size = uploaded_file.tell()

    if file_size >= 78:
        uploaded_file.seek(file_size - 72)
        footer = uploaded_file.read(72)

        if footer[40:] == b"8db42d694ccc418790edff439fe026bf":
            metadata_start = file_size - struct.unpack_from("<I", footer, 32)[0]
            position = file_size - 72

            while position - 6 >= metadata_start:
                uploaded_file.seek(position - 6)
                version, record_type, size = struct.unpack(
                    "<BBI", uploaded_file.read(6)
                )
                position -= size + 6

                if position < metadata_start:
                    break

                if record_type != 1:
                    continue

                if version != 1:
                    break

                uploaded_file.seek(position)
                data = uploaded_file.read(size)
                offset = 0
                fields = {}

                def read_integer():
                    nonlocal offset
                    value = 0

                    for shift in range(0, 70, 7):
                        byte = data[offset]
                        offset += 1
                        value |= (byte & 127) << shift

                        if byte < 128:
                            return value

                    raise ValueError("Invalid metadata integer.")

                try:
                    while offset < len(data):
                        key = read_integer()
                        field, wire_type = key >> 3, key & 7

                        if wire_type == 0:
                            fields[field] = read_integer()
                        elif wire_type == 1:
                            offset += 8
                        elif wire_type == 2:
                            length = read_integer()
                            offset += length
                        elif wire_type == 5:
                            offset += 4
                        else:
                            break

                    if 30 in fields and fields.get(59) == 1:
                        metadata["capture_interval_seconds"] = fields[30] / 1000

                except (IndexError, ValueError):
                    metadata["insta360_metadata_error"] = (
                        "Could not decode capture metadata."
                    )

                break

    uploaded_file.seek(0)

    with tempfile.TemporaryDirectory() as directory:
        video_path = Path(directory) / "video.insv"

        with video_path.open("wb") as file:
            while chunk := uploaded_file.read(1024 * 1024):
                file.write(chunk)

        uploaded_file.seek(0)
        capture = cv2.VideoCapture(str(video_path))

        try:
            if not capture.isOpened():
                raise ValueError("Could not open the video.")

            fps = capture.get(cv2.CAP_PROP_FPS)
            frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

            metadata.update(
                {
                    "width": int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    "height": int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                    "fps": fps,
                    "frame_count": frame_count,
                    "playback_duration_seconds": (
                        frame_count / fps if fps > 0 else None
                    ),
                }
            )

            return metadata

        finally:
            capture.release()


def save_frames(uploaded_file, frame_interval=1):
    if frame_interval < 1:
        raise ValueError("Frame interval must be at least 1.")

    video_name = Path(uploaded_file.name).stem
    output_directory = Path("data") / video_name / "images"
    output_directory.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as directory:
        video_path = Path(directory) / "video.insv"
        uploaded_file.seek(0)

        with video_path.open("wb") as file:
            while chunk := uploaded_file.read(1024 * 1024):
                file.write(chunk)

        uploaded_file.seek(0)
        capture = cv2.VideoCapture(str(video_path))
        saved_video_path = output_directory.parent / Path(uploaded_file.name).name

        if not saved_video_path.exists():
            shutil.copy2(video_path, saved_video_path)

        saved_count = 0
        frame_index = 0

        try:
            if not capture.isOpened():
                raise ValueError("Could not open the video.")

            while True:
                success, frame = capture.read()

                if not success:
                    break

                if frame_index % frame_interval == 0:
                    image_path = output_directory / f"frame_{frame_index:06d}.jpg"

                    if image_path.exists():
                        raise FileExistsError(f"Image already exists: {image_path}")

                    if not cv2.imwrite(str(image_path), frame):
                        raise RuntimeError(f"Could not save: {image_path}")

                    saved_count += 1

                frame_index += 1

        finally:
            capture.release()

    return saved_count, output_directory


def main():
    uploaded_file = upload_video()

    if uploaded_file is not None:
        metadata = read_metadata(uploaded_file)
        st.json(metadata)

        frame_interval = st.number_input("Frame Interval", value=1, min_value=1)
        if st.button("Save frames"):
            saved_count, output_directory = save_frames(
                uploaded_file, frame_interval=frame_interval
            )
            st.success(f"Saved {saved_count} frames to {output_directory}")


if __name__ == "__main__":
    main()
