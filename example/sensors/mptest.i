 /* mptest.i */
 %module mptest
 %{
 /* Put header files here or function declarations like below */
  extern void AccelerometerStart(void);
  extern void AccelerometerStop(void);
  extern char * AccelerometerReadData(void);
  extern void MagnaticSensorStart(void);
  extern void MagnaticSensorStop(void);
  extern char * MagnaticSensorReadData(void);
  extern void LightSensorStart(void);
  extern void LightSensorStop(void);
  extern char * LightSensorReadData(void);
 %}
 
  extern void AccelerometerStart(void);
  extern void AccelerometerStop(void);
  extern char * AccelerometerReadData(void);
  extern void MagnaticSensorStart(void);
  extern void MagnaticSensorStop(void);
  extern char * MagnaticSensorReadData(void);
  extern void LightSensorStart(void);
  extern  void LightSensorStop(void);
  extern char * LightSensorReadData(void);
