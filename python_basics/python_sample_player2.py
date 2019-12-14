import simpleaudio as sa;
import time;
import random;
from midiutil import MIDIFile;
#laad de sample, kan ook met een input()
kick = sa.WaveObject.from_wave_file("samples/kickdrum.wav");
snare = sa.WaveObject.from_wave_file("samples/snare.wav");
hat = sa.WaveObject.from_wave_file("samples/hat.wav");

print("Welkom bij jouw persoonlijke beatgenerator!");

bpm = int(input("Voer hier het tempo in van je beat. "));
ms = input("Kies hier je maatsoort van de beat. Format n n  ");
bars_input = int(input("Hoeveel maten zou je willen genereren? "));
# snares_input = input("Willen we meer of minder snares? [meer/minder] ");
swing = (int(input("Hoeveel Swing zou je willen? [0-100] "))) / 100 / 2;
#.split() deelt de ingevoerde maatsoort in een lijst en scheid deze bij de spatie
mz = (ms.split(" "));

#hoeveelheid beats per maat
beats_per_maat = int(mz[0]);

#Lengte van de noten
lengte_per_beat = int(mz[1]);

# bars = (lengte_per_beat) * bars_input
full_slices = beats_per_maat * bars_input
slices = list(range(1, full_slices+1));


# Kwartnoot = 0.5s bij 120bpm
kn = (60/bpm);
lengte = kn*(4/lengte_per_beat);

snare_plaats = 2
# if snares_input == 'meer':
#     si = 2;
# elif snares_input == 'minder':
#     si = 1;
# if beats_per_maat > 7:
#     snare_plaats = 4/si;
# elif beats_per_maat > 15:
#     snare_plaats = 8/si;

# print(snare_plaats)
sampleplaying_kick = 0;
sampleplaying_snare = 0;
sampleplaying_hat = 0;
snarecount = 0;
kickcount = 0;
value = 0; #hoeveelste beat
volume = 100;
list = [];

list2 = [];


timeZero=time.time()*1000;

ts = slices.pop(0);

# while True:
#     now = time.time()*1000;
#     if now-timeZero >= ts*lengte:
#         ts.play();
#         if slices:
#             ts = slices.pop();
#         else:
#             break;
#     else:
#         time.sleep(0.001);

for i in slices:
    # print(i)
    snarecount = 0;
    kickcount = 1;

    #List om de midi mee te genereren
    partial_list = [];
    value += 1;
    partial_list.append(value);

    if i == 1:
        # kick.play();
        partial_list.append('kick');
        # time.sleep(lengte/2 + (lengte*swing));
        # sampleplaying_kick = 1

    if (i % beats_per_maat) % snare_plaats == 0:
        if (random.randint(1, 100)/100) < 0.8:
            # snare.play();
            # snarecount += 1
            partial_list.append('snare');

        # time.sleep(lengte/2 + (lengte*swing));

    if i % beats_per_maat == 0 or i % 3 == 0:
        if (i % beats_per_maat) % snare_plaats != 0 and (random.randint(1, 100)/100) < 0.8:
            # sampleplaying_kick = 1
            # kick.play();
            partial_list.append('kick');
            # time.sleep(lengte/2 + (lengte*swing));
            # kickcount += 1
    # hat.play();
    # partial_list.append(hat);
    # time.sleep(lengte/2 - (lengte*swing));
    list2.append(partial_list);


print(time.time());
print(timeZero);
print(list2);


for n in list2:
    print(n[0]);
    now = time.time()*1000;
    print(now)
    print(lengte)
    if now - timeZero <= n[0] * lengte:
        print(n[0]);
        n[1].play();
    else:
        time.sleep(0.001);





# print(list2);
#3 tracks voor 3 samples
MyMIDI = MIDIFile(3);
MyMIDI.addTempo(0, 0, bpm);
track1    = 0; #Kick
track2    = 0; #Snare
track3    = 0; #Hat
channel  = 0;
volume   = 100; #127 is het luidst
volume = 100;
duration = 0.5;
time_extra = lengte_per_beat * 0.25;

#Schrijven van de midi-noten op de juiste events
for i in list2:
    if i[1] == kick:
        MyMIDI.addNote(track1, channel, 60, ((i[0]-1)/time_extra), duration, 100);
        # print('kick');
    if i[1] == hat:
        # print('hat')
        volume = random.randint(70,100);
        MyMIDI.addNote(track3, channel, 64, ((i[0]-1)/time_extra) + swing, duration, volume);
    if len(i) == 3:
        if i[2] == hat:
            # print('hat');
            volume = random.randint(70,100);
            MyMIDI.addNote(track3, channel, 64, ((i[0]-1)/time_extra) + swing, duration, volume);
        if i[2] == snare:
            # print('snare')
            MyMIDI.addNote(track2, channel, 67, ((i[0]-1)/time_extra), duration, 100);

    if i[1] == snare:
        # print('snare');
        MyMIDI.addNote(track2, channel, 67, ((i[0]-1)/time_extra), duration, 100);

#Creeren van de .Midi file
with open("mymidifile.mid", 'wb') as output_file:
    MyMIDI.writeFile(output_file);
