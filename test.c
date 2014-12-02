#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ADDR_0 25
#define ADDR_1 24
#define ADDR_2 23
#define ADDR_3 18
#define D_G 17
#define D_R 22
#define CLK 10
#define WE   9
#define ALE 11

int main(void) {
    int i;
    int j;
    int chk0, chk1, chk2, chk3;
    char line[100];
    char s[100];
    long long int data_ag[32];
    long long int data_ar[32];
    long long int n=0;
    for (i=0; i<32 ; i++){
            fgets(s, 50,stdin);
            sscanf(s,"%llx",&n);
            data_ag[i] = n;
            data_ar[i] = 0;
    }

    unsigned long long int  data_g,data_r;

    if(wiringPiSetupGpio() == -1) return 1;

    pinMode(ADDR_0, OUTPUT);
    pinMode(ADDR_1, OUTPUT);
    pinMode(ADDR_2, OUTPUT);
    pinMode(ADDR_3, OUTPUT);
    pinMode(D_G,OUTPUT);
    pinMode(D_R,OUTPUT);
    pinMode(CLK,OUTPUT);
    pinMode(WE,OUTPUT);
    pinMode(ALE,OUTPUT);

    for(j=0; j<16; j++){
        data_g = (data_ag[j] << 32) + data_ag[j+16];
        data_r = (data_ar[j] << 32) + data_ar[j+16];
        for(i=0; i<64; i++){
            if (data_g >> i & 1){
                digitalWrite(D_G, 1);
            }else{
	        digitalWrite(D_G, 0);
            }
            if (data_r >> i & 1){
                digitalWrite(D_R, 1);
            }else{
	        digitalWrite(D_R, 0);
            }
	    digitalWrite(CLK, 1);
	    digitalWrite(CLK, 0);
        }
        chk0 = j & 1;
        chk1 = (j >>1) & 1;
        chk2 = (j >>2) & 1;
        chk3 = (j >>3) & 1;
        digitalWrite(ALE, 1);
        if (chk0 == 1){
            digitalWrite(ADDR_0, 1);
        }else{
            digitalWrite(ADDR_0, 0);
        }
        if (chk1 == 1){
            digitalWrite(ADDR_1, 1);
        }else{
            digitalWrite(ADDR_1, 0);
        }
        if (chk2 == 1){
            digitalWrite(ADDR_2, 1);
        }else{
            digitalWrite(ADDR_2, 0);
        }
        if (chk3 == 1){
            digitalWrite(ADDR_3, 1);
        }else{
            digitalWrite(ADDR_3, 0);
        }
        digitalWrite(WE, 1);
        digitalWrite(WE, 0);
        digitalWrite(ALE, 0);
    }
    return 0;
}
