#include <stdio.h>
#include <math.h>
#include "OpenSimplex2S.h"

#define RADIUS 0.6
//#define RESOLUTION (180 * 60 * 60 / 200.0)
#define RESOLUTION 1080
#define MAXELEV 65536

#define OFFSET 1.0
#define LACUNARITY 2.0
#define GAIN 2.0
#define H 1.0
#define OCTAVES 8

OpenSimplexEnv *ose;
OpenSimplexGradients *osg;

double noiseSpherical(OpenSimplexEnv *env, OpenSimplexGradients *grad, double az, double alt, double r) {
	double theta = (90.0 - alt) * M_PI / 180.0;
	double phi = (az + 180.0) * M_PI / 180.0;
	return noise3_Classic(env, grad, r * sin(theta) * cos(phi), r * sin(theta) * sin(phi), r * cos(theta));
}

double elevation(double longitude, double latitude) {
	double signal = 0.0;

	double radius = RADIUS;
	signal = OFFSET - fabs(noiseSpherical(ose, osg, longitude, latitude, radius));
	signal *= signal;

	double result = signal;
	double weight = 1.0;
	double frequency = 1.0;

	for(int i = 1; i < OCTAVES; i++) {
		radius *= LACUNARITY;
		weight = signal * GAIN;
		if (weight > 1.0) weight = 1.0;
		if (weight < 0.0) weight = 0.0;
		signal = OFFSET - fabs(noiseSpherical(ose, osg, longitude, latitude, radius));
		signal *= signal;
		signal *= weight;
		result += signal * pow(frequency, -(H));
		frequency *= LACUNARITY;
	}
	return result;
}

int main(int argc, char **argv)
{
	ose = initOpenSimplex();
	osg = newOpenSimplexGradients(ose, 1337);
	printf("P2\n%d %d\n%d\n", (int)RESOLUTION * 2, (int)RESOLUTION, (int)MAXELEV - 1);
	for (int i = 0; i < RESOLUTION; i++) {
		for (int j = 0; j < RESOLUTION * 2; j++) {
			double latitude = (i / (double)RESOLUTION) * 180.0 - 90.0;
			double longitude = (j / (double)(RESOLUTION * 2.0)) * 360.0 - 180.0;
			printf("%d ", (int)(MAXELEV * elevation(longitude, latitude) / 2.0));
		}
		printf("\n");
	}
	return 0;
}

