
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include "MyComplex.h"

void splitString(const std::string& s, std::vector<std::string>& v, const std::string& delim) {
	int start = 0;
	int end = s.find(delim);
	while (end != std::string::npos) {
		v.push_back(s.substr(start, end - start));
		start = end + delim.length();
		end = s.find(delim, start);
	}
	v.push_back(s.substr(start, end));
}

int main()
{
	int errcode = 0;
	std::vector<std::string> filenames;
	filenames.push_back("input1.txt"); 
	for (std::string filename : filenames) {
		if (errcode) break;
		std::ifstream inFile(filename);
		if (!inFile.is_open()) {
			std::cerr << "Error opening file " << filename << std::endl;
			return 1;
		}
		std::ofstream outFile("o_" + filename);
		if (!outFile.is_open()) {
			std::cerr << "Error opening file " << "o_" + filename << std::endl;
			inFile.close();
			return 1;
		}
		std::string line;
		while (std::getline(inFile, line)) {
			if (errcode) break;
			if (line.empty()) continue;
			std::vector<std::string> tokens;
			splitString(line, tokens, " ");
			if (tokens.size() != 3) {
				std::cerr << "Invalid input format" << std::endl;
				errcode = 2;
				outFile << "Invalid input format" << std::endl;
				break;
			}
			try {
				MyComplex c1(tokens[0]);
				MyComplex c2(tokens[2]);
				MyComplex result;
				if (tokens[1] == "ADD") {
					result = c1 + c2;
				}
				else if (tokens[1] == "SUB") {
					result = c1 - c2;
				}
				else if (tokens[1] == "MUL") {
					result = c1 * c2;
				}
				else {
					std::cerr << "Invalid operation" << std::endl;
					errcode = 3;
					outFile << "Invalid operation" << std::endl;
					break;
				}
				outFile << "= " << result << std::endl;
			}
			catch (std::invalid_argument e) {
				std::cerr << e.what() << std::endl;
				errcode = 4;
				outFile << e.what() << std::endl;
				break;
			}
			
		}
		inFile.close();
		outFile.close();
	}
	if (!errcode) {
		std::cout << "Kraj" << std::endl;
	}
	return errcode;
}
