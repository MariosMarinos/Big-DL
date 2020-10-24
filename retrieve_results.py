import os
import re
current_dir = "./test/"
times = []
acc = []
for file in os.listdir(current_dir):
    if file.endswith('.out'):
        with open(os.path.join(current_dir, file)) as open_file:
            lines = open_file.readlines()
            size_of_file = len(lines)
            line = lines[size_of_file - 3].strip()
            time = re.search('Wall Clock (.+?)s]', line)
            accuracy = re.search('accuracy: (0.[0-9]*)', line)
            if hasattr(time, 'group') and hasattr(accuracy, 'group'):
                times.append(time.group(1))
                acc.append(accuracy.group(1))
sum = 0
for i in range(len(times)):
    print(float(times[i])/((float(acc[i])*100)**2))
