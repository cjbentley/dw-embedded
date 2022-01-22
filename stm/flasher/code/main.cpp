#include "mbed.h"

static BufferedSerial pc(USBTX, USBRX);

int main()
{
    char in;
    char tmp;
    char out[9];
    while (1) {
        pc.read(&in, 1);
        if (in = 10) { // End of line marker
            for (int i = 0; i < 9; i++) {
                pc.read(&tmp, 1);
                out[i] = tmp;
            }
            out[9] = 10;
            pc.write(&out, 10);
        }
    }
}