#ifndef __POST__CALCULATOR_H__
#define __POST__CALCULATOR_H__


/*
 * help function
 * getOpPriority : return priortiy
 * WhoPrecOp : return operator priortiy between op1 and op2
 */
int getOpPriority(char op);
int whoPrecOp(char op1, char op2);
//Infix Expression -> Post Expression
int infixExpToPostExp(char exp[]);

//Post Expression -> VALUE
int postExpToValue(char exp[]);

//Calculator controller
int calEngine(char exp[]);

#endif
