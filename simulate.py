import matplotlib.pyplot as plt
import philosophy
import matplotlib.patches as mpatch

philosophy.main(300)
philosophers = philosophy.philosopher_list

fig, gnt = plt.subplots()

gnt.set_ylim(0, 60)
gnt.set_xlim(0, 315)

gnt.set_xlabel('Seconds since simulation start')
gnt.set_ylabel('Philosophers')

gnt.set_yticks([15, 25, 35, 45, 55])
gnt.set_yticklabels(['Phil 0', 'Phil 1', 'Phil 2', 'Phil 3', 'Phil 4'])

gnt.grid(True)

fakegreenbar = mpatch.Rectangle((0, 0), 1, 1, fc ='tab:green')
fakeredbar = mpatch.Rectangle((0, 0), 1, 1, fc='tab:red')
fakebluebar = mpatch.Rectangle((0, 0), 1, 1, fc='tab:blue')

gnt.legend([fakegreenbar, fakeredbar, fakebluebar], ['Thinking', 'Hungry', 'Eating'])

def philGraph(philosopher, y):
    gnt.broken_barh(philosopher.timethinking, (y, 6), facecolors=('tab:green'))

    gnt.broken_barh(philosopher.timehungry, (y, 6), facecolors=('tab:red'))

    gnt.broken_barh(philosopher.timeeating, (y, 6), facecolors=('tab:blue'))

for i in range(len(philosophers)):
    philGraph(philosophers[i], (i+1)*10)

plt.savefig("diningphilosophers_graph.png")