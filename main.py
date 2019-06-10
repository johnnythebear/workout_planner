from random import randint, choice

exercises = ['Push-ups', 'Bench Presses', 'Shoulder Presses', 'Dips',\
             'Squats', 'Lunges', 'Bridges', 'Deadlifts',\
             'Pull-Ups', 'Rows', 'Biceps Curls',\
             'Burpees', 'Plank Knee Raises']

for i in range(5):
    ranNum = randint(0, len(exercises)-1)
    selected = exercises[ranNum]
    exercises.pop(ranNum)
    sets = randint(2, 5)
    reps = choice([5, 6, 8, 10, 12, 15])
    print('{}. {} {}x{}'.format(i+1, selected, sets, reps))
