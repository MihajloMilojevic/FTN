/*
 * Napisati program koji kreira jednosmerni FIFO kanal za komunikaciju
 * (pipe) i zatim klonira svoj proces.
 *
 * Originalni proces treba da ucita string sa standardnog ulaza
 * (najvise 100 karaktera) i zatim da ga posalje kopiji procesa preko
 * pipe-a.
 *
 * Kopija procesa treba da ucita najvise 100 karatera iz pipe-a i da
 * ih ispise na standardni izlaz.
 *
 * Osim toga, originalni proces mora da saceka da se kopija zavrsi pre
 * nego sto zavrsi sa svojim radom.
 */

#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define MAX_LENGTH 100

int main(void)
{
    /* Implementirati... */
}
