// inheritance.cpp
#include "inheritance.h"
#include <iostream>
#include <string>
using namespace std;

Instrument::Instrument(string sound)
{
    this->sound = sound;
	cout << "\nConstructor - Instrument\n";
};

void Instrument::setRange(string pitch_range)
{
	this->pitch_range = pitch_range;
	cout << "\nPitch range is\n" << pitch_range;
	// return pitch_range;
};

void Instrument::setTimbre(string timbre)
{
	this->timbre = timbre;
	cout << "\nTimbre is\n" << timbre << "\n";
};

void Instrument::play()
{
	    cout << "playing piano\n" << sound << endl;
};


// void Instrument::pitch(int y)
// {
//     this->y = y;
// }



// Strings::Strings()
// {
//     this->sound = "nnmmMMMeh"
//     cout << "\nThis sound = " << sound << "\n";
// }
//
// Percussion::Percussion()
// {
//     this->sound = "Boom".
//     cout << "\nThis sound = " << sound << "\n";
// }
