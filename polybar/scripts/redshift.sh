#!/bin/sh

envFile=~/.config/polybar/scripts/env.sh
changeValue=300

changeMode() {
  sed -i "s/REDSHIFT=$1/REDSHIFT=$2/g" $envFile 
  REDSHIFT=$2
  echo $REDSHIFT
}

case $1 in 
  toggle) 
    if [ "$REDSHIFT" = on ];
    then
      changeMode "$REDSHIFT" off
      pkill redshift
    else
      changeMode "$REDSHIFT" on
      redshift -l -45.5:170.5
    fi
    ;;
  temperature)
    case $REDSHIFT in
      on)
        printf " ON "
        ;;
      off)
        printf " OFF "
        ;;
    esac
    ;;
esac

