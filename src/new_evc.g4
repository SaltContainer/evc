grammar new_evc;


/*
 * Parser Rules
 */

/*
 * Program
 * Zero or more scripts
 */
prog                    : script* ;

/*
 * Script
 * A label and one or more instructions
 */
script                  : label instruction+ ;

/*
 * Instruction
 * A command and an argument list
 * Ex: _OBJ_DEL('NURSE'), _END(), _LDVAL(@SCWK_ANSWER, 1)
 */
instruction             : command argument_list ;

/*
 * Script label
 * A name and a colon
 * Ex: ev_dummy:, EV_DUMMY:, script_5:
 */
label                   : NAME ':' ;

/*
 * Argument list
 * An open parenthesis, optionally one or more arguments separated by commas, and a closed parenthesis
 * Ex: (), (@SCWK_PARAM1), (#3001, 6.4)
 */
argument_list           : '(' (argument (',' argument)*)? ')';

/*
 * Argument
 * A float, work, flag, system flag, or string
 */
argument                : float
                        | work
                        | flag
                        | sysflag
                        | string_ ;

/*
 * Commmand
 * A name
 * Ex: _OBJ_DEL, AC_WAIT, _ITEM_NAME
 */
command                 : NAME ;

/*
 * Float
 * A float value
 * Ex: 0, -9, -5.4, 1.3
 */
float                   : FLOAT ;

/*
 * Work
 * An at sign and either a name or a float value (NOTE: replace with just digits at some point?)
 * Ex: @SCWK_PARAM1, @LOCALWORK11, @400
 */
work                    : '@' (NAME | FLOAT) ;

/*
 * Flag
 * A hashtag and either a name or a float value (NOTE: replace with just digits at some point?)
 * Ex: #FH_14, #FV_R224_MAI, #1112
 */
flag                    : '#' (NAME | FLOAT) ;

/*
 * System flag
 * A cash sign and either a name or a float value (NOTE: replace with just digits at some point?)
 * Ex: $BADGE_ID_C03, $FIRST_SAVE, $654
 */
sysflag                 : '$' (NAME | FLOAT) ;

/*
 * String
 * A string value
 * Ex: '', 'string', 'another string'
 */
string_                 : STRING ;


/*
 * Lexer Rules
 */

/*
 * Name
 * A series of lowercase letters, uppercase letters, underscores, or digits, with the first one not being a digit
 * Ex: _OBJ_DEL, SCWK_PARAM1, _1_ON_1
 */
NAME                    : (UNDERSCORE | LOWERCASE | UPPERCASE) (UNDERSCORE | LOWERCASE | UPPERCASE | DIGIT)+ ;

/*
 * Float value
 * An optional hyphen, digits, and an optional decimal part (a period and digits)
 * Ex: 0, -9, -5.4, 1.3
 */
FLOAT                   : HYPHEN? DIGIT+ (PERIOD DIGIT+)? ;

/*
 * String value
 * A single quote, non-single quote characters, and a single quote
 * Ex: '', 'string', 'another string'
 */
STRING                  : SINGLE_QUOTE ~'\u0027'* SINGLE_QUOTE ;

/*
 * Comment
 * A semi-colon and non-line ending characters
 * Ex: ;, ;comment, ;another comment
 */
COMMENT                 : SEMICOLON ~[\r\n]* -> skip ;

/*
 * End of line
 * A new line character
 */
EOL                     : NEWLINE -> skip ;

/*
 * Whitespace
 * Skips whitespace
 */
WS                      : WHITESPACE -> skip ;

// Fragments
fragment DIGIT          : [0-9] ;

fragment ZERO           : '0' ;
fragment ONE            : '1' ;
fragment TWO            : '2' ;
fragment THREE          : '3' ;
fragment FOUR           : '4' ;
fragment FIVE           : '5' ;
fragment SIX            : '6' ;
fragment SEVEN          : '7' ;
fragment EIGHT          : '8' ;
fragment NINE           : '9' ;

fragment LOWERCASE      : [a-z] ;
fragment UPPERCASE      : [A-Z] ;

fragment A              : ('a' | 'A') ;
fragment B              : ('b' | 'B') ;
fragment C              : ('c' | 'C') ;
fragment D              : ('d' | 'D') ;
fragment E              : ('e' | 'E') ;
fragment F              : ('f' | 'F') ;
fragment G              : ('g' | 'G') ;
fragment H              : ('h' | 'H') ;
fragment I              : ('i' | 'I') ;
fragment J              : ('j' | 'J') ;
fragment K              : ('k' | 'K') ;
fragment L              : ('l' | 'L') ;
fragment M              : ('m' | 'M') ;
fragment N              : ('n' | 'N') ;
fragment O              : ('o' | 'O') ;
fragment P              : ('p' | 'P') ;
fragment Q              : ('q' | 'Q') ;
fragment R              : ('r' | 'R') ;
fragment S              : ('s' | 'S') ;
fragment T              : ('t' | 'T') ;
fragment U              : ('u' | 'U') ;
fragment V              : ('v' | 'V') ;
fragment W              : ('w' | 'W') ;
fragment X              : ('x' | 'X') ;
fragment Y              : ('y' | 'Y') ;
fragment Z              : ('z' | 'Z') ;

fragment WHITESPACE     : (' ' | '\t') ;
fragment NEWLINE        : ('\r'? '\n' | '\r')+ ;

fragment PERIOD         : '.' ;
fragment SEMICOLON      : ';' ;
fragment HYPHEN         : '-' ;
fragment SINGLE_QUOTE   : '\u0027' ;
fragment UNDERSCORE     : '_' ;
fragment ATSIGN         : '@' ;
fragment HASHTAG        : '#' ;
fragment CASH           : '$' ;