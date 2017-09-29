#include <string.h>
#include <ctype.h>
#include "../ListStack/ListBaseStack.h"

//return priortiy
int getOpPriority(char op)
{
	switch(op)
	{
		case '*':
		case '/':
			return 5;
		case '+':
		case '-':
			return 3;
		case '(':
			return 1;
	}

	return -1;	// no regist operator
}

//return operator priority
int whoPrecOp(char op1, char op2)
{
	int op1Prec = getOpPriority(op1);
	int op2Prec = getOpPriority(op2);

	if(op1Prec > op2Prec)
		return 1;
	else if(op1Prec < op2Prec)
		return -1;
	else
		return 0;
}

//Infix Expression->Post Expression
int infixExpToPostExp(char exp[])
{
	Stack stack;
	int expLen = strlen(exp);
	char *convExp = (char*)malloc(expLen+1);

	int i, idx = 0;
	char tok, popOp;

	memset(convExp, 0, sizeof(char)*expLen+1);
	StackInit(&stack);

	for(i=0; i<expLen; i++)
	{
		tok = exp[i];

		if(isdigit(tok))	//if char token is digit
		{
			convExp[idx++] = tok;
		}
		else				// if char token is not digit, It's operator
		{					// Stack to stack
			switch(tok)
			{
				case '(':
					SPush(&stack, tok);
					break;
				case ')':
					while(1)
					{
						popOp = SPop(&stack);
						if(popOp == '(')
							break;
						convExp[idx++] = popOp;
					}
					break;
				case '+': case '-':
				case '*': case '/':
					while(!SIsEmpty(&stack) && whoPrecOp(SPeek(&stack), tok) >= 0)
						convExp[idx++] = SPop(&stack);
					
					SPush(&stack, tok);
					break;
			}
		}
	}

	while(!SIsEmpty(&stack))
		convExp[idx++] = SPop(&stack);
	
	strcpy(exp, convExp);
	free(convExp);
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
					//SPush(&stack, op1-op2);	//It's happen bug code. You have to think stack
					SPush(&stack, op2-op1);
					break;
				case '*':
					SPush(&stack, op1*op2);
					break;
				case '/':
					//SPush(&stack, op1/op2);
					SPush(&stack, op2/op1);
					break;
			}
		}
	}
	
	return SPop(&stack);

}

int calEngine(char exp[])
{
	int len = strlen(exp);
	int ret;
	char *expCpy = (char*)malloc(len+1);
	strcpy(expCpy, exp);

	infixExpToPostExp(expCpy);
	ret = postExpToValue(expCpy);

	free(expCpy);

	return ret;
}
