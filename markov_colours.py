import random

class Markov(object):

    def __init__(self, counter = 1, c = 0, p = 0, d = 0):
        self.counter = counter
        self.c = c
        self.p = p
        self.d = d
            
    def yellow(self, counter, c, p, d):
        randnum = random.randint(1, 100)
        if counter <= 500:
            if randnum <= 15:
                counter += 1
                d += 1
                self.red(counter, c, p, d)
            elif randnum >= 41:
                counter += 1
                c += 1
                self.yellow(counter, c, p, d)
            else:
                counter += 1
                p += 1
                self.green(counter, c, p, d)
        else:
            print ('The breakdown is:', c, 'for yellow,', p, 'for green,', 'and', d, 'for red.')
           
    def green(self, counter, c, p, d):
        randnum = random.randint(1, 100)
        if counter <= 500:
            if randnum <= 25:
                counter += 1
                d += 1
                self.red(counter, c, p, d)
            elif randnum >= 51:
                counter += 1
                p += 1
                self.green(counter, c, p, d)
            else:
                counter += 1
                c += 1
                self.yellow(counter, c, p, d)
        else:
            print ('The breakdown is:', c, 'for yellow,', p, 'for green,', 'and', d, 'for red.')
 
    def red(self, counter, c, p, d):
        randnum = random.randint(1, 100)
        if counter <= 500:
            if randnum <= 33:
                counter += 1
                c += 1
                self.yellow(counter, c, p, d)
            elif randnum >= 67:
                counter += 1
                d += 1
                self.red(counter, c, p, d)
            else:
                counter += 1
                p += 1
                self.green(counter, c, p, d)
        else:
            print ('The breakdown is:', c, 'for yellow,', p, 'for green,', 'and', d, 'for red.')

if __name__ == '__main__':
    markov = Markov()
    print ('Each sample size is 500.')
    
    for i in range(10):
        markov.yellow(markov.counter, markov.c, markov.p, markov.d)
