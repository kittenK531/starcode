# Kepler's orbit simulation documentation
This package simulates particle keplerian orbits around massive star with given initial velocity and position.

Detailed simulation details found in [here](https://kittenk531.github.io/starcode-track/).

## Prequisites
It is suggested that an isolated virtual environment is created under execution
```
conda create -n starcode python==3.8
conda activate starcode
pip install loguru (autoflake black isort)
```
The packages bracketed are optional for collaboration purposes (pre-commit reformatting).

## Units
Consistent unit set through out the calculations used is listed as below
* Mass: solar mass (Mo)
* Length: astronomical unit (AU)
* Time: year (yr)

Remarks: display of mass for dark matter particle is in GeV for easy reference to literatures.

## How to run?
Amend arguments of 
* M: mass of massive star (solar mass Mo)
* mx: mass of dark matter particle (GeV)
* N: number of steps of evolution
* h: timestep (yr)
```
python3 orbit.py 
```

## Methods
By numeric integration of equation of motion, the updating of positions and velocity is implemented by verlet method.

Since the range of dark matter particle mass is of range 10^-3 to 10^19, the order of magnitude for DM particle is significantly less than the sun, it is thus assumed that the sun is stationary/ (in the rest frame of the sun) in our calculation.


## Possible issue
1. Partition for the mass distribution (point source approximation of massive star may bug)
2. Energy drift (sympletic): swifter
3. Ambient dark matter capture change of mass: cross section * lifetime * pi R ^2 

## TODO: Monte Carlo + logic