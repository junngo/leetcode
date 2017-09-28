/*
 * start date : 26.9.2017
 * desc : It's list stack
 */

#include <stdio.h>
#include <stdlib.h>
#include "ListBaseStack.h"

void StackInit(Stack *pstack)
{
	pstack->head = NULL;
}

int SIsEmpty(Stack *pstack)
{
	if(pstack->head == NULL)
		return TRUE;
	else
		return FALSE;
}

void SPush(Stack *pstack, Data data)
{
	Node *newNode = (Node*)malloc(sizeof(Node));

	newNode->data = data;
	newNode->next = pstack->head;
	
	pstack->head = newNode;
}

Data SPop(Stack *pstack)
{
	Data tempData;
	Node *tempNode;

	if(SIsEmpty(pstack))
	{
		printf("Stack is empty\n");
		exit(-1);
	}
	
	tempData = pstack->head->data;
	tempNode = pstack->head;

	pstack->head = pstack->head->next;
	free(tempNode);

	return tempData;
}

Data SPeek(Stack *pstack)
{
	if(SIsEmpty(pstack))
	{
		printf("Stack is empty\n");
		exit(-1);
	}

	return pstack->head->data;
}
