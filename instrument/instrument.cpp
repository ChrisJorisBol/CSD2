#include "instrument.h"
using namespace std;

Instrument::Instrument(std::string sound)
{
    this->sound = sound;
}

void Instrument::play()
{
    cout << "play: " << this->sound << endl;
}

void Instrument::roll(int x)
{
    while(x>0)
    {
        play();
        --x;
    }
}
