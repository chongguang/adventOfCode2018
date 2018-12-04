import datetime
import operator
import numpy

with open("inputday4.txt") as f:
    content = f.readlines()

actions = [x.strip() for x in content]

class Action:
    def __init__(self, action_string):
        time_and_action = action_string.split('] ')
        time = time_and_action[0].split('[')[1]
        action = time_and_action[1]
        self.time = time
        self.datetime = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M')
        self.action = action


actions = [Action(s) for s in actions]

actions.sort(key=operator.attrgetter('datetime'))


guard_iter = 0
current_id = ""
sleep_map = {}
total_time = {}
minutes = numpy.zeros(60)

while guard_iter < len(actions):
    if actions[guard_iter].action.startswith('Guard'):
        current_id = actions[guard_iter].action.split(' ')[1]
        if current_id not in sleep_map:
            sleep_map[current_id] = numpy.zeros(60)
        if current_id not in total_time:
            total_time[current_id] = 0
        guard_iter = guard_iter + 1
    else:
        start = int(actions[guard_iter].time.split(':')[1])
        end = int(actions[guard_iter + 1].time.split(':')[1])
        total_time[current_id] = total_time[current_id] + (end - start)
        for i in range(start, end):
            sleep_map[current_id][i] = sleep_map[current_id][i] + 1
        for i in range(start, end):
            minutes[i] = minutes[i] + 1
        guard_iter = guard_iter + 2

print(total_time)

#print(sleep_map['#401'])

print(minutes)

# #31 => 170

for key, value in sleep_map.items():
    print(key)
    print(value[31])




