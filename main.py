#you will have to manually add pulse_fg and bg_scroll by yourself

import json
import random

# Function to load the segments from colors.json
def load_segments_from_json(file_path):
    with open(file_path, "r") as file:
        segments = json.load(file)
    return segments

def generate_tape_reference_clips(map_name, segments):
    clips = []
    use_uv_left = True  # This will help alternate between UV left and UV right
    
    for segment in segments:
        color = segment["color"]
        start = segment["start"]
        duration = segment["duration"]
        
        # First clip for the color
        clip1 = {
            "__class": "TapeReferenceClip",
            "Id": random.randint(100000000, 999999999),  # Generate a random 9-digit Id
            "TrackId": random.randint(1000000000, 9999999999),  # Generate a random 10-digit TrackId
            "IsActive": 1,
            "StartTime": start,
            "Duration": duration,
            "Path": f"world/maps/{map_name.lower()}/cinematics/tapereferences/color_{color}.tape",
            "Loop": 0
        }
        
        # Second clip for the color (duo)
        clip2 = {
            "__class": "TapeReferenceClip",
            "Id": random.randint(100000000, 999999999),
            "TrackId": random.randint(1000000000, 9999999999),
            "IsActive": 1,
            "StartTime": start,
            "Duration": duration,
            "Path": f"world/maps/{map_name.lower()}/cinematics/tapereferences/color_{color}_duo.tape",
            "Loop": 0
        }

        # UV left or right clip (alternating based on use_uv_left)
        uv_clip = {
            "__class": "TapeReferenceClip",
            "Id": random.randint(100000000, 999999999),
            "TrackId": random.randint(1000000000, 9999999999),
            "IsActive": 1,
            "StartTime": start,
            "Duration": duration,
            "Path": f"world/maps/{map_name.lower()}/cinematics/tapereferences/uv_{'left' if use_uv_left else 'right'}.tape",
            "Loop": 0
        }
        
        # Append the color clips
        clips.append(clip1)
        clips.append(clip2)
        
        # Append the alternating UV clip
        clips.append(uv_clip)
        
        # Toggle the UV position for the next segment
        use_uv_left = not use_uv_left
    
    tape_data = {
        "__class": "Tape",
        "Clips": clips,
        "TapeClock": 0,
        "TapeBarCount": 1,
        "FreeResourcesAfterPlay": 0,
        "MapName": map_name
    }
    
    return tape_data

# Load the segments from colors.json
segments = load_segments_from_json("colors.json")

# Generate tape clips with the mapname below
map_name = "HeyMamaMU"
tape_data = generate_tape_reference_clips(map_name, segments)

# Convert to JSON string and print
tape_json = json.dumps(tape_data, indent=4)
print(tape_json)

# write to a file
with open(f"{map_name.lower()}_mainsequence.tape.ckd", "w") as f:
    f.write(tape_json)
