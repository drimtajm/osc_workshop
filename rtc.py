#!/usr/bin/python
# -*- coding: utf-8 -*-
import smbus
import time

address = 0x68
register = 0x00
bus = smbus.SMBus(1)

def read_time():
        return bus.read_i2c_block_data(address,register,7);

def convert_from_bcd(bcd):
    """Convert a bcd value to a decimal value

    :param value: The value to unpack from bcd
    :returns: The number in decimal form
    """
    place, decimal = 1, 0
    while bcd > 0:
        nibble = bcd & 0xF
        decimal += nibble * place
        bcd >>= 4
        place *= 10
    return decimal

rtc_time = read_time()
seconds = convert_from_bcd(rtc_time[0])
minutes = convert_from_bcd(rtc_time[1])
hours = convert_from_bcd(rtc_time[2])
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
print(time.localtime())
