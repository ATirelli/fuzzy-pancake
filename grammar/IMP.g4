grammar IMP;

/* Rules to construct the parser */
program 	  : varlist ';' seq | varlist ';'  statement ;
varlist : intvarlist | boolvarlist | intvarlist ';' varlist | boolvarlist ';' varlist;
intvarlist 	  : 'int '     (VAR',')* VAR;
boolvarlist   : 'logical ' (VAR',')* VAR;
ifconstruct   : 'if' bexpr block 'else' block ;
expr  : bracket
      | expr div expr
	  | expr plus expr
      | var
      | int
	  ;

bexpr :	bracket
 	  | not bexpr
	  | expr greater expr
	  | bexpr and bexpr
	  | bool
	  ;
seq  : statement statement | statement seq ;
greater   : '>' ;
and       : '&&';
plus 	  : '+' ;
div 	  : '/' ;
not		  : '!' ;
bracket   : '(' expr ')' | '(' bexpr ')';
block	  : '{''}' | '{' seq '}' | '{' statement '}' ;
assigment : var '=' expr ';' | var '=' bexpr ';';
statement 	  : assigment | whileconstruct | ifconstruct;

whileconstruct 	  :	'while' bexpr  block ;
bool 	  : BVAL ;
var 	  : VAR ;
int 	  : AVAL ;

/* Rules to contruct the lexer */
fragment NUMBER     : [0-9]+ ;
fragment STRING 	: [a-z]+ ;
WS 			     	: [ \t\r\n]+ -> skip ;
BVAL                : 'true' | 'false' ;
VAR 				: STRING ;
AVAL 				: NUMBER ;
EQ  				: '=' ;
