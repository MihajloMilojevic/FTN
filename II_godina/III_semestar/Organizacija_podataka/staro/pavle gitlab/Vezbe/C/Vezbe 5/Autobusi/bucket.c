#include "bucket.h"


void printTrip(BusTrip trip)
{
    printf("%s %s %s %d ||", trip.id, trip.destination, trip.platform, trip.seats);
}

void printBucket(Bucket bucket)
{
    for(int i = 0; i < BUCKETING_FACTOR; i++)
        printTrip(bucket.trips[i]);
}

BusTrip readTrip()
{
    BusTrip trip;
    puts("ID: ");
    scanf("%s", trip.id);
    puts("Destination:" );
    scanf("%s", trip.destination);
    puts("Platform: ");
    scanf("%s", trip.platform);
    puts("Seats: ");
    scanf("%d", &trip.seats);
    trip.dateTime = readDateTime();
    trip.deleted = 0;
    return trip;
}

DateTime readDateTime()
{
    DateTime date_time;
    puts("DD.MM.YYYY. : ");
    scanf("%d.%d.%d.", &date_time.day, &date_time.month, &date_time.year);
    puts("HH:MM :");
    scanf("%d:%d", &date_time.hour, &date_time.minute);
    return date_time;
}

