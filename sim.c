/* sim.c */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <math.h>
#include <CL/cl.h>



double perlin(int seed, double x, double y, double z, double w);

int main(int argc, char** argv) {

    double zoom = 1.0; // noise zoom
    double res = 1.0; // degree of arc
    int seed = 0xdeadbeef;
    int detail = 8;
    double sea_level = 0.0;
    double land_curve = 1.0;
    double water_curve = 1.0;

    /*
    char opt;
    while ((opt = getopt(argc, argv, "s")) != -1) {
        switch (opt) {
            case 's':
                break;
            default:
            fprintf(stderr, "Invalid argument!\n");
            exit(-1);
        }
    }
    */

    return 0;
}


double perlin(int seed, double x, double y, double z, double w) {

    return 0.0;
}
