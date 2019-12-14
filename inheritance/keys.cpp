//keys.cpp
#include "keys.h"
#include <iostream>
#include <string>
using namespace std;

Keys::Keys(string sound) : Instrument(sound)
{
	cout << "\nConstructor - Keys\n";
    // cout << "\nThis sounds like = " << timbre << "\n";
};
