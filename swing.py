#!/usr/bin/env python
# #coding=utf-8

# brew install portaudio

import math

anchorFrequency = 440
octaveFrequency = 2 * anchorFrequency

ratio = pow(2, 1.0/12)
equalTemperament = [pow(ratio,x) for x in range(12)]
print equalTemperament

'''
[1.0, 1.0594630943592953, 1.122462048309373, 1.1892071150027212, 
1.2599210498948734, 1.3348398541700346, 1.4142135623730954, 
1.498307076876682, 1.5874010519682, 1.6817928305074297, 
1.7817974362806794, 1.887748625363388]
'''

print "-----------------"

fiveTones = [2/3.0] 
for i in range(7):
    currentRatio = fiveTones[i]
    nextRatio =  currentRatio * 3 / 2.0
    if nextRatio > 2:
        nextRatio = nextRatio / 2.0
    fiveTones.append(nextRatio)

fiveTones.sort()
print fiveTones

'''
[0.6666666666666666, 1.0, 1.125, 1.265625, 1.423828125,
 1.5, 1.6875, 1.8984375]
'''