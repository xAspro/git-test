import numpy as np
import math

import leftRuleInt as l
import rightRuleInt as r
import midRuleInt as m

for i in range(1,6):
    print("n= ",pow(10,i))

    print("Left")
    print(l.iter(0,math.pi,np.sin,pow(10,i)))

    print("Right")
    print(r.iter(0,math.pi,np.sin,pow(10,i)))

    print("Mid")
    print(m.iter(0,math.pi,np.sin,pow(10,i)))
