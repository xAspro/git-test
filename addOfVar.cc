#include<iostream>
using namespace std;

int main()
{
	int var1;
	char var2[10];

	cout <<"Address of var1 variable: ";
	cout <<&var1 <<endl;

	cout <<"Address of var2 variable: ";
	cout <<&var2 <<endl;

	

	int var=1;
	int *y;
	y=&var;

	cout <<"y =&var = "<< y << "    address of stored address is    "<< &y << "   value stored in y(that address) is "<< *y <<endl;
	cout <<"&var ="<< &var <<"    address of variable is(same as earlier first value) "<< &var << endl;

	return 0;
}

