#ifndef MOTOR_H
#define MOTOR_H
#include "mbed.h"
#include <string>
#include <vector>
#include <cmath>



namespace motor {
    static DigitalOut dir_left(PB_15);
    static PwmOut pwm_left(PB_14);
    static DigitalOut dir_right(PB_6);
    static PwmOut pwm_right(PA_7);

    // void dcode(char msg [9]){

    //     int speed_l=((atoi(msg[2])*100)+(atoi(msg[3])*10)+(atoi(msg[4])));
    //     float fspeed_l=speed_l/100.0;
    //     int speed_r=((atoi(msg[6])*100)+(atoi(msg[7])*10)+(atoi(msg[8])));
    //     float fspeed_r=speed_r/100.0;

    //     if (msg[1]=='F'){
    //         int dir_l=1; //forward-- left
    //     }
    //     else if(msg[1]=='R'){
    //         int dir_l=0;
    //     }
    //     else if (msg[5]=='F'){
    //         int dir_r=1;
    //     }
    //     else if(msg[5]=='R'){
    //         int dir_r=0;
    //     }


    //     set_speed(fspeed_l,dir_l,fspeed_r,dir_r);



    // }


    void set_speed(float fspeed_l, int dir_l, float fspeed_r, int dir_r) {
        
        pwm_left.period(0.0001);
        pwm_left.write(fspeed_l);
        pwm_right.period(0.0001);
        pwm_right.write(fspeed_r);

        dir_left=1;
        dir_right=1;
        

    }




}
#endif
