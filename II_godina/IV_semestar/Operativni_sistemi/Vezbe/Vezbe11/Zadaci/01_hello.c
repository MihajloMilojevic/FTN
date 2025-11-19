/*
 * Napisati program koji ispise poruku na standardni izlaz upotrebom
 * samo sistemskih poziva.
 *
 * Napomena 1: Deskriptor datoteke za standardni izlaz je uvek 1, a
 * nalazi se i u konstanti STDOUT_FILENO.
 *
 * Napomena 2: U C-u se duzina konstantnog string-a koji je deklarisan
 * sa inicijalizacijom moze dobiti i bez funkcije strlen()-a pomocu
 * sizeof() operatora, na primer:
 *
 * char poruka[] = "Hello, world!\n";
 *
 * Duzina string-a "poruka" (bez NUL karaktera na kraju) se moze
 * dobiti sa sizeof(poruka) - 1.
 */

#include <unistd.h>
#include <stdlib.h>

int main(void)
{
    /* Implementirati... */
    char poruka[] = "Hello, world!\n";
    ssize_t n = write(1, poruka, sizeof(poruka));
    exit(n);
}
