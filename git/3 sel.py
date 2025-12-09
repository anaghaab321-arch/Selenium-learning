Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> randint(65,90)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    randint(65,90)
NameError: name 'randint' is not defined
>>> import random
>>> random(0,10)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    random(0,10)
TypeError: 'module' object is not callable. Did you mean: 'random.random(...)'?
>>> random.random(0,10)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    random.random(0,10)
TypeError: Random.random() takes no arguments (2 given)
>>> Random.random(0,10)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    Random.random(0,10)
NameError: name 'Random' is not defined. Did you mean: 'random'?
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', '_lgamma', '_log', '_log2', '_os', '_parse_args', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'main', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> random.Random()
<random.Random object at 0x000001B002D9CCB0>
>>> r.random(0,100)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    r.random(0,100)
NameError: name 'r' is not defined
import random as r
r.random()
0.8832625896296523
r.randint(10,100)
80
randint(65,90)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    randint(65,90)
NameError: name 'randint' is not defined
r.randint(65,90)
72
chr(r.randint(65,90))
'W'
chr(r.randint(65,90))
'M'
chr(r.randint(65,90))
'A'
