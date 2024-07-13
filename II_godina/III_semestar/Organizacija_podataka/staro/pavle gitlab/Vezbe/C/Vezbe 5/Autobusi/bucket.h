#ifndef BUCKET_H_INCLUDED
#define BUCKET_H_INCLUDED


#include <stdio.h>
#include <stdlib.h>
#define BUCKETING_FACTOR 3
#define NUM_OF_BUCKETS 7


typedef struct {
    int day, month, year;
    int hour, minute;

} DateTime;

typedef struct {
    char id[8];
    char destination[51];
    DateTime dateTime;
    char platform[4];
    int seats;
    int deleted;
} BusTrip;

typedef struct {
    BusTrip trips[BUCKETING_FACTOR];
} Bucket;

void printTrip(BusTrip trip);
void printBucket(Bucket bucket);
BusTrip readTrip();
DateTime readDateTime();
#endif // BUCKET_H_INCLUDED
