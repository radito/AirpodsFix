#!/usr/bin/env bash

scriptdir="$( dirname -- "$0"; )"

source "$scriptdir/.env"

cat /dev/null > "$scriptdir/out.txt"

echo -e "AirPods Bluetooth Fix Listener\n" | cat | tee -a "$scriptdir/out.txt"

echo "Interface Bluetooth: $INTERFACE_OUT" | tee -a "$scriptdir/out.txt"
echo "Interface Dummy: $INTERFACE_DUMMY" | tee -a "$scriptdir/out.txt"

echo "" | tee -a "$scriptdir/out.txt"

/usr/bin/log stream --process bluetoothd --style syslog --no-backtrace | grep --line-buffered -i 'A2DP packet flushed:' | /opt/homebrew/bin/python3 "$scriptdir/main.py" --int_out "$INTERFACE_OUT" --int_dmy "$INTERFACE_DUMMY" | tee -a "$scriptdir/out.txt"