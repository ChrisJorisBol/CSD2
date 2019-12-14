//oscillator.hpp
#include <iostream>


class Oscillator
{
    //public, private, protected
public:
    Oscillator(float freq);
    ~Oscillator();
    void setFreq(float freq);
    float getFreq();
private:
    float freq;
};
