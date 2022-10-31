#include<iostream>
#include<fstream>
using namespace std;

void readFile (string filename) 
{
	
	ifstream infile (filename);

	if (!infile) 
	{
		cerr << "Uh oh, " + filename + " could not be opened for reading!\n";
		return;
	}
	
	while (infile) 
	{
		string inp;
		infile >> inp;
		cout << inp << endl;
	}
	
	infile.close();
	
}

int main()
{
	readFile("writtenFile.txt");
	readFile("writtenfile.txt");
}
