#include<iostream>
using namespace std;

int main()
{
	int i=0,c;
	do
	{
		c=i*i*i;
		cout << c << endl;

		i++;
	}while(c<1000);
}
