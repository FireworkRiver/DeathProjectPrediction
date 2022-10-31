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
y_balance_dead=[]
x_balance_dead=[]
y_balance_alive=[]
x_balance_alive=[]

for i in range(len(commit_list)):
    if commit_list[i][2]=="dead":
        y_list[i]='1'
        y_balance_dead.append(y_list[i])
        x_balance_dead.append(issues_list[i])
    else:
        y_balance_alive.append(y_list[i])
        x_balance_alive.append(issues_list[i])

temp = list(zip(issues_list,y_list))
random.shuffle(temp)
x_random,y_random = zip(*temp)

x_random_train = x_random[:7000]
y_random_train = y_random[:7000]

with open('x_random_train.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for row in x_random_train:
        writer.writerow(row)
with open('y_random_train.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for row in y_random_train:
        writer.writerow(row)

x_random_test = x_random[7000:]
y_random_test = y_random[7000:]

with open('x_random_test.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for row in x_random_test:
        writer.writerow(row)
with open('y_random_test.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for row in y_random_test:
        writer.writerow(row)

temp = list(zip(x_balance_dead,y_balance_dead))
random.shuffle(temp)
x_balance_dead_random,y_balance_dead_random = zip(*temp)

temp = list(zip(x_balance_alive,y_balance_alive))
random.shuffle(temp)
x_balance_alive_random,y_balance_alive_random = zip(*temp)

x_balance_train = x_balance_alive_random[:2000]+x_balance_dead_random[:2000]
y_balance_train = y_balance_alive_random[:2000]+y_balance_dead_random[:2000]

temp = list(zip(x_balance_train,y_balance_train))
random.shuffle(temp)
x_balance_train_random,y_balance_train_random = zip(*temp)

with open('x_balance_train.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for row in x_balance_train_random:
        writer.writerow(row)
with open('y_balance_train.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for row in y_balance_train_random:
        writer.writerow(row)

x_balance_test = x_balance_alive_random[2000:]+x_balance_dead_random[2000:]
y_balance_test = y_balance_alive_random[2000:]+y_balance_dead_random[2000:]

temp = list(zip(x_balance_test,y_balance_test))
random.shuffle(temp)
x_balance_test_random,y_balance_test_random = zip(*temp)

with open('x_balance_test.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for row in x_balance_test_random:
        writer.writerow(row)
with open('y_balance_test.csv', 'w',newline='') as f:
    print("writing..")
    writer = csv.writer(f)
    for row in y_balance_test_random:
        writer.writerow(row)


