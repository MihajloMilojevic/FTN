#ifndef HASH_H_INCLUDED
#define HASH_H_INCLUDED
#include "bucket.h"

void createEmptyFile(FILE *file);
void addTrip(FILE *file, BusTrip trip_to_write);
void printFile(FILE *file);
int getHash(char *trip_id);
void rewriteTrip(FILE *file, BusTrip trip);

#endif // HASH_H_INCLUDED
