#include <iostream>
#include "calcs.h"

int main()
{
    std::string choice = "";
    std::cout << "0. Exit\n1. Short\n2. Int\n3. Double\n";
    do {
        std::cout << "Enter choice: ";
        std::cin >> choice;
        if (choice == "1")
			calcShort();
		else if (choice == "2")
			calcInt();
		else if (choice == "3")
			calcDouble();
        else
            std::cout << "Invalid choice." << std::endl;
    } while (choice != "0");
}