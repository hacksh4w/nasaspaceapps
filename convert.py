import json
from datetime import datetime

# Replace this with the actual path to your GMAT output file
input_gmat_file = '/Users/mrina/Desktop/ReportFileData.txt'
output_json_file = '/Users/mrina/Desktop/trajectory.json'

trajectory_data = []

with open(input_gmat_file, 'r') as gmat_file:
    # Skip the header
    next(gmat_file)
    
    for line in gmat_file:
        values = line.split()

        date_time_str = f'{values[2]} {values[1]} {values[0]} {values[3]}'
        date_time = datetime.strptime(date_time_str, '%Y %b %d %H:%M:%S.%f')

        x_position = float(values[4])
        y_position = float(values[5])
        z_position = float(values[6])
        #print(x_position, y_position,z_position)

        time_step = {
            "UTCGregorian": date_time.strftime('%Y %b %d %H:%M:%S.%f'),
            "EarthMJ2000Eq": {
                "X": x_position,
                "Y": y_position,
                "Z": z_position
            }
        }

        trajectory_data.append(time_step)

json_data = {
    "trajectory": trajectory_data
}

with open(output_json_file, 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print(f'Trajectory data has been successfully converted to {output_json_file}')
