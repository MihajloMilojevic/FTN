/*
 * Napisati program koji klonira trenutni proces, i zatim:
 *
 * Originalni proces treba svaki sekund da ispise poruku "Prosao je
 * jedan sekund." pomocu sistemskog poziva alarm() i signala SIGALRM.
 *
 * Pomocu signala SIGCHLD, treba detektovati kraj izvrsavanja kopije
 * procesa i ispisati poruku "Kopija procesa je zavrsila sa radom.".
 *
 * Kopija procesa samo treba da ceka 5 sekundi.
 *
 * Kada korisnik pritisne kombinaciju tastera Ctrl+C (signal SIGINT),
 * treba ispisati poruku "Pritisnuli ste Ctrl+C, program zavrsava sa
 * radom.", i zatim prekinuti originalni proces.
 */

#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

int main(void)
{
    /* Implementirati... */
}
