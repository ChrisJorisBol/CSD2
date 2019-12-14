//oscillator.cpp
#include <iostream>
#include "oscillator.hpp"
using namespace std;

Oscillator::Oscillator(float freq)
{
    this->freq = freq;
    cout << "\n Oscillator - Constructor\n";
}

Oscillator::~Oscillator()
{
    cout << "\nOscillator Deconstructor\n";
}

void Oscillator::setFreq(float freq)
{
    cout << "\nOscillator - setFreq\n";
    if(freq < 0 || freq > 22050)
    {
        cout << "\nError - Unable to set the frequency value with value: "
            << freq << "\n";
        return;
    }
    this->freq = freq;
}

float Oscillator::getFreq()
{
    return freq;
}
