#include <stdio.h>
#include "DLinkedList.h"

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

	printf("current num of data: %d \n", LCount(&list));
	
	if(LFirst(&list, &data))
	{
		printf("%d ", data);

		while(LNext(&list, &data))
		{
			printf("%d ", data);
		}
	}

	printf("\n\n");

	//search 22 and remove 22 node
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
	
	//aftet remote node and check current data
	printf("current num of data: %d \n", LCount(&list));
	
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
