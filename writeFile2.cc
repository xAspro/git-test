#include <fstream>
#include <iostream>

using namespace std;

void writeFile(string filename)
{
        ofstream outfile;
        outfile.open(filename);
        if(!outfile)
	{
		cerr<<"Error! Couldnt create a file named " + filename + ".cc for writing\n";
		return;
        }

        outfile <<"Hello!\n";
        outfile <<"This is a sample line\n This is second line\n"<<" third line\n";

        outfile.close();
}
