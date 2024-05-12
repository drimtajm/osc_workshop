#!/bin/bash
./ec
/sbin/ip link set can0 type can bitrate 500000 loopback off
ifconfig can0 up
