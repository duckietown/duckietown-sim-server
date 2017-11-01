#!/bin/bash

rostopic pub /cmd_vel geometry_msgs/Twist "linear:
  x: -1.00
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0 "

