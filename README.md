# Ease v1.0.3a
Simple python library for customizable in/out easing utilities

## Types of easing

#### -linear - x

#### -sine - sin(x*pi/2)

#### -quad/quadratic - x^2

#### -cube/cubic - x^3

#### -quart/quartic - x^4

#### -quint/quintic - x^4

## Main functions

#### - easeIn ( type , start , end , length )

#### - easeOut ( type , start , end , length )

#### - easeInOut ( type , start , end , length )

## Function inputs ( easeIn(), easeOut() , easeInOut() )

####    -type (Types of easing)

####    -start (start vaule)

            #
            #
          # #
    # # # # # 
    ^
    1

####    -end (end vaule)


            #
            #
          # #
    # # # # #
            ^
            4

####    -length (amount of data vaules)


            #
            #
          # #
    # # # # #
    [       ] 5
