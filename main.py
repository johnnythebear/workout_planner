from random import randint, choice

class Lift:
    def __init__(self, name):
        self.name = name
        self.reps = [3, 4, 5, 6, 7, 8]

class Calis:
    def __init__(self, name):
        self.name = name
        self.reps = [5, 6, 8, 10, 12, 15]

class Static:
    def __init__(self, name):
        self.name = name
        self.reps = ['15s', '20s', '30s', '40s', '60s']

exercises = [Calis('Push-ups'), Lift('Bench Presses'), Lift('Shoulder Presses'), Calis('Dips'),\
             Lift('Squats'), Calis('Lunges'), Calis('Bridges'), Lift('Deadlifts'),\
             Calis('Pull-Ups'), Lift('Rows'), Calis('Biceps Curls'),\
             Calis('Burpees'), Static('Plank')]

for i in range(5):
    ranNum = randint(0, len(exercises)-1)
    selected = exercises[ranNum]
    exercises.pop(ranNum)
    sets = randint(2, 5)
    reps = choice(selected.reps)
    print('{}. {} {}x{}'.format(i+1, selected.name, sets, reps))
