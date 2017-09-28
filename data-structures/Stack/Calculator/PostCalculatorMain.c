#include <stdio.h>
#include "PostCalculator.h"

int main(void)
{
	char postEx1[] = "3-2+7";
	
	printf("%s = %d \n", postEx1, calEngine(postEx1)); 

	return 0;
}
