#include <string.h>
#include <ctype.h>
#include "../ListStack/ListBaseStack.h"

//return priortiy
int getOpPriority(char op)
{
	switch(op)
	{

	}
}

//return operator priority
int whoPrecOp(char op1, choar op2)
{

}

//Infix Expression->Post Expression
int infixExpToPostExp(char exp[])
{

}

//Post Expression -> VALUE
int postExpToValue(char exp[])
{
	Stack stack;
	int expLen = strlen(exp);
	int i;
	char numToken, op1, op2; 

	StackInit(&stack);

	for(i=0; i<expLen; i++)
	{
		numToken = exp[i];

		if(isdigit(numToken))
		{
			SPush(&stack, numToken - '0');
		}
		else
		{
			op1 = SPop(&stack);
			op2 = SPop(&stack);

			switch(numToken)
			{
				case '+':
					SPush(&stack, op1+op2);
					break;
				case '-':
					SPush(&stack, op1-op2);
					break;
				case '*':
					SPush(&stack, op1*op2);
					break;
				case '/':
					SPush(&stack, op1/op2);
					break;
			}
		}
	}
	
	return SPop(&stack);

}

int calEngine(char exp[])
{

}
