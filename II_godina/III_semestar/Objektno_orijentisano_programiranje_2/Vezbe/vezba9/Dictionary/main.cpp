#include <iostream>
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <map>

using namespace std;

void readInputFile(ifstream& in);
void erasePunctuation(string& word);
void printOccurencesForTheWord(string findWord);
void generateDictonary(ofstream& out);
void generateStats(ofstream& out);

// used for storing words read from the input file
set<string> dictionary;

// used for storing pairs of words and their occurences read from the input file
map<string, int> occurances;


// array used for generating the dictonary file (a - a, at, ace...)
char alphabet[] = "abcdefghijklmnopqrstuvwxyz";


void main()
{
	string word;
	
	ifstream in("hobbit.txt");
	if (!in)
	{
		cerr << "Invalid input file name";
		exit(-1);
	}

	ofstream outDictionary("dict.txt");
	if (!outDictionary)
	{
		cerr << "Invalid output file name";
		exit(-1);
	}

	ofstream outStats("stats.txt");
	if (!outStats)
	{
		cerr << "Invalid output file name";
		exit(-1);
	}

	// reads the input file and fills the set: dictionary and the map: occurances
	readInputFile(in);

	// prints the desired key-value pair, based on the key
	printOccurencesForTheWord("dwarf");
	printOccurencesForTheWord("dwarfs");

	// generates the output file-dictonary
	generateDictonary(outDictionary);

	// generates the output file containing statistics of the word length usage
	generateStats(outStats);

	return;
}


void readInputFile(ifstream& in)
{
	string word;

	while (!in.eof())
	{

		// if a word is just punctuation skip it
		
		// if a word contains punctuation erase it from the word

		// lower the case of the word

		// fill the dictionary set with the words and the 
		// occurances map with number of occurences of the word
	}
}


void erasePunctuation(string& word)
{
	// there is a function that can check if the character is punctuation
}


void printOccurencesForTheWord(string findWord)
{
	// print the number of the occurences for the desired word
}


void generateDictonary(ofstream& out)
{
	// write out to the output file the dictonary of the words from the input file
	// use the set and the alphabet array
}


void generateStats(ofstream& out)
{
	// create a map which will contain pairs of: word length, and occurences of that word length
	// example: dictonary contains:
	// ate, ate, bar, barn
	// map contains [0] -> 3, 3, [1] -> 4, 1

	// write out to the output the statistics of the usage of certain word length
}
