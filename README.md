# px4_sensor_helper


This is a helper script for the px4_module `sensors status` that is called from the mavlink console in qgroundcontrol. Here is some 
[documentation](https://www.example.com). 
  
This will show you Device Name, Device Type, Bus#, and interface type. You just need to put one of the numbers found when you call
`sensors status` 


To run code use:


  `python3 driver_decode.py <sensor#>`
  
If you add drivers simply copy and paste the `PX4-Autopilot/src/drivers/drv_sensor.h` file into `sensors.txt`. Any additional drivers that you add should be in the format `#define DRV_<devType>_DEVTYPE_<devName> 0x<device_address>`
