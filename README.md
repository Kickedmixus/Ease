# Ease v1.0.4a
Simple python library for customizable in/out easing utilities

## Types of easing

##### - linear - x

##### - sine - sin(x*pi/2)

##### - quad/quadratic - x^2

##### - cube/cubic - x^3

##### - quart/quartic - x^4

##### - quint/quintic - x^4

## Main functions

#### - easeIn ( type , start , end , length , reverse = False )

#### - easeOut ( type , start , end , length , reverse = False )

#### - easeInOut ( type , start , end , length , swap = False)

## Function inputs ( easeIn(), easeOut() , easeInOut() )

####    -type (Types of easing)

####    -start (start vaule)

      |
    | |
  | | |
| | | |
^

####    -end (end vaule)

      |
    | |
  | | |
| | | |
      ^

####    -length (amount of data vaules)

      |
    | |
  | | |
| | | |
[     ]

####    -reverse (if true in easeIn() or easeOut(), reverses list)

####    -swap (if true in easeInOut() swaps the order of eases, allowing for a "easeOutIn")