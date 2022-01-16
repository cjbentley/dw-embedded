#include "mbed.h"

static BufferedSerial pc(USBTX, USBRX);

int main()
{
    char msg[] = "Echoes back to the screen anything you type\n";
    char buff[10];
    pc.write(msg, sizeof(msg));
    while (1) {
        pc.read(&buff, 10);
        pc.write(&buff, 10);
    }
}