// inheritance.h
#pragma once
#include <iostream>
#include <string>
class Instrument
{
public:
    Instrument(std::string sound);
    std::string sound;
	std::string timbre;
    void play();
	void setRange(std::string pitch_range);
	void setTimbre(std::string timbre);
	std::string pitch_range;
    // void pitch(int y);
};






// class Strings: public Instrument
// {
// public:
//     Strings();
// };
//
// class Percussion: public Instrument
// {
// public:
//     Percussion();
// };
