import smbus # imports the System Management Bus library (manage commns between master and slave)
import time 
 
DEVICE     = 0x23 # default address for the Device, found on the BH1750 datasheet
POWER_DOWN = 0x00 # reserved address for 'no active state'
POWER_ON   = 0x01 # reserved address for 'power on'
RESET      = 0x07 # reserved address to 'reset'

# This address is taken from the BH1750 datasheet and is used by 
# the master to tell the slave what resolution to measure. This 
# corresponds to 1lux resolution for 120ms, followed by a power 
# down (Opcode)
ONE_TIME_HIGH_RES_MODE = 0x20
 
bus = smbus.SMBus(1) # create a new bus object

# convert the data bits into a number
def convertToNumber(data):
  return ((data[1] + (256 * data[0])) / 1.2)

# read the data coming back from the slave by passing in the resolution opcode
def readLight(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE) 
  return convertToNumber(data)
 
# main loop constantly taking readings
def main():
 
  while True:
    print("Light Level : " + str(readLight()) + " lux")
    time.sleep(0.5)
 
# general safeguard to prevent invoking the script unless intended
if __name__=="__main__":
   main()