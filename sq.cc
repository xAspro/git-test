#include<iostream>
using namespace std;

float square(float a)
{
	return a*a;
}

int main()
{
	float a;
	cout <<"Enter a number"<< endl;
	cin >> a;

	cout << "square is " <<square(a)<<endl;
}
