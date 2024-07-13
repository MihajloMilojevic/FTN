#include <stdio.h>
#include <stdlib.h>
#include "hash.h"
#include "bucket.h"
#define DEFAULT_INFILENAME "in.dat"
#define LEN 31

int menu();
FILE *safeFopen(char filename[]);
void handleResult(int returnCode);
void fromTxtToSerialFile(FILE *pFtxt, FILE *pFbin);
FILE* open_file(FILE *file);

int main() {
    FILE *file = NULL;
    char filename[LEN];
    char id[8];
    int option = -1, key;
    BusTrip trip;
    int new_seats;
    while (option) {
        option = menu();
        switch (option) {
            case 1:
                file = open_file(file);
                break;
            case 2:
                file = open_file(file);
                printFile(file);
                break;
            case 3:
                file = open_file(file);
                trip = readTrip();
                addTrip(file, trip);
                break;
            case 4:
                file = open_file(file);
                printf("Unesite id: ");
                scanf("%s", id);
                if(findTrip(file, id, &trip) == 0)
                {
                    printf("Ne postoji takav put.\n");
                    break;
                }
                printTrip(trip);
                break;
            case 5:
                file = open_file(file);
                printf("Unesite id: ");
                scanf("%s", id);
                if(findTrip(file, id, &trip) == 0)
                {
                    printf("Ne postoji takav put.\n");
                    break;
                }
                printTrip(trip);
                printf("Unesite novi broj mesta: ");
                scanf("%d", &new_seats);
                trip.seats = new_seats;
                rewriteTrip(file, trip);
                break;
            case 6:
                file = open_file(file);
                printf("Unesite id: ");
                scanf("%s", id);
                if(findTrip(file, id, &trip) == 0)
                {
                    printf("Ne postoji takav put.\n");
                    break;
                }
                printTrip(trip);
                trip.deleted = 1;
                rewriteTrip(file, trip);
                break;
            default:
                break;
        }
    }

    if (file != NULL) fclose(file);

    return 0;
}
FILE* open_file(FILE *file)
{
    char filename[LEN];
    if (file == NULL)
    {
        printf("\nUnesite naziv datoteke: \n");
        scanf("%s", filename);
        file = safeFopen(filename);
    }
    return file;
}

int menu() {
    int option;

    puts("\n\nIzaberite opciju:");
    puts("\t1. Otvaranje datoteke");
    puts("\t2. Prikaz");
    puts("\t3. Unos novog sloga");
    puts("\t4. Pretraga sloga");
    puts("\t5. Izmena mesta u autobusu");
    puts("\t6. Brisanje sloga");
    puts("\t0. Kraj programa");

    printf(">>");

    scanf("%d", &option);
    getchar();
    return option;
}

FILE *safeFopen(char filename[]) {
    FILE *pFile;

    pFile = fopen(filename, "rb+");

    if (pFile == NULL) {
        pFile = fopen(filename, "wb+");
        createEmptyFile(pFile);
        puts("Kreirana prazna datoteka.");
    } else {
        puts("Otvorena postojeca datoteka.");
    }

    if (pFile == NULL) {
        printf("Nije moguce otvoriti/kreirati datoteku: %s.\n", filename);
    }

    return pFile;
}


