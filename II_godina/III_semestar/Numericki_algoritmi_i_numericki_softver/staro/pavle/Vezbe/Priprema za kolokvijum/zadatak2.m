clc
clear all

A = [
    1 -2 1 -8
    3 -9 27 -12
    4 -12 64 -12
    2 -2 8 -4];
b = [11.5 7.8 9.9 5]';
x = NANSLib.gauss_PP(A, b)