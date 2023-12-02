#you will have to manually add pulse_fg and bg_scroll by yourself

import json

def generate_tape_reference_clip(start_time, duration_time, input_color):
    return [
        {
            "__class": "TapeReferenceClip",
            "Id": 144604702,
            "TrackId": 3554742381,
            "IsActive": 1,
            "StartTime": start_time,
            "Duration": duration_time,
            "Path": f"world/maps/_mashup/cinematics/color_{input_color}.tape",
            "Loop": 0
        },
        {
            "__class": "TapeReferenceClip",
            "Id": 144604702,
            "TrackId": 3554742381,
            "IsActive": 1,
            "StartTime": start_time,
            "Duration": duration_time,
            "Path": f"world/maps/_mashup/cinematics/color_{input_color}_duo.tape",
            "Loop": 0
        },
        {
            "__class": "TapeReferenceClip",
            "Id": 144604702,
            "TrackId": 3554742381,
            "IsActive": 1,
            "StartTime": start_time,
            "Duration": duration_time,
            "Path": f"world/maps/_mashup/cinematics/uv_right.tape",
            "Loop": 0
        }
    ]

def main():
    clips = []

    while True:
        start_time = input("Enter startTime (ubiart units): ")
        duration_time = input("Enter durationTime (ubiart units): ")
        input_color = input("Enter color: ")

        stacked_clips = generate_tape_reference_clip(start_time, duration_time, input_color)
        clips.extend(stacked_clips)

        continue_input = input("Continue? (Y/N): ").lower()
        if continue_input != 'y':
            break

    map_name = input("Enter MapName: ")

    tape_data = {
        "__class": "Tape",
        "Clips": clips,
        "ActorPaths": [
            "..|_mashup_main_scene|_MashUp_GRAPH|TXComponent_8x_Left",
            "..|_mashup_main_scene|_MashUp_GRAPH|TXComponent_8x_Right",
            "..|_mashup_main_scene|_MashUp_GRAPH|TXComponent_8x_Top",
            "..|_mashup_main_scene|_MashUp_GRAPH|TXComponent_8x_Bottom"
        ],
        "TapeClock": 0,
        "TapeBarCount": 1,
        "FreeResourcesAfterPlay": 0,
        "MapName": map_name
    }

    with open(f"{map_name}_mainsquence.tape.ckd", 'w') as file:
        json.dump(tape_data, file, indent=4)

if __name__ == "__main__":
    main()
