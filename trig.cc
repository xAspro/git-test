#include<iostream>
#include<cmath>

using namespace std;

int main()
{
	double x=0.44, res= sin(x);
	cout<<"sin("<<x<<"rad)= "<<res<<endl;

	x=90;

	res=sin(x);
	cout<<"sin("<<x<<"rad)= "<<res<<endl;

	x=x*M_PI/180;
	res=sin(x);
	cout<<"sin("<<x<<"rad)= "<<res<<endl;

	int fact=1;
	double sum=0;
	
	cout<<"Enter x value for taylor series expansion for sin: "
	cin>>x;
	for(int n=0;n<5;n++)
	{
		sum+=pow((-1),n)*pow((x),(2*n+1))/(fact);
		fact*=2*(n+1)*(2*(n+1)+1);
	}

	cout <<"sum= "<<sum<<endl;
}
