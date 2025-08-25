import csv

input_filename = 'sf_buildings.csv'
output_filename = 'sf_buildings_processed.csv'

try:
    with open(input_filename, 'r') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)

        fieldnames = [field for field in reader.fieldnames if field != 'use']

        # 处理每一行数据
        processed_rows = []
        for row in rows:
            # 移除'use'列
            if 'use' in row:
                del row['use']
                pass

            # 转换高度从英尺到米 (1英尺 = 0.3048米)
            if 'height' in row:
                height_feet = float(row['height'].strip())
                height_meters = height_feet * 0.3048
                row['height'] = round(height_meters, 2)

            processed_rows.append(row)

    # 写入新的CSV文件
    with open(output_filename, 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(processed_rows)

    print(f"saved new file: {output_filename}")

except FileNotFoundError:
    print(f"Error: {output_filename} is not exist")
except Exception as e:
    print(f"Error: {str(e)}")
