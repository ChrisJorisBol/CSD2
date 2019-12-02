// inheritance.cpp
#include "inheritance.h"
#include <iostream>
#include <string>
using namespace std;

Instrument::Instrument(string sound)
{
    this->sound = sound;
	cout << "Constructor - Instrument";
}

Keys::Keys(string timbre) : Instrument(sound)
{
    this->sound = "pling";
	cout << "Constructor - Keys";
    cout << "\nThis sounds like = " << timbre << "\n";
}

// void Keys::setSound(string sound)
// {
// 	this->sound = timbre;
// }

// string Keys::getSound()
// {
// 	return sound;
// 	cout << "\n" << timbre ;
// }
//
void Instrument::play()
{
    cout << "play: " << sound << endl;
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
