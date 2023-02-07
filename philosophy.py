import threading
import random
import time

philosopher_list = []

class Philosopher(threading.Thread):
    running = True

    def __init__(self, index, leftfork, rightfork, thinkingmax):
        threading.Thread.__init__(self)
        self.index = index
        self.leftfork = leftfork
        self.rightfork = rightfork
        self.thinkingmax = thinkingmax
        self.timethinking = []
        self.timehungry = []
        self.timeeating = []
        self.truetime = time.time()

    def run(self):
        # This dude is THINKING
        while(self.running):
            print('Philosopher %s is thinking' % self.index)
            start = time.time() - self.truetime
            time.sleep(self.thinkingmax*random.random())
            print('Philosopher %s is now hungry' % self.index)
            end = time.time() - self.truetime
            thinking = (start, (end-start))
            self.timethinking.append(thinking)
            self.eat()

    def eat(self):
        fork1, fork2 = self.leftfork, self.rightfork
        start = time.time() - self.truetime
        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print('Philosopher %s swaps forks' % self.index)
            fork1, fork2 = fork2, fork1 
        else:
            return
        end = time.time() - self.truetime
        hungry = (start, (end-start))
        self.timehungry.append(hungry)   
        self.munching()
        fork2.release()
        fork1.release()    

        self.munching()

    def munching(self):
        print('Philosopher %s starts eating' % self.index)
        start = time.time() - self.truetime
        time.sleep(10)
        print('Philosopher %s is done eating and starts to think' % self.index)
        end = time.time() - self.truetime
        eating = (start, (end-start))
        self.timeeating.append(eating)             


def main(runtime):
    forks = [threading.Semaphore() for n in range (5)]
    philosophers= [Philosopher(i, forks[i%5], forks[(i+1)%5], 10)
            for i in range(5)]
    
    for p in philosophers:
        p.start()
    time.sleep(runtime)  
    Philosopher.running = False
    for p in philosophers:
        philosopher_list.append(p)

    print('Simulation done. Here are some stats')



    
if __name__== "__main__":
        main()
