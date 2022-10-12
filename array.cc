#include<iostream>
using namespace std;

int main()
{
	int a[5];

	double b[5]={0};

	for(int i=0;i<5;i++)
	{
		cout << "Should be a trash value "<< a[i] << "      now all zeroes " << b[i] <<endl;
	}

	cout <<"Checking whats a[length] is " << a[5]<< "   " << b[5] << endl;
}
