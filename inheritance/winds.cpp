//winds.cpp
#include "winds.h"
#include <iostream>
#include <string>
using namespace std;

Winds::Winds(string sound) : Instrument(sound)
{
	// this->sound = timbre;
	cout << "\nConstructor - Winds\n";
	// cout << "\nThis sounds like = " << timbre << "\n";
};
