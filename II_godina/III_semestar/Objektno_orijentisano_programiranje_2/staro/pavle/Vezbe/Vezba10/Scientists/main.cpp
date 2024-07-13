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
	cout << "Print names: " << endl;
	printNames();
	cout << endl;
	cout << "Print ids: " << endl;
	printIds();
	cout << endl;
	cout << "Print names and ids: " << endl;
	printNamesAndIds();
	cout << endl;
	cout << "Print names and ids in reverse: " << endl;
	printNamesAndIdsInReverse();
	cout << endl;

	addScientist();
	cout << "Print names and ids: " << endl;
	printNamesAndIds();
	cout << endl;

	fillScientistsList();
	cout << "Print scientists: " << endl;
	printScientistsList();
	cout << endl;

	removeDuplicatesAndSortById();
	cout << "Print unique and sorted: " << endl;
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
		FullName full(name, surname);
		
		scientistsNames.push_back(full);		//vector containing full names of scientists
		// @TODO: add id to the proper list
		scientistsIds.push_back(id);
		// NOTE: vector and list are already defined as global variables -> NO NEED TO MAKE NEW ONES ! <-
	}
}

void printNames()
{
	// @TODO: using iterators print the vector of names
	vector<FullName>::iterator it1;
	for (it1 = scientistsNames.begin(); it1 < scientistsNames.end(); it1++)
	{
		cout << (*it1).getName() << " " << (*it1).getSurname() << endl;
	}

}

void printIds()
{
	// @TODO: using iterators print the list of ids
	list<int>::iterator it1;
	for (it1 = scientistsIds.begin(); it1 != scientistsIds.end(); it1++)
	{
		cout << (*it1) << endl;
	}
}

void printNamesAndIds()
{
	// @TODO: using iterators print scientist id and the its name and surname
	// using list of ids and vector of names
	vector<FullName>::iterator it1;
	list<int>::iterator it2;
	for (it1 = scientistsNames.begin(), it2 = scientistsIds.begin(); it1 < scientistsNames.end(); it1++, it2++)
	{
		cout << (*it2) << " " << (*it1).getName() << " " << (*it1).getSurname() << endl;
	}
}

void printNamesAndIdsInReverse()
{
	// @TODO: using iterators print scientist id and the its name and surname
	// using list of ids and vector of names, in reverse
	cout << "Reverse : " << endl;
	vector<FullName>::reverse_iterator it1;
	list<int>::reverse_iterator it2;
	for (it1 = scientistsNames.rbegin(), it2 = scientistsIds.rbegin(); it1 < scientistsNames.rend(); it1++, it2++)
	{
		cout << (*it2) << " " << (*it1).getName() << " " << (*it1).getSurname() << endl;
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
	vector<FullName>::iterator it1;
	for (it1 = scientistsNames.begin(); it1 < scientistsNames.end(); it1++)
	{
		if ((*it1) == findName)
		{
			scientistsNames.insert(++it1, newScientist);
			break;
		}
	}

	list<int>::iterator it2;
	for (it2 = scientistsIds.begin(); it2 != scientistsIds.end(); it2++)
	{
		if ((*it2) == findId)
		{
			scientistsIds.insert(++it2, newID);
			break;
		}
	}
	
}

void fillScientistsList()
{
	// @TODO: fill the list of scientists by creating objects of class Scientist
	// NOTE: use existing vector of names and list of ids to create Scientist objects
	vector<FullName>::iterator it1;
	list<int>::iterator it2;
	int id;
	for (it1 = scientistsNames.begin(), it2 = scientistsIds.begin(); it1 < scientistsNames.end(); it1++, it2++)
	{
		id = (*it2);
		FullName full((*it1).getName(), (*it1).getSurname());
		Scientist sc(full, id);
		scientists.push_back(sc);
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
	list<Scientist>::iterator it1;
	int id;
	for (it1 = scientists.begin(); it1 != scientists.end(); it1++)
	{
		cout << (*it1).getId() << " " << (*it1).getFullName().getName() << " " <<
			(*it1).getFullName().getSurname() << endl;
	}
}
