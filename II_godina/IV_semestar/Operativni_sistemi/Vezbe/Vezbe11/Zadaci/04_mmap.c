/*
 * Napisati program koji sifruje datoteku ROT13 algoritmom pomocu
 * sistemskih poziva.
 *
 * ROT13 algoritam pretvara zamenjuje slova A-M sa slovima N-Z, i
 * obrnuto. Drugacije gledano, na redni broj slova (izmedju 0 i 25) se
 * dodaje broj 13, a zatim se uzima ostatak pri deljenju sa 26 kako bi
 * se dobio novi redni broj. Karakteri koji nisu velika ili mala slova
 * ostaju nepromenjeni.
 *
 * Program treba da otvori datoteku ciji je naziv dat u parametru
 * komandne linije, i da mapira celokupan sadrzaj te datoteke u
 * memoriju pomocu sistemskog poziva mmap(). Zatim se ROT13 algoritam
 * primenjuje nad nizom koji predstavlja sadrzaj cele datoteke.
 */

#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/mman.h>
#include <sys/stat.h>

int main(int argc, char *argv[])
{
    /* Implementirati... */
}
