import json
from datetime import datetime

gmat_op = '/folder/ReportFileData.txt'
json_output = '/folder/trajectory.json'

trajectory_data = []

with open(gmat_op, 'r') as gmat_file:
    #reset file pointer
    gmat_file.seek(0) 
    # Skip the headers
    next(gmat_file)
    
    for line in gmat_file:
        values = line.split()

        date_time_str = f'{values[2]} {values[1]} {values[0]} {values[3]}'
        date_time = datetime.strptime(date_time_str, '%Y %b %d %H:%M:%S.%f')

        x_position = float(values[4])
        y_position = float(values[5])
        z_position = float(values[6])
        #print(x_position, y_position,z_position)

        '''time_step = {
            "UTCGregorian": date_time.strftime('%Y %b %d %H:%M:%S.%f'),
            "EarthMJ2000Eq": {
                "X": x_position,
                "Y": y_position,
                "Z": z_position
            }
        }'''

        time_step = {
                "Date": date_time.strftime('%d %b %Y'),
                "Time": date_time.strftime('%H:%M:%S.%f')[:-3],  # Remove the last 3 characters (milliseconds)
                "X": x_position,
                "Y": y_position,
                "Z": z_position
        }

        trajectory_data.append(time_step)

json_data = {
    "trajectory" :trajectory_data
}

with open(json_output, 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print(f'Trajectory data has been successfully converted to {json_output}')
