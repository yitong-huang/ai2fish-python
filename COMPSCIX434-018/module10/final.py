import csv
import matplotlib.pyplot as plt
from datetime import datetime

def load_data(filename):
    """
    read f1 winner data from csv
    """
    data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # clean empty data
            if not all([row['date'], row['winner_name'], row['team'], row['year']]):
                continue
            # revert data
            try:
                row['year'] = int(row['year'])
                row['laps'] = float(row['laps']) if row['laps'] else 0
                row['winner_name'] = " ".join(row['winner_name'].split())
                row['date'] = datetime.strptime(row['date'], '%Y-%m-%d').date()
                row['time'] = datetime.strptime(row['time'], '%H:%M:%S').time()
            except ValueError:
                continue

            data.append(row)
    return data


def get_descriptive_stats(data):
    years = [row['year'] for row in data]
    min_year = min(years)
    max_year = max(years)
    total_races = len(data)

    return {
        'year_range': (min_year, max_year),
        'total_races': total_races,
    }


def get_top_circuits(data, n=5):
    """
    获取比赛次数最多的前n个赛道
    """
    circuit_counts = {}

    for row in data:
        circuit = row['circuit']
        circuit_counts[circuit] = circuit_counts.get(circuit, 0) + 1

    # 按比赛次数排序并返回前n个
    sorted_circuits = sorted(circuit_counts.items(), key=lambda x: x[1], reverse=True)
    return [circuit[0] for circuit in sorted_circuits[:n]]


def get_circuit_time_data(data, circuit_names):
    """
    获取指定赛道的年份和时间数据
    """
    circuit_data = {}

    for circuit in circuit_names:
        circuit_data[circuit] = {'years': [], 'times': []}

        for row in data:
            if row['circuit'] == circuit:
                circuit_data[circuit]['years'].append(row['year'])
                circuit_data[circuit]['times'].append(row['time'])

    return circuit_data


def plot_circuit_times(circuit_data):
    """
    绘制赛道时间变化折线图
    """
    plt.figure(figsize=(14, 8))

    # 为每个赛道创建折线图
    for circuit, data in circuit_data.items():
        if len(data['years']) > 1:
            # 将秒转换为小时:分钟格式用于y轴
            times_hours = [t.hour * 3600 + t.minute * 60 + t.second for t in data['times']]

            # 绘制折线图
            plt.plot(data['years'], times_hours, label=circuit)

    plt.title('F1 Race Times by Circuit Over Years', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Race Time (Second)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    plt.savefig('f1_circuit_times.png', dpi=300, bbox_inches='tight')
    plt.close()


def main():
    data = load_data('winners_f1_1950_2025_v2.csv')

    stats = get_descriptive_stats(data)
    print("=== DESCRIPTIVE STATISTICS ===")
    print(f"Year range: {stats['year_range'][0]} - {stats['year_range'][1]}")
    print(f"Total races: {stats['total_races']}")

    top_circuits = get_top_circuits(data, 5)
    circuit_data = get_circuit_time_data(data, top_circuits)
    plot_circuit_times(circuit_data)


main()
