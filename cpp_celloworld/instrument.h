// class.h
#include <string>
#include <iostream>
class Instrument
{
public:
    Instrument(std::string sound);
    std::string sound;
    void play();
    void roll(int x);
};
