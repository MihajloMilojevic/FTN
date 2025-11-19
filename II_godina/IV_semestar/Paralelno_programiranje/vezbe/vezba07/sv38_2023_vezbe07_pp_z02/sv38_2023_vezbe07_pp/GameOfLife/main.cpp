// Sara Stojkov SV38/2023

#include "GameOfLife.h"
#include <iostream>
#include <string>
#include <tbb/tick_count.h>

#define NUM_OF_ITERATIONS 32
#define TABLE_SIZE 256

using namespace std;
using namespace tbb;

static void printTable(GameOfLife *game, int iterNum);

int main(int argc, char *argv[]) {

	unsigned long long startTicks, endTicks;

	GameOfLife gameSerial(TABLE_SIZE, TABLE_SIZE, PULSAR);
	GameOfLife gameParallel(TABLE_SIZE, TABLE_SIZE, PULSAR);


	int bornAgainCellsSerial = 0;
	int bornAgainCellsParallel = 0;
	cout << " TABLE SIZE: " << TABLE_SIZE << ", ITERATIONS: " << NUM_OF_ITERATIONS << endl;

	// serial version
	cout << "Serial Game of Life initiated..." << endl;
	tick_count startTime = tick_count::now();
	for (int i = 0; i < NUM_OF_ITERATIONS; i++) {
		//printTable(&gameSerial, i);
		bornAgainCellsSerial += gameSerial.nextIterSerial();		

	}
	tick_count endTime = tick_count::now();
	cout << "Serial time: \t\t\t" << (endTime - startTime).seconds() << " seconds\n";
	cout << "Reborn cells (serial): \t\t\t" << bornAgainCellsSerial << endl;
	
	
	// parallel version
	cout << "Parallel Game of Life initiated..." << endl;
	startTime = tick_count::now();
	for (int i = 0; i < NUM_OF_ITERATIONS; i++) {
		//printTable(&gameParallel, i);
		bornAgainCellsParallel += gameParallel.nextIterParallel(0, 0, TABLE_SIZE);		

	}
	endTime = tick_count::now();
	cout << "Parallel time: \t\t\t" << (endTime - startTime).seconds() << " seconds\n";
	cout << "Reborn cells (parallel): \t\t\t" << bornAgainCellsParallel << endl;

	int x = 0;
	cin >> x;

	return 0;
}

static void printTable(GameOfLife *game, int iterNum){	

	cout << "Iteration: " << iterNum << endl;
	game->printIteration();
	system("pause");
	system("cls");

	return;
}