#include "ArrayList.h"
#include <stdio.h>

int main(void)
{
	List list;
	int data;

	ListInit(&list);

	LInsert(&list, 11);
	LInsert(&list, 11);
	LInsert(&list, 22);
	LInsert(&list, 22);
	LInsert(&list, 33);

	printf("current count of data : %d \n", LCount(&list));

	if(LFirst(&list, &data))
	{	
		printf("%d ", data);

		while(LNext(&list, &data))
		{
			printf("%d ", data);
		}
	}	


	printf("\n\n");

	// Search 22 and Remove this number
	if(LFirst(&list, &data))
	{	
		if(data == 22)
			LRemove(&list);

		while(LNext(&list, &data))
		{
			if(data == 22)
				LRemove(&list);
		}
	}	

	printf("\n\n");


	//After delete num, total print
	printf("current count of data : %d \n", LCount(&list));

	if(LFirst(&list, &data))
	{	
		printf("%d ", data);

		while(LNext(&list, &data))
		{
			printf("%d ", data);
		}
	}	

	printf("\n\n");

	return 0;
}
