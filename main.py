import cv2
from pathlib import Path

DATA_DIRECTORY = Path("data")
CAPTURE_INTERVAL_SECONDS = 2
JPEG_QUALITY = 95


def extract_frames(video_path: Path, output_directory: Path) -> int:
    capture = cv2.VideoCapture(str(video_path))

    if not capture.isOpened():
        capture.release()
        raise RuntimeError(f"Could not open video: {video_path}")

    frame_count = 0

    try:
        output_directory.mkdir(parents=True, exist_ok=True)

        while True:
            success, frame = capture.read()

            if not success:
                break

            relative_seconds = frame_count * CAPTURE_INTERVAL_SECONDS
            filename = (
                f"frame_{frame_count:05d}" f"_relative_{relative_seconds:05d}s.jpg"
            )
            output_path = output_directory / filename

            if output_path.exists():
                raise FileExistsError(f"Output file already exists: {output_path}")

            saved = cv2.imwrite(
                str(output_path),
                frame,
                [cv2.IMWRITE_JPEG_QUALITY, JPEG_QUALITY],
            )

            if not saved:
                raise RuntimeError(f"Could not save image: {output_path}")

            frame_count += 1

    finally:
        capture.release()

    return frame_count


def main() -> None:
    for clip_name in ("cut1", "cut2", "cut3"):
        clip_directory = DATA_DIRECTORY / clip_name
        video_path = clip_directory / f"{clip_name}_360.mp4"
        output_directory = clip_directory / "images"

        frame_count = extract_frames(video_path, output_directory)

        print(f"{clip_name}: saved {frame_count} frames " f"to {output_directory}")


if __name__ == "__main__":
    main()
