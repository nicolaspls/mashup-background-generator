import json

# Function to generate colors.json
def generate_colors_json():
    segments = []
    
    print("Welcome to the colors.json generator!")
    print("You will be asked to input color segments (color, start, and duration). Type 'done' when finished.\n")
    
    while True:
        color = input("Enter color (or type 'done' to finish): ").strip().lower()
        if color == "done":
            break
        
        try:
            start = int(input(f"Enter start time for {color} (in ubiart units): ").strip())
            duration = int(input(f"Enter duration for {color} (in ubiart units): ").strip())
        except ValueError:
            print("Invalid input. Start time and duration must be integers. Try again.")
            continue

        # Create the segment dictionary
        segment = {
            "color": color,
            "start": start,
            "duration": duration
        }
        
        # Add the segment to the list
        segments.append(segment)
        print(f"Added segment: {segment}\n")
    
    # Save segments to colors.json
    with open("colors.json", "w") as json_file:
        json.dump(segments, json_file, indent=4)
    
    print(f"\ncolors.json has been successfully generated with {len(segments)} segments!")

# Run the generator
generate_colors_json()
