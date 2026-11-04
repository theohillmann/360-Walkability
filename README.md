# 360-Walkability

A tool for assessing walkability from route videos, including 360° recordings. Built with Python and Streamlit, the **WalkLabel** application extracts video frames and records manual indicator assessments for each route segment.

## Features

- Upload MP4, MOV, and INSV videos, subject to OpenCV decoding support.
- Display video metadata: resolution, frame rate, frame count, and playback duration. The code also attempts to detect the capture interval from Insta360 metadata.
- Extract JPEG images at a configurable frame interval.
- Preview MP4 videos and browse each segment's images.
- Assess 33 indicators with scores, justifications, and evidence images.
- Save assessments locally as CSV files and track progress by segment.

## Installation

Python and the `venv` module must be available. Run these commands from the project root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, replace the activation command with:

```powershell
.venv\Scripts\Activate.ps1
```

Dependencies and their pinned versions are listed in `requirements.txt`. The main libraries are Streamlit, OpenCV, and pandas.

## Running the application

```bash
python -m streamlit run image_annotator/app.py
```

Open the address displayed by Streamlit in your browser. Run the application from the project root because data paths are relative to that directory.

### 1. Extract frames

1. Open **Extract frames** and upload a video.
2. Review the displayed metadata.
3. Set **Frame Interval**: `1` saves every frame; `10` saves one out of every ten frames. This value is measured in frames, not seconds.
4. Click **Save frames**.

Images are saved to `data/<video_name>/images/`, with names such as `frame_000000.jpg`. A copy of the video is also stored in the segment folder if a file with the same name does not already exist.

Extraction stops if a destination image already exists. To repeat the operation, use a different video name or move the previous results before starting. An interrupted extraction may leave already extracted images in the folder.

### 2. Assess a segment

1. Open **Classify frames**.
2. Select a segment in the sidebar. The application lists folders in `data/` that contain an `images/` subfolder.
3. Review the video in the **Video** tab or browse images in the **Frames** tab.
4. Select an indicator and review its criteria under **PDF criteria**.
5. Choose a score, enter a justification, and select evidence frames.
6. Click **Save assessment** to save that indicator's assessment.

The score applies to the **entire segment**. Selected frames document the evidence supporting the assessment. **Not assessed** leaves the indicator without a score. Saving an indicator again replaces its previous assessment.

## Indicators

| Codes | Dimension | Count |
| --- | --- | ---: |
| AC1–AC8 | Path conditions and accessibility | 8 |
| AE1–AE4 | Trees, greenspace, maintenance, and cleanliness | 4 |
| L1–L8 | Land use and services | 8 |
| S1–S8 | Safety and interactions with vehicles | 8 |
| T1–T5 | Public transportation infrastructure and service | 5 |

Score options vary by indicator and are defined in `image_annotator/pages/classify_frames.py`. Indicator S4 also accepts intermediate values to record the average score of both sides of the street. When information cannot be verified from the images, document the limitation in the justification or leave the indicator unassessed.

## Project structure

```text
360-Walkability/
├── README.md
├── requirements.txt
├── main.py                         # Extract frames from three predefined clips
├── frame_by_frame.py               # Local OpenCV frame viewer
├── image_annotator/
│   ├── app.py                      # WalkLabel home page
│   └── pages/
│       ├── extract_frames.py       # Video upload and frame extraction
│       └── classify_frames.py      # Segment assessment
└── data/
    └── <segment>/
        ├── <video>.mp4              # Original video; extension may vary
        └── images/
            ├── frame_000000.jpg
            └── annotations.csv
```

You can also manually populate `data/<segment>/images/` with JPG, JPEG, or PNG images. The video preview on the assessment page only looks for files with the `.mp4` extension in the segment folder.

## Assessment format

Each segment has its own `data/<segment>/images/annotations.csv` file:

| Column | Contents |
| --- | --- |
| `indicator` | Indicator code, such as `AC1` or `T5` |
| `score` | Selected score; empty when unassessed |
| `justification` | Justification, observations, and limitations |
| `evidence_frames` | Evidence image filenames separated by `;` |

The file is created when the first assessment is saved. Existing assessments are loaded when opening the segment.

## Auxiliary scripts

### `main.py`

```bash
python main.py
```

Processes `data/cut1/cut1_360.mp4`, `data/cut2/cut2_360.mp4`, and `data/cut3/cut3_360.mp4`, saving images to their respective `images/` folders at JPEG quality 95.

**Note:** this script reads and saves every frame. The constant `CAPTURE_INTERVAL_SECONDS = 2` is only used to calculate the time included in filenames; it does not sample frames or verify actual video timing. These filenames should therefore not be treated as verified timestamps.

### `frame_by_frame.py`

Displays frames in an OpenCV window. Before running it, update the absolute video path in the script, which currently points to a file on the author's machine:

```bash
python frame_by_frame.py
```

Press Space to advance and `Esc` to exit. The script requires an environment that supports graphical windows.