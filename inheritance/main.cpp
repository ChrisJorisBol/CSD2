// main.cpp
#include "inheritance.h"
#include "winds.h"
#include "keys.h"
#include <iostream>
#include <string>

using namespace std;

int main()
{
	// Instrument key("");

	Keys piano("geluid");
	// Instrument tromp("Sound2");
	Winds trumpet("asdf");
    piano.setRange("8 Octaves");
	piano.setTimbre("Warm");
	piano.play();

	trumpet.setRange("2.5 Octaven");
	trumpet.setTimbre("Schel");
	trumpet.play();

    return 0;
};
