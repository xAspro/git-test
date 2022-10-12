#include<iostream>
using namespace std;

int main()
{
	cout << "Enter n: ";
	int n;
	cin >> n;
	cout <<"Printing first n natural numbers" << endl;

	for(int i=1; i<=n; i++)
	{
		cout << i<<endl;
	}
}
