# Power Measurement for MLPerf inference
## Requirements
1. Power analyzer (any one certified by SPEC PTDaemon)
2. SPEC PTDaemon (can be downloaded from here after signing the EULA)
3. MLCommons power-dev repository

We need to connect the power analyzer to a director machine (via USB or Ethernet) and the power supply to the SUT is done through the power analyzer 
(current in series and voltage in parallel). The director machine runs the `server.py` script and loads a server process. When a client connects to it 
(using `client.py`), it inturn connects to the SPEC PTDaemon and initiates a measurement run. Once the measurement ends, the power log files are 
transferred to the client. 

## Ranging mode and Testing mode
Power analyzers usually have different current and voltage ranges it supports. But which one to be used depends on a given SUT and this needs some 
emperical data. We can do a ranging run where the current and voltage ranges are set to `Auto` and power analyzer automatically figures out the correct
ranges needed. These ranges are then used for a proper testing mode run. Usage of 'auto' mode in a testing run is not allowed as it can mess up with the 
measurements.

## Setup using CM

## Running a dummy workload with power

## Running MLPerf Image Classification with power
