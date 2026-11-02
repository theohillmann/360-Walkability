INDICATORS = {
    "AC1": (
        "Surface type",
        {
            1: "Grass, soil, mud, or gravel",
            2: "Asphalt",
            3: "Paving bricks",
            4: "Concrete slabs",
            5: "Continuous concrete",
        },
        "If multiple surface types are present, use the lowest score.",
    ),
    "AC2": (
        "Path maintenance",
        {
            1: "Poorly maintained; many defects and major hazards",
            3: "Moderately maintained; some defects and hazards",
            5: "Well maintained; few or no hazards",
        },
        "Assess cracks, bumps, holes, weeds, and root intrusions.",
    ),
    "AC3": (
        "Path continuity",
        {
            1: "Disjointed path without a useful route to destinations",
            5: "Useful, coherent, direct route to a campus destination",
        },
        "Assess continuity across the entire segment.",
    ),
    "AC4": (
        "Gradient",
        {
            1: "Steep slope with a sharp, rapid incline",
            3: "Moderate slope",
            5: "Flat or slight, gradual incline",
        },
        "Assess the steepest part of the segment.",
    ),
    "AC5": (
        "Temporary barriers",
        {
            1: "Many barriers: at least 5",
            3: "Some barriers: approximately 3–5",
            5: "Few or no barriers: approximately 0–2",
        },
        (
            "Count temporary surface obstructions blocking at least half "
            "the path width, such as water, ice, snow, or mud. "
            "The PDF overlaps at 5 barriers; document this case for review."
        ),
    ),
    "AC6": (
        "Cross slope",
        {
            1: "Steep cross slope",
            3: "Moderate cross slope",
            5: "Flat or gentle cross slope",
        },
        (
            "Assess the slope across the path, perpendicular to travel. "
            "Use the steepest part of the segment."
        ),
    ),
    "AC7": (
        "Sufficient vertical clearance",
        {
            1: "Insufficient vertical clearance",
            5: "Sufficient vertical clearance",
        },
        (
            "The PDF defines sufficient clearance as greater than "
            "2.5 meters (100 inches). Any vegetation below the acceptable "
            "clearance makes the answer No. Do not infer measurements "
            "from images when evidence is insufficient."
        ),
    ),
    "AC8": (
        "Public resting places",
        {
            1: "No resting places",
            3: "Approximately 1–2 resting places",
            5: "3 or more resting places",
        },
        (
            "Count structures intended for public seating near the path, "
            "generally within approximately 25 yards. Exclude restaurant "
            "and cafe seating. Count each structure only once."
        ),
    ),
    "AE1": (
        "Trees and tree cover",
        {
            1: "Small or no trees; little or no cover or shade",
            3: "Some and/or medium-height trees; some cover or shade",
            5: "Many and/or large trees; substantial cover or shade",
        },
        "Assess tree coverage along the segment.",
    ),
    "AE2": (
        "Greenspace",
        {
            1: "Little or no greenspace",
            3: "Some or moderate greenspace",
            5: "Much greenspace or a wide variety of greenery",
        },
        "Consider bushes, lawns, gardens, and recreational green areas.",
    ),
    "AE3": (
        "General maintenance",
        {
            1: "Poorly maintained",
            3: "Somewhat maintained",
            5: "Well maintained",
        },
        (
            "Assess the path and surrounding streetscape, including "
            "trees, verges, gardens, and lawns."
        ),
    ),
    "AE4": (
        "Cleanliness",
        {
            1: "Large amounts of litter and discarded material",
            3: "Some or small amounts of litter and discarded material",
            5: "Little or no litter and discarded material",
        },
        (
            "Consider rubbish, graffiti, broken glass, and other discarded "
            "items. Conditions can vary with season and climate."
        ),
    ),
    "L1": (
        "Diversity of land use",
        {
            1: "Little or no diversity; 0–1 listed amenity categories",
            3: "Some diversity; approximately 2 amenity categories",
            5: "Even distribution across 3 or more amenity categories",
        },
        (
            "Campus categories: food services; multifunctional centers; "
            "athletic/recreational facilities; teaching/lab buildings; "
            "administration; greenspace; libraries/bookstores; "
            "residences; parking. Assess the majority of the segment."
        ),
    ),
    "L2": (
        "Ground-floor retail",
        {
            1: "No buildings with ground-floor retail",
            3: "Some buildings with ground-floor retail",
            5: "Numerous buildings with ground-floor retail",
        },
        "Assess retail presence across the segment.",
    ),
    "L3": (
        "Food services",
        {1: "Absent", 5: "At least one present"},
        "Restaurants, grocery stores, or other food services.",
    ),
    "L4": (
        "Health services",
        {1: "Absent", 5: "At least one present"},
        "Pharmacies, clinical care centers, or health offices.",
    ),
    "L5": (
        "Miscellaneous services",
        {1: "Absent", 5: "At least one present"},
        "Examples include auto services, post offices, and banks.",
    ),
    "L6": (
        "Convenience stores",
        {1: "Absent", 5: "At least one present"},
        "Convenience stores or bodegas.",
    ),
    "L7": (
        "Shopping",
        {1: "Absent", 5: "At least one present"},
        "Examples include clothing, retail, and hardware stores.",
    ),
    "L8": (
        "Attractions",
        {1: "Absent", 5: "At least one present"},
        "City centers, event locations, landmarks, theaters, or skateparks.",
    ),
    "S1": (
        "Lighting",
        {
            1: "No or very little lighting",
            3: "Some lighting; incomplete coverage or wide spacing",
            5: "Extensive lighting; full coverage and/or regular spacing",
        },
        (
            "Lighting must illuminate most of the path for nighttime use. "
            "Daytime images alone may not establish nighttime performance."
        ),
    ),
    "S2": (
        "Surveillance",
        {
            1: "Visibility from less than 50% of buildings; no technology",
            3: "Visibility from 50–74%; little surveillance technology",
            5: "Visibility from at least 75%; surveillance technology present",
        },
        (
            "Consider windows, verandas, porches, CCTV, and blue-light "
            "systems. At least 75% visibility without surveillance "
            "technology receives 3 according to the PDF."
        ),
    ),
    "S3": (
        "Crossing aids",
        {
            1: "Crossing aids absent",
            5: "Crossing aids present, or primarily pedestrian-only",
        },
        "Examples include median refuges, traffic islands, and curb extensions.",
    ),
    "S4": (
        "Buffer verge width",
        {
            1: "No buffer or path",
            2: "Buffer within 1 foot of the curb",
            3: "Buffer between 1–2 feet",
            4: "Buffer between 2–3 feet",
            5: "Buffer over 3 feet, or qualifying pedestrian-only path",
        },
        (
            "Assess the separating area between pedestrian and vehicle "
            "zones. Isolated tree plantings, poles, parking meters, and "
            "bike lanes generally do not count. If a buffer exists on "
            "only one side, average the scores of both sides. "
            "A pedestrian-only path qualifies for 5 when it is not "
            "adjacent to roadways or other busy areas."
        ),
    ),
    "S5": (
        "Driveway crossovers",
        {
            1: "Most buildings have a driveway, or active vehicle sharing",
            2: "Approximately 50% of buildings have a driveway",
            3: "Approximately 25% of buildings have a driveway",
            5: "No driveways; pedestrian-only without vehicle crossovers",
        },
        "Assess proportions when few buildings are present.",
    ),
    "S6": (
        "Posted vehicle speed limit",
        {
            1: "Greater than 45 mph",
            2: "36–45 mph",
            3: "26–35 mph",
            4: "16–25 mph",
            5: "Under 15 mph, or pedestrian-only without vehicles",
        },
        (
            "Use the speed limit, not observed vehicle speed. "
            "The PDF suggests Waze Map Editor if a sign is unavailable. "
            "Exactly 15 mph is not explicitly assigned in the PDF; "
            "document this case for review."
        ),
    ),
    "S7": (
        "Traffic calming",
        {
            1: "No traffic-calming devices",
            3: "Few traffic-calming devices",
            5: "Multiple devices, or primarily pedestrian-only",
        },
        (
            "Examples include chicanes, on-street parking, chokers, "
            "closures, bump-outs, median barriers, roundabouts, speed "
            "cushions, speed bumps, and raised intersections. "
            "Consider segment size and proportion."
        ),
    ),
    "S8": (
        "Graffiti and broken glass",
        {
            1: "Large amounts",
            3: "Some or small amounts",
            5: "Little or none",
        },
        "Include the path edges and shoulders.",
    ),
    "T1": (
        "Bus stops",
        {
            1: "No bus stops",
            3: "One stop and/or stops on only one side",
            5: "Two or more stops and/or stops on both sides",
        },
        (
            "Inspect both sides. The PDF uses 'and/or'; "
            "document ambiguous quantity/distribution cases."
        ),
    ),
    "T2": (
        "Bus stop shelters",
        {
            1: "No shelter and/or no stop",
            3: "One shelter at one stop and/or on only one side",
            5: "Two or more shelters and/or shelters on both sides",
        },
        "Count each shelter once across the segment.",
    ),
    "T3": (
        "Bus stop seating",
        {
            1: "No bus stop seating and/or no stop",
            3: "Seating at one stop and/or on only one side",
            5: "Seating at two or more stops and/or on both sides",
        },
        "Count stops with seating, avoiding duplicate observations.",
    ),
    "T4": (
        "Bus stop timetables",
        {
            1: "No timetable and/or no stop",
            3: "Timetable at one stop and/or on only one side",
            5: "Timetables at two or more stops and/or on both sides",
        },
        "Verify that a timetable is identifiable.",
    ),
    "T5": (
        "Bus routes serving a stop",
        {
            1: "No stop or no current routes",
            2: "1 route",
            3: "2 routes",
            4: "3 routes",
            5: "4 or more routes",
        },
        (
            "Count routes serving the specific stop, not passing buses. "
            "The PDF suggests the Lehigh Transit app for campus routes. "
            "Identify the stop in the justification."
        ),
    ),
}


from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Assess segment",
    layout="wide",
)

DATA_DIRECTORY = Path("data")
COLUMNS = ["indicator", "score", "justification", "evidence_frames"]


def format_score(value, scores):
    if not value:
        return "Not assessed"

    numeric_value = float(value)

    if numeric_value.is_integer():
        return f"{value} — {scores[int(numeric_value)]}"

    return f"{value} — Average of both sides"


st.title("Assess segment")

segments = (
    sorted(
        folder
        for folder in DATA_DIRECTORY.iterdir()
        if folder.is_dir() and (folder / "images").is_dir()
    )
    if DATA_DIRECTORY.exists()
    else []
)

if not segments:
    st.info("No segments found.")
    st.stop()

segment = st.sidebar.selectbox(
    "Segment",
    segments,
    format_func=lambda folder: folder.name,
)

images_directory = segment / "images"
csv_path = images_directory / "annotations.csv"

try:
    annotations = (
        pd.read_csv(csv_path, dtype=str, keep_default_na=False)
        if csv_path.exists()
        else pd.DataFrame(columns=COLUMNS)
    )
except (OSError, pd.errors.ParserError, pd.errors.EmptyDataError) as error:
    st.error(f"Could not read annotations: {error}")
    st.stop()

if not set(COLUMNS).issubset(annotations.columns):
    st.error("The existing CSV has an incompatible format.")
    st.stop()

frames = sorted(
    image
    for image in images_directory.iterdir()
    if image.suffix.lower() in {".jpg", ".jpeg", ".png"}
)

videos = sorted(segment.glob("*.mp4"))
frame_names = [frame.name for frame in frames]

media_column, form_column = st.columns([3, 1])

with media_column:
    video_tab, frame_tab = st.tabs(["Video", "Frames"])

    with video_tab:
        if videos:
            selected_video = st.selectbox(
                "Video",
                videos,
                format_func=lambda video: video.name,
                key=f"video_{segment.name}",
            )
            st.video(str(selected_video))
        else:
            st.info("No MP4 preview found in the segment folder.")

    with frame_tab:
        if frames:
            frame_index = st.select_slider(
                "Frame",
                options=list(range(len(frames))),
                format_func=lambda index: frames[index].name,
                key=f"frame_{segment.name}",
            )

            selected_frame = frames[frame_index]

            st.image(
                str(selected_frame),
                caption=selected_frame.name,
                use_container_width=True,
            )
        else:
            st.info("No frames found.")

completed_indicators = set(
    annotations.loc[
        annotations["score"].str.strip() != "",
        "indicator",
    ]
)

completed_count = len(completed_indicators.intersection(INDICATORS))

st.sidebar.progress(completed_count / len(INDICATORS))
st.sidebar.caption(f"{completed_count} of {len(INDICATORS)} indicators scored")

with form_column:
    indicator = st.selectbox(
        "Indicator",
        list(INDICATORS),
        format_func=lambda code: (
            f"{'✅' if code in completed_indicators else '⬜'} "
            f"{code} — {INDICATORS[code][0]}"
        ),
        key=f"indicator_{segment.name}",
    )

    name, scores, instruction = INDICATORS[indicator]

    with st.expander("PDF criteria"):
        st.write(instruction)

        for value, description in scores.items():
            st.write(f"**{value}:** {description}")

    matching_rows = annotations["indicator"] == indicator

    saved = (
        annotations.loc[matching_rows].iloc[-1].to_dict() if matching_rows.any() else {}
    )

    score_options = [""] + [str(value) for value in scores]

    # S4 allows averaging the scores of both street sides.
    if indicator == "S4":
        score_options = [""] + [f"{value / 2:g}" for value in range(2, 11)]

    saved_score = saved.get("score", "")

    if saved_score:
        try:
            saved_score = f"{float(saved_score):g}"
        except ValueError:
            st.error("The saved score is not a valid number.")
            st.stop()

    if saved_score not in score_options:
        st.error("The saved score is invalid for this indicator.")
        st.stop()

    saved_evidence = [
        frame_name
        for frame_name in saved.get("evidence_frames", "").split(";")
        if frame_name in frame_names
    ]

    st.caption("The score applies to the entire segment.")

    with st.form(f"assessment_{segment.name}_{indicator}"):
        score = st.selectbox(
            "Score",
            score_options,
            index=score_options.index(saved_score),
            format_func=lambda value: format_score(value, scores),
        )

        justification = st.text_area(
            "Justification / limitations",
            value=saved.get("justification", ""),
            height=120,
        )

        evidence = st.multiselect(
            "Evidence frames",
            frame_names,
            default=saved_evidence,
        )

        submitted = st.form_submit_button(
            "Save assessment",
            type="primary",
        )

    if submitted:
        row = {
            "indicator": indicator,
            "score": score,
            "justification": justification,
            "evidence_frames": ";".join(evidence),
        }

        updated_annotations = pd.concat(
            [
                annotations.loc[~matching_rows],
                pd.DataFrame([row]),
            ],
            ignore_index=True,
        )

        temporary_path = csv_path.with_suffix(".tmp")

        try:
            updated_annotations.to_csv(temporary_path, index=False)
            temporary_path.replace(csv_path)
        except OSError as error:
            st.error(f"Could not save assessment: {error}")
        else:
            st.success("Assessment saved.")
