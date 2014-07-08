latest=0
nvidia304=0
nvidia173=0

for device in /proc/bus/pci/??/*; do
  Vendor=`hexdump -s 0 -n 2 -e '1/2 "%04x"' $device`
  Device=`hexdump -s 2 -n 2 -e '1/2 "%04x"' $device`
  Class=`hexdump -s 10 -n 2 -e '1/2 "%04x"' $device`
  if [[ "$Class" == 0300 && "$Vendor" == "10de" ]]; then
    if grep -Fxq "^0x$Device" nvidia_304.x_device_ids; then
      nvidia304=1
    elif grep -Fxq "^0x$Device" nvidia_173_device_ids; then
      nvidia173=1
    else
      latest=1
    fi
    
  fi

done

if [[ $latest == 1 ]]; then
    echo "nvidia-graphics-drivers-331-updates"
elif [[ $nvidia304 == 1 ]]; then
    echo "nvidia-graphics-drivers-304-updates"
elif [[ $nvidia173 == 1 ]]; then
    echo "nvidia-graphics-drivers-173"
fi
