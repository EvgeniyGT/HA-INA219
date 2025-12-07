#from smbus2 import SMBus
#import time
#
#I2C_BUS = 1
#ADDRESS = 0x41
#
## Регистр Bus Voltage
#REG_BUS_VOLTAGE = 0x02
#REG_CURRENT = 0x04
#REG_POWER = 0x03
#
#def read_word(bus, reg):
#    data = bus.read_i2c_block_data(ADDRESS, reg, 2)
#    return (data[0] << 8) | data[1]

#while True:
#    try:
#        print("Hello!!!")
#        with SMBus(I2C_BUS) as bus:
#            bus_voltage_raw = read_word(bus, REG_BUS_VOLTAGE)
#            bus_voltage = (bus_voltage_raw >> 3) * 0.004
#
#            power_raw = read_word(bus, REG_POWER)
#            current_raw = read_word(bus, REG_CURRENT)
#
#            print("Load Voltage: {:.3f} V".format(bus_voltage))
#            print("Current RAW: {}".format(current_raw))
#            print("Power RAW: {}".format(power_raw))
#            print("-----")
#
#    except Exception as e:
#        print("Error:", e)
#
#    time.sleep(2)

print("Hello!!!")
