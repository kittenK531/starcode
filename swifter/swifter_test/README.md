# Swifter modified

## How to use
To minimise the time of operation and calculation, I have removed all stdout possible and recompiled.
It is less userfriendly but more time-saving. Under the swifter directory, you will find test.sh. Which produces test/follow.out containing the osculating elements at a time step.

```
./test.sh
```

## Note

The standard procedure of operation is 
```
cd example
./../bin/swifter_tu4 ==> select param.in
./../bin/tool_follow ==> dump_param1/2.dat
```

## TO-B-developed
Automation of parameter changes without using input files