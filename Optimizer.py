import os
import re
import subprocess
lr = 0.0005
prev_lr = 0.001
high_constant = 10000000
cost = high_constant
prev_cost = high_constant

for i in range(20):
    if cost <= prev_cost:
        prev_lr = lr
        lr = lr * 2
    else:
        lr = prev_lr * 1.1

    print("----------Using learning_rate of: " + str(lr))


    current_dir = "./"
    file = 'conf.json'
    with open(os.path.join(current_dir, file), 'r') as open_file:
            content = open_file.read()
            new_content = re.sub('"learningRate": "(0.[0-9]*)"','"learningRate": "' + str(lr) + '"' , content, flags=re.M)

    with open(os.path.join(current_dir, file), 'w') as open_file:
            open_file.write(new_content)

    process = subprocess.Popen('./sparkgen -r -d -c conf.json', shell=True, stdout=subprocess.PIPE)
    process.wait()

    current_dir = "./test"
    times = []
    acc = []
    for file in os.listdir(current_dir):
        if file.endswith('.out'):
           with open(os.path.join(current_dir, file)) as open_file:
                    lines = open_file.readlines()
                    size_of_file = len(lines)
                    line = lines[size_of_file-3].strip()
                    time = re.search('Wall Clock (.+?)s]', line)
                    accuracy = re.search('accuracy: (0.[0-9]*)', line)
                    if hasattr(time, 'group') and hasattr(accuracy, 'group'):
                        times.append(time.group(1))
                        acc.append(accuracy.group(1))

    sum = 0
    acc_sum = 0
    time_sum = 0
    for i, entry in enumerate(acc):
        acc_sum += float(entry)
        time_sum += float(times[i])
        sum += float(times[i]) / float(entry) ** 2

    avg_acc = acc_sum / len(acc)
    avg_time = time_sum / len(times)

    prev_cost = cost
    cost = sum / len(acc)
    print("------------------------------------Cost of using learning_rate of " + str(lr) + " is: " + str(
        cost) + "------------------------------------")
    print("avg acc: " + str(avg_acc) + ", avg time: " + str(avg_time))
    with open("optimization_results.txt", "a") as myfile:
        myfile.write(str(lr) + "," + str(cost) + "," + str(avg_acc) + "," + str(avg_time) + "\n");