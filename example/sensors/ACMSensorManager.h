#ifndef __ACCMAGLIGHTSENSOR_H__
#define __ACCMAGLIGHTSENSOR_H__

#include "common.h"

_BEGIN_EXTERN_C


#define ACM_SIMPLE_EXPORT

#ifdef ACM_SIMPLE_EXPORT

//
// Accelerometer
//
void AccelerometerStart(void);
void AccelerometerStop(void);
char * AccelerometerReadData(void);


// 
// Magnatic sensor
//
void MagnaticSensorStart(void);
void MagnaticSensorStop(void);
char * MagnaticSensorReadData(void);


//
// Light sensor
//
void LightSensorStart(void);
void LightSensorStop(void);
char * LightSensorReadData(void);


#else

void AccelerometerInit(void);
void AccelerometerDeinit(void);
void AccelerometerEnable(void);
void AccelerometerDisable(void);
char * AccelerometerReadData(void);


// 
// Magnatic sensor
//
void MagnaticSensorInit(void);
void MagnaticSensorDeinit(void);
void MagnaticSensorEnable(void);
void MagnaticSensorDisable(void);
char * MagnaticSensorReadData(void);


//
// Light sensor
//
void LightSensorInit(void);
void LightSensorDeinit(void);
void LightSensorEnable(void);
void LightSensorDisable(void);
char * LightSensorReadData(void);

#endif

_END_EXTERN_C


#endif	/* __ACCMAGLIGHTSENSOR_H__ */
