#include<iostream>
using namespace std;

void square(float *a,int n)
{
	for(int i =0;i<n;i++)
	{
		*a *=*a; 
		a++;
	}
}

void square(long int *a,int n)
{
	for(int i =0;i<n;i++)
	{
		*a *=*a; 
		a++;
	}
}

int main()
{
	float a[5] ={10.0, 5.0, 20.0, 34.0, 39.2};
	square(a, 5);

	long int b[8]={1,2,3,4,5,6,7,8};
	square(b,8);
	
	cout <<"The square of the array is :"; 
	
	for(int i =0;i<5;i++)
	{
		cout <<a[i] <<",";
	}
	
	cout<<endl; 


	cout <<"The square of the array is :"; 
	for(int i =0;i<8;i++){
		cout <<b[i] <<",";
	}
	cout<<endl; 

	cout <<&b[0]<<endl;
	cout <<b[0]<<endl;
	cout <<*(&b[0]+1)<<endl;
	cout <<b[1]<<endl;

	cout<<*(&b[0]+4)<<endl;
	cout<<b[4]<<endl;

	return 0;
}

