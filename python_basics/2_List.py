import time
import pygame.midi as pgmidi
import random

device=7 # default device
velocity=100
drumChannel=9

bassdrum=35
snare=38
closedhihat=42
openhihat=46
tom=[]
tom.append(50)
tom.append(48)
tom.append(47)
tom.append(45)
tom.append(40)
tom.append(41)
tom.append(42) # stiekem toch hihat
tom.append(43)

qNote=500

def init():
  pgmidi.init()


def showMidiDevices():
    n=pgmidi.get_count()
    for i in range(n):
        print(pgmidi.get_device_info(i))


def setDevice(d):
  global device
  device=d


def test():
  pgmidi.Output(device).note_on(60,100,0)
  time.sleep(0.5)
  pgmidi.Output(device).note_off(60,100,0)


def drumloop():
  sequence=[]
  sequence.append((0,bassdrum))
  sequence.append((2*qNote,bassdrum))
  sequence.append((4*qNote,bassdrum))
  sequence.append((6*qNote,bassdrum))

  sequence.append((qNote,snare))
  sequence.append((3*qNote,snare))
  sequence.append((5*qNote,snare))
  sequence.append((7*qNote,snare))

  """ double hihat
  for i in range(16):
    sequence.append((0.5*i*qNote,closedhihat))
  """

  sequence.append((8*qNote,0)) # dummy event indicates end of bar

  """ Go Animal Go
  for i in range(12):
    sequence.append((qNote*8 + i*qNote/3,tom[random.randint(0,len(tom)-1)]))

  sequence.append((8*qNote+12*qNote/3,0)) # dummy event indicates end of bar
  """

while True:
    seq=list(sequence) # create copy of sequence
    seq.sort(reverse=True)
    event=seq.pop()
    timeZero=time.time()*1000
    print("Loop start")

    while True:
            now=time.time()*1000
            if now-timeZero > event[0]:
    	            print(event[1])
            if event[1] > 0:
    	            pgmidi.Output(device).note_on(event[1],velocity,drumChannel)
            if seq: # if events left in queue
                    event=seq.pop()
            else:
              break # if no events left, break from this loop
    else:
	         time.sleep(0.01) # if time for event hasn't come, wait
