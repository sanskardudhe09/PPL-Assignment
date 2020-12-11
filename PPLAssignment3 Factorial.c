#include <stdio.h>

/* Function: find_fact 
 * To find factorial of given number recursively.
 */
int find_fact(int n)
{
	if(n==0)
		return 1;
	else 
		return n * find_fact(n-1);
}

int main()
{
	int num; // Declare variable 'num' to hold value of number
	int fact; // Declare variable 'fact' to hold value of factorialg
	
	printf("Enter a number: "); // Display message to enter number
	scanf("%d", &num); // Read number 
	
	if(num<0){
		printf("Factorial of negative number doesn't exists.\n");
		return 0;
	}
	
	fact = find_fact(num); // Call function 'find_fact' to compute factorial of 'num'
	
	// Display value of factorial
	printf("Factorial is %d\n", fact);
}
