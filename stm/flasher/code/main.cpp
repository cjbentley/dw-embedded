#include "mbed.h"
#include "motor.h"

static BufferedSerial pc(USBTX, USBRX);

int main()
{
    int speed_l;
    float fspeed_l;
    int speed_r;
    float fspeed_r;
    int dir_l;
    int dir_r;

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



            speed_l=((atoi(&out[2])*100)+(atoi(&out[3])*10)+(atoi(&out[4])));
            fspeed_l=speed_l/100.0;
            speed_r=((atoi(&out[6])*100)+(atoi(&out[7])*10)+(atoi(&out[8])));
            fspeed_r=speed_r/100.0;

            if (out[1]=='F'){
                int dir_l=1; //forward-- left
            }
            else if(out[1]=='R'){
                int dir_l=-1;
            }
            else if (out[5]=='F'){
                int dir_r=1;
            }
            else if(out[5]=='R'){
                int dir_r=-1;
            }

            motor::set_speed(fspeed_l,dir_l,fspeed_r,dir_r);

        }
    }            
               
    
}