nb_player = 452
last_marble = 70784

scores = [0] * (nb_player + 1)

circle = [0]
current_p = 0
current_marble = 1





def max_score(times):

    nb_player = 452
    last_marble = 70784 * times

    scores = [0] * (nb_player + 1)

    circle = [0]
    current_p = 0
    current_marble = 1

    def insertion_position():
        next_one = current_p + 1
        if next_one >= len(circle):
            next_one = next_one - len(circle)
        return next_one + 1

    def pop_position():
        previous_seven = current_p - 7
        if previous_seven < 0:
            previous_seven = len(circle) + previous_seven
        return previous_seven


    for i in range(1, last_marble + 1):
        if i % 23 != 0:
            ip = insertion_position()
            circle.insert(ip, i)
            current_p = ip
        else:
            current_player = i % nb_player
            if current_player == 0:
                current_player = nb_player
            scores[current_player] = scores[current_player] + i
            pp = pop_position()
            remove_elem = circle.pop(pp)
            scores[current_player] = scores[current_player] + remove_elem
            current_p = pp

    print(max(scores))

max_score(1)


from collections import deque, defaultdict

def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0

print(play_game(452, 70784 * 100))