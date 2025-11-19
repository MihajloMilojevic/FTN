/* Napisati konkurentni program koji koristi STL kontejner <map>. U main-u
 * inicijalizovati mapu tako da sadrzi 10 elemenata pri cemu je kljuc broj od
 * 1-10 a vrednost id niti main.
 * 
 * Kreirati 10 niti klasom thread. Svakoj niti se prosleduje njen redni broj
 * prilikom stvaranja i referenca na mapu. Svaka nit u mapi treba upise svoj id
 * na element kojem je kljuc redni broj date niti (1-10).
 * 
 * Na kraju programa iz mape ispisati id-eve niti u obrnutom redosledu rednog
 * broja niti.
 */
