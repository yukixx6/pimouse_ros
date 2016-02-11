#!/bin/bash -xve

#repuired packages
pip install catkin_pkg
pip install empy
pip install pyyaml
pip install rospkg

#ros install 
cd ..
git clone http://github.com/ryuichiueda/ros_setup_scripts_Ubuntu14.04_server.gitcd ./ros_setup_scripts_Ubuntu14.04_server
bash ./step0.bash
bash ./step1.bash

#catkin setup
mkdir -p ~/catkin_wk/src
cd ~/catkin_wk/scr
source /opt/ros/indigo/setup.bash
catkin_init_workspace
cd ~/catkin_wk
catkin_make
