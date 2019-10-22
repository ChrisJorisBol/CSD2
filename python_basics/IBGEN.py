import simpleaudio as sa;
import time;
import random;
from midiutil import MIDIFile;

bpm = 0
maatsoort = 0
maten_input = 0
volume = 100;
event_list = [];
partial_list = [];
value = True



def setup():
    global kick
    global snare
    global hat
    global play_obj
    print (" ;; Welkom bij jouw persoonlijke beatgenerator! ;; ");
    print(" ;; ");
    print (" ;; Voordat er een beat gegenereerd"
    " kan worden heb ik wat informatie van je nodig ;; ")
    kick = sa.WaveObject.from_wave_file("samples/kickdrum.wav");
    snare = sa.WaveObject.from_wave_file("samples/snare.wav");
    hat = sa.WaveObject.from_wave_file("samples/hat.wav");
setup();


def bpm_input():
    global bpm;
    while value:
        try:
            print(" ;; ")
            print(" ;; Allereerst heb ik het gewenste bpm  nodig. ;; ")
            print(" ;; ")
            bpm = (int(input(" ;; Voer hier het getal in. ;; ")))
            zero_check = 1/bpm
        except ValueError:
            print(" ;; Verkeerde waarde, probeer het opnieuw. ;; ")
        except NameError:
            print(" ;; Dat is geen nummer, probeer het opnieuw. ;; ")
        except TypeError:
            print(" ;; Ik heb een heel getal nodig, probeer het opnieuw. ;; ")
        except ZeroDivisionError:
            print(" ;; Het getal mag geen 0 zijn, probeer het opnieuw. ;; ")
        else:
            print(" ;; Je gekozen bpm is:",bpm," ;; ")
            return bpm;
            value == False;



def maatsoort_input():
    value == True
    global maatsoortx;
    global maatsoorty;
    while value:
        try:
            print(" ;; ")
            print(" ;; Vervolgens heb ik je gewenste maatsoort nodig. ;; ")
            print(" ;; ")
            print(" ;; Elke maatsoort is mogelijk. Houdt alsjeblieft dit format aan. 4/4 ;; ")
            print(" ;; ")
            print(" ;; Eerst dit getal -> 4/4 ;; ")
            maatsoortx = int(input(" ;; "));
            zero_check = 1/maatsoortx
            print(" ;; Vervolgens dit getal 4/4 <- ;; ")
            maatsoorty = int(input(" ;; "));
            zero_check2 = 1/maatsoorty
        except ValueError:
            print(" ;; Verkeerde waarde, probeer het opnieuw. ;; ")
        except NameError:
            print(" ;; Dat is geen nummer, probeer het opnieuw. ;; ")
        except TypeError:
            print(" ;; Ik heb een heel getal nodig, probeer het opnieuw. ;; ")
        except ZeroDivisionError:
            print(" ;; Het getal mag geen 0 zijn, probeer het opnieuw. ;; ")
        else:
            print(" ;; Je gekozen maatsoort is.",maatsoortx,'/',maatsoorty," ;; ")
            print(" ;; ")
            return maatsoortx
            return maatsoorty
            value == False;


def maat_input():
    global maten_input;
    while value:
        try:
            print(" ;; ")
            print(" ;; Als laatste heb ik de gewenste hoeveelheid maten nodig. ;; ")
            print(" ;; ")
            maten_input = int(input(" ;; Voer hier de gewenste hoeveelheid in. ;; "))
            zero_check = 1/maten_input;
        except ValueError:
            print(" ;; Verkeerde waarde, probeer het opnieuw. ;; ")
        except NameError:
            print(" ;; Dat is geen nummer, probeer het opnieuw. ;; ")
        except TypeError:
            print(" ;; Ik heb een heel getal nodig, probeer het opnieuw. ;; ")
        except ZeroDivisionError:
            print(" ;; Het getal mag geen 0 zijn, probeer het opnieuw. ;; ")
        else:
            print(" ;; De gekozen hoeveelheid maten is",maten_input," ;; ")
            return maten_input
            value == False;


def user_interface():
    bpm_input();
    maatsoort_input();
    maat_input();
user_interface();

def event_grid():
    global beats_per_maat;
    global lengte_per_beat;
    global partial_grid;
    global grid;
    global grid_copy;
    global kwartnoot_lengte;
    global lengte;
    beats_per_maat = maatsoortx
    lengte_per_beat = maatsoorty
    partial_grid = int(beats_per_maat*maten_input)
    grid = list(range(1, partial_grid+1));
    grid_copy = grid.copy();
    kwartnoot_lengte = (60/bpm);
    lengte = kwartnoot_lengte*(4/lengte_per_beat)*1000;
event_grid();

def logic_algorythm():
    global event_list;
    global select_algorythm;
    global tellingx3;
    global full_list

    select_algorythm = 0
    full_list = [];
    grouping_2 = [1, 2];
    grouping_3 = [1, 2, 3];
    grouping_4 = [1, 2, 3 ,4];
    aantalx3 = int(beats_per_maat/3);
    tellingx3 = aantalx3 * 3;
    aantalx4 = int(beats_per_maat/4);
    twee_of_vier = beats_per_maat % 3;

    if beats_per_maat % 4 == 0:
        event_list = grouping_4 * aantalx4;
        #als de hoeveelheid beats per maat gedeeld door 4 kan worden;
        #volgt het deze logica;
    if beats_per_maat % 4 != 0:
        #als dat niet kan volgt de andere logica om een 'logische';
        #groepering te maken van groepjes van 2 en 3 of 3 en 4;
        if twee_of_vier == 0:
            event_list = grouping_3 * aantalx3;
            select_algorythm = 1
        if twee_of_vier == 1:
            aantalx3 -= 1;
            event_list = grouping_3 * aantalx3 + grouping_4;
            select_algorythm = 2
        if twee_of_vier == 2:
            event_list = grouping_3 * aantalx3 + grouping_2;
            select_algorythm = 3
    full_list = event_list * maten_input
logic_algorythm();



def event_algorythm():
    global partial_list;
    global list_list
    partial_list = [];
    list_list = [];
    probability_snare = 80;
    count = 0;
    iteratie_veiligheid = 0
    timestamp = 0
    for n in full_list:
        temporary_variable = 0;
        iteratie_veiligheid = 0
        if select_algorythm == 0:

            if len(grid_copy) > 0:
                timestamp = grid_copy.pop(0)
            iteratie_veiligheid = 0
            partial_list.append(timestamp)
            if n == 1 or n == 3:
                partial_list.append(kick);
            if n == 2:
                partial_list.append(snare);
            if n == 4:
                partial_list.append(snare);
            partial_list.append(hat);
            list_list.append(partial_list);
            partial_list = [];

        if select_algorythm == 1:

            if len(grid_copy) > 0:
                timestamp = grid_copy.pop(0)
            partial_list.append(timestamp)
            chance_snare = random.randint(1, 100);
            if n == 1:
                partial_list.append(kick);
            if n == 2 and chance_snare < probability_snare:
                partial_list.append(snare);
                temporary_variable = 1;
            if n ==  3 and temporary_variable != 1:
                partial_list.append(snare);
            partial_list.append(hat);
            list_list.append(partial_list);
            partial_list = [];

        if select_algorythm == 2:

            if len(grid_copy) > 0:
                timestamp = grid_copy.pop(0)
            chance_snare = random.randint(1,100);
            if count < 1:
                partial_list.append(timestamp)
                if n == 1:
                    partial_list.append(kick);
                if n == 3:
                    partial_list.append(snare);
                    count += 1;
                    iteratie_veiligheid = 1
                partial_list.append(hat);
                list_list.append(partial_list);
                partial_list = [];

            if count == 1 and iteratie_veiligheid != 1:

                partial_list.append(timestamp)
                if n == 1:
                    partial_list.append(kick);
                if n == 2 and chance_snare < probability_snare:
                    partial_list.append(snare);
                    temporary_variable = 1;
                if n == 4 and temporary_variable != 1:
                    partial_list.append(snare);
                if n == 4:
                    count = 0;
                partial_list.append(hat);
                list_list.append(partial_list);
                partial_list = [];

        if select_algorythm == 3:

            if len(grid_copy) > 0:
                timestamp = grid_copy.pop(0)
            if count < 1:
                partial_list.append(timestamp)
                if n == 1:
                    partial_list.append(kick);
                if n == 3:
                    partial_list.append(snare);
                    count += 1;
                    iteratie_veiligheid = 1
                partial_list.append(hat);
                list_list.append(partial_list);
                partial_list = [];

            if count == 1 and iteratie_veiligheid != 1:
                partial_list.append(timestamp)
                if n == 1:
                    partial_list.append(kick);
                if n == 2:
                    partial_list.append(snare);
                    count = 0
                partial_list.append(hat);
                list_list.append(partial_list);
                partial_list = [];
event_algorythm()

MyMIDI = MIDIFile(3);
MyMIDI.addTempo(0, 0, bpm);
track1    = 0; #Kick
channel  = 10;
volume   = 100; #127 is het luidst
volume = 100;
duration = lengte_per_beat * 0.25;
time_extra = lengte_per_beat * 0.25;
timeZero=time.time()*1000;  #Geeft de start van de timer aan

def audio_play():
    payload = list_list.pop(0); #Payload is een timestamp met bijbehorende events
    ts = payload.pop(0);
    while True:
        sample1 = 0
        sample2 = 0
        now = time.time()*1000;
        if now-timeZero >= ts*lengte:   #Als de tijd nu - de tijd dat we begonnen zijn
                                        #Later is dan de timestamp * de nootlengte moet de event afspelen.
            if payload:
                event = payload.pop(0)
                sample1 = event.play();
                if event == kick:
                     MyMIDI.addNote(track1, channel, 60, ((ts-1)/time_extra), duration, 100);
                if event == snare:
                     MyMIDI.addNote(track1, channel, 61, ((ts-1)/time_extra), duration, 100);
                if event == hat:
                     MyMIDI.addNote(track1, channel, 60, ((ts-1)/time_extra), duration, 100);

                if len(payload) > 0:
                    event = payload.pop(0)
                    sample2 = event.play();
                    if event == kick:
                         MyMIDI.addNote(track1, channel, 60, ((ts-1)/time_extra), duration, 100);
                    if event == snare:
                         MyMIDI.addNote(track1, channel, 61, ((ts-1)/time_extra), duration, 100);
                    if event == hat:
                         MyMIDI.addNote(track1, channel, 62, ((ts-1)/time_extra), duration, 100);

            if list_list:
                payload = list_list.pop(0);
                ts = payload.pop(0);
            if not list_list:
                if not payload:
                    sample1.wait_done();    #zonder wait_done speelt de laatste sample niet af
                    sample2.wait_done();
                    break;
        else:
            time.sleep(0.001);
audio_play();

def ama():
    global opnieuw
    print(" ;; ")
    print (" ;; Je gegenereerde beat is klaar! ;; ")
    print(" ;; ")
    print(" ;; Was hij naar wens? Dan kan hij direct opgeslagen worden als MIDI bestand. ;; ")
    print (" ;; Voer een Y of N in om te laten weten of je hem wilt opslaan. ;; ")
    save_midi = input(" ;; [Y/N] ;; ")

    if save_midi.lower() == 'y':
        print (" ;; De MIDI file word opgeslagen in dezelfde Map als deze python file. ;; ")
        print(" ;; Bedankt voor het gebruiken van je persoonlijke beatgenerator. ;; ")
        with open("De_Beat.mid", 'wb') as output_file:
            MyMIDI.writeFile(output_file);
            exit();
    if save_midi.lower() == 'n':
        print(" ;; Zou je het opnieuw willen proberen? ;; ")
        opnieuw = input(" ;; [Y/N] ;; ")

ama();

def recursive():
    if opnieuw.lower() == 'y':
        print(" ;; Wederom heb ik wat informatie van je nodig. ;; ")
        user_interface();
        event_grid();
        logic_algorythm();
        event_algorythm();
        audio_play();
        ama();
        recursive();
    if opnieuw.lower() == 'n':
        print(" ;; Bedankt voor het gebruiken van je persoonlijke beatgenerator. ;; ")
        exit();
recursive();
