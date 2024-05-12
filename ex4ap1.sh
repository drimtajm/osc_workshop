#!/bin/bash
/sbin/ip link set can0 type can bitrate 125000 loopback on
ifconfig can0 up
