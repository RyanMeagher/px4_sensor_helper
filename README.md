# px4_sensor_helper


This is a helper script for the px4_module `sensors status` that is called from the mavlink console in qgroundcontrol. Here is some 
  
This will show you Device Name, Device Type, Bus#, and interface type. You just need to put one of the numbers found when you call
`sensors status` 


requires python version >=3.6 since fstring is used

To run code use:


`python3 driver_decode.py <sensor#>`

for multiple sensors  
`python3 driver_decode.py <sensor#1> <sensor#2> <sensor#n>`
  
If you add drivers simply copy and paste the `PX4-Autopilot/src/drivers/drv_sensor.h` file into `sensors.txt`. 
Any additional drivers that you add should be in the format `#define DRV_<devType>_DEVTYPE_<devName> 0x<device_address>`
