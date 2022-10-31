import csv
import random

commit_address = "./rep_commit.csv"
commit_reader = csv.reader(open(commit_address))
commit_list = [row for row in commit_reader]
print(len(commit_list))

issues_address = "./repo_issues.csv"
issues_reader = csv.reader(open(issues_address))
issues_list = [row for row in issues_reader]
print(len(issues_list))

y_list =  ['0' for i in range(len(commit_list))]

for i in range(len(commit_list)):
    if commit_list[i][2]=="dead":
        y_list[i]='1'

temp = list(zip(issues_list,y_list))
random.shuffle(temp)
x_random,y_random = zip(*temp)

x_balance2_test = x_random[7000:]
y_balance2_test = y_random[7000:]

with open('x_balance2_test.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for row in x_balance2_test:
        writer.writerow(row)
with open('y_balance2_test.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for row in y_balance2_test:
        writer.writerow(row)

x_balance2 = x_random[:7000]
y_balance2 = y_random[:7000]

y_balance2_dead=[]
x_balance2_dead=[]
y_balance2_alive=[]
x_balance2_alive=[]
for i in range(len(y_balance2)):
    if y_balance2[i] == '1':
        y_balance2_dead.append(y_balance2[i])
        x_balance2_dead.append(x_balance2[i])
    else:
        y_balance2_alive.append(y_balance2[i])
        x_balance2_alive.append(x_balance2[i])

temp = list(zip(x_balance2_dead,y_balance2_dead))
random.shuffle(temp)
x_balance_dead_random,y_balance_dead_random = zip(*temp)

temp = list(zip(x_balance2_alive,y_balance2_alive))
random.shuffle(temp)
x_balance_alive_random,y_balance_alive_random = zip(*temp)

min_num = min(len(y_balance2_dead),len(y_balance2_alive))

x_balance2_train = x_balance_dead_random[:min_num]+x_balance_alive_random[:min_num]
y_balance2_train = y_balance_dead_random[:min_num]+y_balance_alive_random[:min_num]

temp = list(zip(x_balance2_train,y_balance2_train))
random.shuffle(temp)
x_balance2_train_random,y_balance2_train_random = zip(*temp)

with open('x_balance2_train.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for row in x_balance2_train_random:
        writer.writerow(row)
with open('y_balance2_train.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for row in y_balance2_train_random:
        writer.writerow(row)
