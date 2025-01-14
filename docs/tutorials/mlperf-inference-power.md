# Power Measurement for MLPerf inference
## Requirements
1. Power analyzer (any one [certified by SPEC PTDaemon](https://www.spec.org/power/docs/SPECpower-Device_List.html)). Yokogawa is the one which most submitters have submitted with and a new single channel model like 310E can cost around 3000$.
2. SPEC PTDaemon (can be downloaded from [here](https://github.com/mlcommons/power) after signing the EULA which can be requested by email from `support@mlcommons.org`)
3. [MLCommons power-dev](https://github.com/mlcommons/power-dev) repository which has the `server.py` to be run on the director node and `client.py` to be run on the SUT node.

We need to connect the power analyzer to a director machine (via USB or Ethernet) and the power supply to the SUT is done through the power analyzer (current in series and voltage in parallel). The director machine runs the `server.py` script and loads a server process. When a client connects to it (using `client.py`), it inturn connects to the SPEC PTDaemon and initiates a measurement run. Once the measurement ends, the power log files are transferred to the client. 

## Ranging mode and Testing mode
Power analyzers usually have different current and voltage ranges it supports. But which one to be used depends on a given SUT and this needs some emperical data. We can do a ranging run where the current and voltage ranges are set to `Auto` and power analyzer automatically figures out the correct ranges needed. These ranges are then used for a proper testing mode run. Usage of 'auto' mode in a testing run is not allowed as it can mess up with the 
measurements.

## Setup using CM
### Install CM
```
python3 -m pip install cmind
cm pull repo mlcommons@ck
```
## Start Power Server (Power analyzer should be connected to this and PTDaemon runs here)
If you are having GitHub access to [MLCommons power](https://github.com/mlcommons/power) repository PTDaemon should be automatically installed by the below command.
```
cm run script --tags=mlperf,power,server --device_type=49 --device_port=/dev/usbtmc0
```
`--device_type=49` corresponds to Yokogawa 310E and `ptd -h` should list the device_type for all supported devices. More configuration options can be found [here](https://github.com/mlcommons/power-dev/tree/master/ptd_client_server)

### Running the power server inside a docker container
```
cm run script --tags=run,docker,container --cm_repo=octoml@ck --gh_token=<GitHub AUTH_TOKEN> \
--docker_os=ubuntu --docker_os_version=22.04 --device=/dev/usbtmc0 --port_maps,=4950:4950 \
--run_cmd="cm run script --tags=run,mlperf,power,server --adr.power-src.tags=_octoml --adr.power-src.version=fix"
```

## Running a dummy workload with power (on host machine)
```
cm run script --tags=mlperf,power,client --power_server=<POWER_SERVER_IP> 
```

### Run a dummy workload with power inside a docker container
```
cm run script --tags=run,docker,container --cm_repo=octoml@ck \
--docker_os=ubuntu --docker_os_version=22.04  \
--run_cmd="cm run script --tags==mlperf,power,client --power_server=<POWER_SERVER_IP>"
```

## Running MLPerf Image Classification with power (on host machine)
```
cm run script --tags=app,mlperf,inference,_reference,_power,_resnet50,_onnxruntime,_cpu --mode=performance
```

### Running MLPerf Image Classification with power inside a docker container
```
cm run script --tags=run,docker,container --cm_repo=octoml@ck  \
--docker_os=ubuntu --docker_os_version=22.04  \
--run_cmd="cm run script --tags=app,mlperf,inference,_reference,_power,_resnet50,_onnxruntime,_cpu --mode=performance"
```
