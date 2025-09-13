import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


input_filename = 'winners_f1_1950_2025_v2.csv'

try:
    with open(input_filename, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        for row in rows:
            row['year'] = int(row['year'])
            row['laps'] = float(row['laps'])
            row['date'] = datetime.strptime(row['date'], '%Y-%m-%d').date()
            row['winner_name'] = row['winner_name'].replace(u'\xa0', ' ')
            try:
                row['time'] = datetime.strptime(row['time'], '%H:%M:%S').time()
            except ValueError:
                row['time'] = datetime.strptime(row['time'], '%M:%S').time()
except FileNotFoundError:
    print(f"Error: {input_filename} is not exist")
except Exception as e:
    print(f"Error: {str(e)}")


def static_occurrence(data, column):
    occurrence = {}
    for r in data:
        if r[column] not in occurrence:
            occurrence[r[column]] = 1
        else:
            occurrence[r[column]] += 1
    occurrence_list = sorted(occurrence.items(), key=lambda x: x[1], reverse=True)
    print(occurrence_list)
    return occurrence_list


def plot_occurrence(occurrence_list, fig_name, top_n=8):
    plt.figure(figsize=(20, 8))
    x = []
    y = []
    occurrence_list = occurrence_list[:top_n]
    for occurrence in occurrence_list:
        x.append(occurrence[0])
        y.append(occurrence[1])
    plt.bar(x, y)
    plt.savefig(fig_name)
    plt.show()
    plt.close()


team_occurrence = static_occurrence(rows, 'team')
plot_occurrence(team_occurrence, 'team_occurrence.png')
winner_occurrence = static_occurrence(rows, 'winner_name')
plot_occurrence(winner_occurrence, 'winner_occurrence.png', 8)


max_laps = 0
for row in rows:
    if row['laps'] > max_laps:
        max_laps = row['laps']
print(f"max laps is {max_laps}")


sum_time = timedelta(hours=0, minutes=0, seconds=0)
for row in rows:
    sum_time += timedelta(hours=row['time'].hour, minutes=row['time'].minute, seconds=row['time'].second)
mean_time = sum_time / len(rows)
hours = mean_time.seconds // 3600
minutes = mean_time.seconds % 3600 // 60
seconds = mean_time.seconds % 60
print(f"total mean time is {hours:02d}:{minutes:02d}:{seconds:02d}")


# mean 'time' group by 'circuit'
circuit_time = {}
for row in rows:
    if row['circuit'] not in circuit_time:
        circuit_time[row['circuit']] = (timedelta(hours=row['time'].hour, minutes=row['time'].minute, seconds=row['time'].second), 1)
    else:
        circuit_time[row['circuit']] = (circuit_time[row['circuit']][0] + timedelta(hours=row['time'].hour, minutes=row['time'].minute, seconds=row['time'].second),
                                        circuit_time[row['circuit']][1] + 1)

for circuit in circuit_time.keys():
    circuit_mean_time = circuit_time[circuit][0] / circuit_time[circuit][1]
    hours = circuit_mean_time.seconds // 3600
    minutes = circuit_mean_time.seconds % 3600 // 60
    seconds = circuit_mean_time.seconds % 60
    print(f"{circuit} mean time is {hours:02d}:{minutes:02d}:{seconds:02d}")


# count 'team' group by 'circuit'
circuit_team = {}
for row in rows:
    if row['circuit'] not in circuit_team:
        circuit_team[row['circuit']] = {}
    if row['team'] not in circuit_team[row['circuit']]:
        circuit_team[row['circuit']][row['team']] = 1
    else:
        circuit_team[row['circuit']][row['team']] += 1

for circuit in circuit_team.keys():
    print(f"{circuit}: ")
    for team in circuit_team[circuit].keys():
        print(f"\t{team}: {circuit_team[circuit][team]}")

l = []
l.index()