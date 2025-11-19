#include "GameOfLife.h"
#include <iostream>
#include <string>
#include <vector>
#include "string.h"
#include "tbb/tick_count.h"

#define NUM_OF_ITERATIONS 100
#define TABLE_SIZE 1000

using namespace std;
using namespace tbb;

struct Result {
	int TableSize;
	int IterCount;

	double SerialTime;
	double ParallelTime;
	double ReduceTime;

	int SerialRebirths;
	int ParallelRebirths;
	int ReduceRebirts;
};

static void printTable(GameOfLife* game, int iterNum);
static Result runWithParameters(int tableSize, int numberOfIterations);

int main(int argc, char* argv[]) {
	std::vector<int> dimensions = {20, 50, 100, 300, 500, 1000};
	std::vector<int> iters = { 20, 50, 100, 300, 500, 1000 };

	std::vector<std::vector<Result> > results(dimensions.size());

	for (int i = 0; i < dimensions.size(); ++i) {
		results[i].reserve(iters.size());
		for (int j = 0; j < iters.size(); ++j) {
			results[i][j] = runWithParameters(dimensions[i], iters[j]);
		}
	}

	for (int i = 0; i < dimensions.size(); ++i) {
		printf("     ");
		for (int j = 0; j < iters.size(); ++j) {
			printf("%10d", iters[j]);
		}
		printf("\n");
		printf("%5d", dimensions[i]);
		for (int j = 0; j < iters.size(); ++j) {
			printf("(%1.4f, %1.4f) ", results[i][j].SerialTime, results[i][j].ParallelTime);
		}
		printf("\n");
	}

	return 0;
}



static Result runWithParameters(int tableSize, int numberOfIterations) {
	unsigned long long startTicks, endTicks;

	Result result{};
	result.TableSize = tableSize;
	result.IterCount = numberOfIterations;

	cout << "Running with paramaters: TABLE_SIZE = " << tableSize << " ITERS = " << numberOfIterations << "\n\n";

	GameOfLife game(tableSize, tableSize, PULSAR);
	int rebornCells = 0;

	// serial version
	cout << "Serial Game of Life initiated..." << endl;
	tick_count startTime = tick_count::now();
	for (int i = 0; i < numberOfIterations; i++) {
		//printTable(&game, i);
		rebornCells += game.nextIterSerial();
	}
	tick_count endTime = tick_count::now();
	cout << "Serial time: \t\t\t" << (endTime - startTime).seconds() << " seconds\n";
	cout << "Reborn cells: \t\t\t" << rebornCells << endl;
		
	result.SerialTime = (endTime - startTime).seconds();
	result.SerialRebirths = rebornCells;

	cout << "==================================\n\n";
	// parallel version

	GameOfLife parallelGame(tableSize, tableSize, PULSAR);
	rebornCells = 0;
	cout << "Parallel Game of Life initiated..." << endl;
	startTime = tick_count::now();
	for (int i = 0; i < numberOfIterations; i++) {
		//printTable(&parallelGame, i);
		rebornCells += parallelGame.nextIterParallel(0, 0, tableSize, tableSize);
	}
	endTime = tick_count::now();
	cout << "Parallel time: \t\t\t" << (endTime - startTime).seconds() << " seconds\n";
	cout << "Reborn cells: \t\t\t" << rebornCells << endl;
	result.ParallelTime = (endTime - startTime).seconds();
	result.ParallelRebirths = rebornCells;
	cout << "==================================\n\n";

	// parallel version

	GameOfLife reduceGame(tableSize, tableSize, PULSAR);
	rebornCells = 0;
	int temp = 0;
	cout << "Reduce Game of Life initiated..." << endl;
	startTime = tick_count::now();
	for (int i = 0; i < numberOfIterations; i++) {
		//printTable(&reduceGame, i);
		temp += reduceGame.nextIterParallel(0, 0, tableSize, tableSize);
		rebornCells += reduceGame.calculateReborn();
	}
	endTime = tick_count::now();
	cout << "Reduce time: \t\t\t" << (endTime - startTime).seconds() << " seconds\n";
	cout << "Reborn cells: \t\t\t" << rebornCells << endl;
	cout << "Reborn cells: \t\t\t" << temp << endl;
	result.ReduceTime = (endTime - startTime).seconds();
	result.ReduceRebirts = rebornCells;
	cout << "==================================\n\n";

	return result;
}


static void printTable(GameOfLife* game, int iterNum) {

	cout << "Iteration: " << iterNum << endl;
	game->printIteration();
	system("pause");
	system("cls");

	return;
}