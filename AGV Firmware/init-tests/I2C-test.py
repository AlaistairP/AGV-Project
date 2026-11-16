# I2C-test.py
# barry.mcmullin@dcu.ie


from machine import I2C
from machine import Pin

print("\nStarting...")

i2c = I2C(0, scl=Pin("I2C_SCL"), sda=Pin("I2C_SDA"))

#i2c = I2C(1, scl=Pin(15), sda=Pin(14)) # Internal I2C bus (IMU!)

print(i2c.scan())
i2c_addrs = i2c.scan()
for addr in i2c_addrs :
  print(addr, hex(addr))

print("Done!")
