#include <stdio.h>
#include "PostCalculator.h"

int main(void)
{
	char postEx1[] = "3+2*7";
	char postEx2[] = "(3-2)*7";
	char postEx3[] = "(4+5)/3";
	
	//infixExpToPostExp
	infixExpToPostExp(postEx1);
	printf("%s \n", postEx1);

	//postExpToValue
	printf("%d \n", postExpToValue(postEx1));

	//calEngine
	printf("%s = %d \n", postEx1, calEngine(postEx1)); 
	printf("%s = %d \n", postEx2, calEngine(postEx2)); 
	printf("%s = %d \n", postEx3, calEngine(postEx3)); 

	return 0;
}
