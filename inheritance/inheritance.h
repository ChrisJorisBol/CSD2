// inheritance.h
#include <iostream>
#include <string>
class Instrument
{
public:
    Instrument(std::string sound);
    std::string sound;
    int y;
    void play();
    // void pitch(int y);
};



class Keys: public Instrument
{
public:
    Keys(std::string timbre);
	std::string timbre;
	void setSound(std::string sound);
	std::string getSound();
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
