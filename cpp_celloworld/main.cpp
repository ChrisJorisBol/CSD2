#include "instrument.h"

int main()
{
    Instrument in1("mmmm");
    Instrument in2("fwwaap");

    in1.play();
    in2.play();

    in1.roll(15);
    return 0;
}
