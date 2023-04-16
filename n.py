import json

def convert_mmss_to_hhmmss(duration):
    if ':' not in duration:
        raise ValueError("Invalid duration format. Expected format: 'mm:ss' or 'hh:mm:ss'")

    parts = duration.split(':')
    if len(parts) == 2:
        # duration is in mm:ss format
        minutes, seconds = int(parts[0]), int(parts[1])
        if minutes < 60:
            # duration is less than 1 hour
            return f"{minutes}:{seconds:02d}"
        else:
            # duration is 1 hour or more
            hours = minutes // 60
            minutes = minutes % 60
            return f"{hours:01d}:{minutes:02d}:{seconds:02d}"
    elif len(parts) == 3:
        # duration is in hh:mm:ss format
        hours, minutes, seconds = int(parts[0]), int(parts[1]), int(parts[2])
        if hours == 0:
            # remove leading 0 from hours field
            return f"{minutes}:{seconds:02d}"
        else:
            return f"{hours:01d}:{minutes:02d}:{seconds:02d}"
    else:
        raise ValueError("Invalid duration format. Expected format: 'mm:ss' or 'hh:mm:ss'")

try:
    with open('call.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = []
except json.decoder.JSONDecodeError:
    print("Error: Invalid JSON format in the file.")
    data = []

while True:
    time = input("Enter the time (hh:mm:ss AM/PM): ")
    internet_speed = input("Enter the internet speed (in Mbps): ")
    call_duration = input("Enter the call duration (hh:mm:ss or mm:ss): ")
    mobile_charge = input("Enter the mobile charge (in %): ")

    try:
        call_duration = convert_mmss_to_hhmmss(call_duration)
    except ValueError as e:
        print(e)
        continue

    call_data = {
        "time": time,
        "Internet_speed": internet_speed,
        "call_duration": call_duration,
        "mobile_charge": mobile_charge
    }

    data.append(call_data)

    choice = input("Do you want to add more data? (y/n): ")
    if choice.lower() == 'n':
        break

with open('call.json', 'w') as f:
    json.dump(data, f)

print("Data saved successfully.")
