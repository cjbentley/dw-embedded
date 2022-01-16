#ifndef WHEEL_H
#define WHEEL_H
#include "mbed.h"
#include <ratio>
#include <string>
#include <vector>
#include <cmath>

#ifndef M_PI
#define M_PI 3.1415
#endif


namespace wheel
{

    PwmOut pwm_left(PB_7);
    DigitalOut dir_left(PA_13);

    PwmOut pwm_right(PA_4);
    DigitalOut dir_right(PC_14);


void set(){
    dir_left=0; //set MCU direction pin 0 is frwrd

    pwm_left.period(0.0001f);      // PWM period
    pwm_left.write(0.95);

    dir_right=1; //set MCU direction pin

    pwm_right.period(0.0001f);      // PWM period
    pwm_right.write(0.95);
}

}
#endif
