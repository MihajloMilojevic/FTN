#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <fstream>

#include "FullName.h"
#include "Scientist.h"

using namespace std;

// global variables
vector<FullName> scientistsNames;		//vector containing full names of scientists
list<int> scientistsIds;				//list containing ids of scientists
list<Scientist> scientists;				//list containing scientists (objects of class Scientist)

// function declarations
void loadScientists(ifstream& in);

void printNames();						//prints scientists' names
void printIds();						//prints scientists' ids
void printNamesAndIds();				//prints scientists' ids and names
void printNamesAndIdsInReverse();		//prints scientists' in reverse
void addScientist();					//adds new scientist

void fillScientistsList();				//fills scientists with scientists objects (formed of full names and ids)
void removeDuplicatesAndSortById();		//removes duplicates scientists and sorts them based on their id value
void printScientistsList();				//prints the list of scientists

// main
void main()
{
	ifstream in("scientists.txt");
	if (!in)
	{
		cerr << "ERROR: wrong input file name!";
		exit(-1);
	}

	loadScientists(in);

	printNames();
	cout << endl;
	
	printIds();
	cout << endl;

	printNamesAndIds();
	cout << endl;

	printNamesAndIdsInReverse();
	cout << endl;

	addScientist();

	printNamesAndIds();
	cout << endl;

	fillScientistsList();

	printScientistsList();
	cout << endl;

	removeDuplicatesAndSortById();
	
	printScientistsList();
	cout << endl;

	return;
}

void loadScientists(ifstream& in)
{
	while(!in.eof())
	{
		int id;
		string name;
		string surname;
		
		// @TODO: read id, name and surname from input file stream
		in >> id >> name >> surname;
		
		// @TODO: create Fullname object from name and surname and add object to the proper vector
		FullName fn(name, surname);
		scientistsNames.push_back(fn);
		// @TODO: add id to the proper list
		scientistsIds.push_back(id);
		// NOTE: vector and list are already defined as global variables -> NO NEED TO MAKE NEW ONES ! <-
	}
}

void printNames()
{
	// @TODO: using iterators print the vector of names
	for (auto it = scientistsNames.begin(); it != scientistsNames.end(); ++it)
		std::cout << it->getName() << " " << it->getSurname() << std::endl;
}

void printIds()
{
	// @TODO: using iterators print the list of ids
	for (auto it = scientistsIds.begin(); it != scientistsIds.end(); ++it)
		std::cout << *it << std::endl;
}

void printNamesAndIds()
{
	// @TODO: using iterators print scientist id and the its name and surname
	// using list of ids and vector of names
	auto nameIt = scientistsNames.begin();
	auto idIt = scientistsIds.begin();
	while (nameIt != scientistsNames.end() && idIt != scientistsIds.end())
	{
		std::cout << *idIt << " " << nameIt->getName() << " " << nameIt->getSurname() << std::endl;
		++nameIt;
		++idIt;
	}
}

void printNamesAndIdsInReverse()
{
	// @TODO: using iterators print scientist id and the its name and surname
	// using list of ids and vector of names, in reverse
	auto nameIt = scientistsNames.rbegin();
	auto idIt = scientistsIds.rbegin();
	while (nameIt != scientistsNames.rend() && idIt != scientistsIds.rend())
	{
		std::cout << *idIt << " " << nameIt->getName() << " " << nameIt->getSurname() << std::endl;
		++nameIt;
		++idIt;
	}
}

void addScientist()
{
	FullName newScientist("Petar", "Petrovic");
	int newID = 999;
	
	FullName findName("Nikola", "Tesla");
	int findId = 123;
	
	// @TODO: add new scientist "Petar Petrovic" with "999" ID, after
	// "Nikola Tesla" who has "123" as ID
	auto nameIt = scientistsNames.begin();
	auto idIt = scientistsIds.begin();
	while (nameIt != scientistsNames.end() && idIt != scientistsIds.end())
	{
		if (*nameIt == findName && *idIt == findId) {
			scientistsNames.insert(++nameIt, newScientist);
			scientistsIds.insert(++idIt, newID);
			break;
		}
		++nameIt;
		++idIt;
	}
}

void fillScientistsList()
{
	// @TODO: fill the list of scientists by creating objects of class Scientist
	// NOTE: use existing vector of names and list of ids to create Scientist objects

	auto nameIt = scientistsNames.begin();
	auto idIt = scientistsIds.begin();
	while (nameIt != scientistsNames.end() && idIt != scientistsIds.end())
	{
		Scientist sc(*nameIt, *idIt);
		scientists.push_back(sc);
		++nameIt;
		++idIt;
	}
}

void removeDuplicatesAndSortById()
{
	// @TODO sort the list of scientists and remove duplicate occurencies
	scientists.sort();
	scientists.unique();
}

void printScientistsList()
{
	// @TODO print the list of scientists
	for (Scientist s : scientists) {
		std::cout << s.getId() << " " << s.getFullName().getName() << " " << s.getFullName().getSurname() << std::endl;
	}
}
