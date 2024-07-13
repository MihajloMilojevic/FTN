#include <stdio.h>
#include <stdlib.h>
#include "hash.h"
#include "bucket.h"
#include <string.h>

void createEmptyFile(FILE *file)
{
    fseek(file, 0, SEEK_SET);
    Bucket *bucket = calloc(NUM_OF_BUCKETS, sizeof(Bucket));
    fwrite(bucket, sizeof(Bucket), NUM_OF_BUCKETS, file);
}

void printFile(FILE *file)
{
    fseek(file, 0, SEEK_SET);
    Bucket buckets[NUM_OF_BUCKETS];
    fread(buckets, sizeof(Bucket), NUM_OF_BUCKETS, file);
    for (int i = 0; i < NUM_OF_BUCKETS; i++)
    {
        printf("Bucket number %d: \n", i);
        printBucket(buckets[i]);
        printf("\n");
    }
}

void addTrip(FILE *file, BusTrip trip_to_write)
{
    BusTrip trip[BUCKETING_FACTOR];
    int bucket_num = getHash(trip_to_write.id);
    int check = findTrip(file, trip_to_write.id, &trip[0]);
    if(check == 1)
    {
        printf("Postoji put sa tim identifikatorom!\n");
        return;
    }
    fseek(file, 0, SEEK_SET);
    fseek(file, sizeof(Bucket)*bucket_num, SEEK_SET);
    int i = 0;
    printf("%d\n", file == NULL);
    fread(trip, sizeof(BusTrip), BUCKETING_FACTOR, file);
    while((trip[i].id[0] != '\0') && i < BUCKETING_FACTOR)
    {
        i++;
    }
    if (i >= BUCKETING_FACTOR)
    {
        printf("Prekoracenje!\n");
        return;
    }
    fseek(file, sizeof(Bucket)*bucket_num + sizeof(BusTrip)*i, SEEK_SET);
    fwrite(&trip_to_write, sizeof(BusTrip), 1, file);
    fflush(file);
}

int findTrip(FILE *file, char *id, BusTrip *to_trip)
{
    int bucket_num = getHash(id);
    fseek(file, 0, SEEK_SET);
    fseek(file, sizeof(Bucket)*bucket_num, SEEK_SET);
    BusTrip trip[BUCKETING_FACTOR];
    int i = 0;
    fread(trip, sizeof(BusTrip), BUCKETING_FACTOR, file);
    while(i < BUCKETING_FACTOR)
    {
        if(strcmp(trip[i].id, id) == 0 && trip[i].deleted != 1)
        {
            (*to_trip) = trip[i];
            return 1;
        }
        i++;
    }

    return 0;
}

void rewriteTrip(FILE *file, BusTrip trip)
{
    int bucket_num = getHash(trip.id);
    fseek(file, 0, SEEK_SET);
    fseek(file, sizeof(Bucket)*bucket_num, SEEK_SET);
    BusTrip read_trip[BUCKETING_FACTOR];
    int i = 0;
    fread(read_trip, sizeof(BusTrip), BUCKETING_FACTOR, file);
    while(i < BUCKETING_FACTOR)
    {
        if(strcmp(read_trip[i].id, trip.id) == 0)
        {
            break;
        }
        i++;
    }
    if(i >= BUCKETING_FACTOR)
    {
        printf("Ne postoji takav put.\n");
        return;
    }
    fseek(file, sizeof(Bucket)*bucket_num + sizeof(BusTrip)*i, SEEK_SET);
    fwrite(&trip, sizeof(BusTrip), 1, file);
    fflush(file);
}

int getHash(char *trip_id)
{
    int id = atoi(trip_id);
    return id % NUM_OF_BUCKETS;
}
