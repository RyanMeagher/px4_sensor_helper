#!/usr/local/bin/python3
import sys

def make_driver_dict(fin):
    driver_lst=[]
    with open(fin, "r") as f:
        for line in f:
            if (line[0]=="#"):
                driver_name = line.split("_DEVTYPE_")[1].split("0x")[0].replace("\t","").replace(" ","")
                driver_type = line.split("_")[1]
                drive_code = "0x"+ line.split("0x")[-1].replace("\n", "")

                driver_lst.append([driver_name, driver_type, drive_code])
    driver_dict={x[2]:x[0:2] for x in driver_lst}
    return driver_dict

def findDriver(number,driver_dict):
    bus_interface=["unknown","I2C","SPI","UAVCAN"]
    binary_num = bin(number)
    bin_str = str(binary_num).replace("0b","")
    padding = "0"*(24-len(bin_str))

    padded_str=padding+bin_str

    devtype, address, bus, bus_type =  padded_str[0:8], padded_str[8:16], \
                                       padded_str[16:21], padded_str[21:] 

    sens_lst =[devtype, address, bus, bus_type ]
    bin_sens_lst=["0b"+x for x in sens_lst]
    int_sens_lst=[int(x,2) for x in bin_sens_lst]

    d_key=str(hex(int_sens_lst[0]))
    print( "=============================================")
    print(f"Device name:  {driver_dict[d_key][0]} ")
    print(f"Device type:  {driver_dict[d_key][1]} ")
    print(f"Device bus :  {int_sens_lst[2]}       ") 
    print(f"Interface  :  {bus_interface[int_sens_lst[3]]}")
    print(" ")


driver_dict=make_driver_dict("sensors.txt")

if (len(sys.argv)==1):
    print("[ERROR] add sensor argument")
    
else:
    for sensor_num in sys.argv[1:]:
        findDriver(int(sensor_num), driver_dict)



