# Generated from c:/Users/naclc/source/repos/evc/src/new_evc.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,78,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,1,1,1,4,1,33,8,1,11,1,12,1,34,1,2,1,2,1,2,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,5,4,47,8,4,10,4,12,4,50,9,4,3,4,52,8,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,3,5,61,8,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,
        9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,
        16,18,20,22,0,1,1,0,8,9,73,0,27,1,0,0,0,2,30,1,0,0,0,4,36,1,0,0,
        0,6,39,1,0,0,0,8,42,1,0,0,0,10,60,1,0,0,0,12,62,1,0,0,0,14,64,1,
        0,0,0,16,66,1,0,0,0,18,69,1,0,0,0,20,72,1,0,0,0,22,75,1,0,0,0,24,
        26,3,2,1,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,
        0,28,1,1,0,0,0,29,27,1,0,0,0,30,32,3,6,3,0,31,33,3,4,2,0,32,31,1,
        0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,3,1,0,0,0,36,
        37,3,12,6,0,37,38,3,8,4,0,38,5,1,0,0,0,39,40,5,8,0,0,40,41,5,1,0,
        0,41,7,1,0,0,0,42,51,5,2,0,0,43,48,3,10,5,0,44,45,5,3,0,0,45,47,
        3,10,5,0,46,44,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,
        49,52,1,0,0,0,50,48,1,0,0,0,51,43,1,0,0,0,51,52,1,0,0,0,52,53,1,
        0,0,0,53,54,5,4,0,0,54,9,1,0,0,0,55,61,3,14,7,0,56,61,3,16,8,0,57,
        61,3,18,9,0,58,61,3,20,10,0,59,61,3,22,11,0,60,55,1,0,0,0,60,56,
        1,0,0,0,60,57,1,0,0,0,60,58,1,0,0,0,60,59,1,0,0,0,61,11,1,0,0,0,
        62,63,5,8,0,0,63,13,1,0,0,0,64,65,5,9,0,0,65,15,1,0,0,0,66,67,5,
        5,0,0,67,68,7,0,0,0,68,17,1,0,0,0,69,70,5,6,0,0,70,71,7,0,0,0,71,
        19,1,0,0,0,72,73,5,7,0,0,73,74,7,0,0,0,74,21,1,0,0,0,75,76,5,10,
        0,0,76,23,1,0,0,0,5,27,34,48,51,60
    ]

class new_evcParser ( Parser ):

    grammarFileName = "new_evc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'('", "','", "')'", "'@'", "'#'", 
                     "'$'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NAME", "FLOAT", "STRING", "COMMENT", "EOL", "WS" ]

    RULE_prog = 0
    RULE_script = 1
    RULE_instruction = 2
    RULE_label = 3
    RULE_argument_list = 4
    RULE_argument = 5
    RULE_command = 6
    RULE_float = 7
    RULE_work = 8
    RULE_flag = 9
    RULE_sysflag = 10
    RULE_string_ = 11

    ruleNames =  [ "prog", "script", "instruction", "label", "argument_list", 
                   "argument", "command", "float", "work", "flag", "sysflag", 
                   "string_" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NAME=8
    FLOAT=9
    STRING=10
    COMMENT=11
    EOL=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def script(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(new_evcParser.ScriptContext)
            else:
                return self.getTypedRuleContext(new_evcParser.ScriptContext,i)


        def getRuleIndex(self):
            return new_evcParser.RULE_prog




    def prog(self):

        localctx = new_evcParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 24
                self.script()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(new_evcParser.LabelContext,0)


        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(new_evcParser.InstructionContext)
            else:
                return self.getTypedRuleContext(new_evcParser.InstructionContext,i)


        def getRuleIndex(self):
            return new_evcParser.RULE_script




    def script(self):

        localctx = new_evcParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_script)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.label()
            self.state = 32 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 31
                    self.instruction()

                else:
                    raise NoViableAltException(self)
                self.state = 34 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(new_evcParser.CommandContext,0)


        def argument_list(self):
            return self.getTypedRuleContext(new_evcParser.Argument_listContext,0)


        def getRuleIndex(self):
            return new_evcParser.RULE_instruction




    def instruction(self):

        localctx = new_evcParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.command()
            self.state = 37
            self.argument_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(new_evcParser.NAME, 0)

        def getRuleIndex(self):
            return new_evcParser.RULE_label




    def label(self):

        localctx = new_evcParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(new_evcParser.NAME)
            self.state = 40
            self.match(new_evcParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(new_evcParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(new_evcParser.ArgumentContext,i)


        def getRuleIndex(self):
            return new_evcParser.RULE_argument_list




    def argument_list(self):

        localctx = new_evcParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(new_evcParser.T__1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1760) != 0):
                self.state = 43
                self.argument()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 44
                    self.match(new_evcParser.T__2)
                    self.state = 45
                    self.argument()
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 53
            self.match(new_evcParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def float_(self):
            return self.getTypedRuleContext(new_evcParser.FloatContext,0)


        def work(self):
            return self.getTypedRuleContext(new_evcParser.WorkContext,0)


        def flag(self):
            return self.getTypedRuleContext(new_evcParser.FlagContext,0)


        def sysflag(self):
            return self.getTypedRuleContext(new_evcParser.SysflagContext,0)


        def string_(self):
            return self.getTypedRuleContext(new_evcParser.String_Context,0)


        def getRuleIndex(self):
            return new_evcParser.RULE_argument




    def argument(self):

        localctx = new_evcParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argument)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.float_()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.work()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.flag()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.sysflag()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.string_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(new_evcParser.NAME, 0)

        def getRuleIndex(self):
            return new_evcParser.RULE_command




    def command(self):

        localctx = new_evcParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(new_evcParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(new_evcParser.FLOAT, 0)

        def getRuleIndex(self):
            return new_evcParser.RULE_float




    def float_(self):

        localctx = new_evcParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(new_evcParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WorkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(new_evcParser.NAME, 0)

        def FLOAT(self):
            return self.getToken(new_evcParser.FLOAT, 0)

        def getRuleIndex(self):
            return new_evcParser.RULE_work




    def work(self):

        localctx = new_evcParser.WorkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_work)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(new_evcParser.T__4)
            self.state = 67
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(new_evcParser.NAME, 0)

        def FLOAT(self):
            return self.getToken(new_evcParser.FLOAT, 0)

        def getRuleIndex(self):
            return new_evcParser.RULE_flag




    def flag(self):

        localctx = new_evcParser.FlagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_flag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(new_evcParser.T__5)
            self.state = 70
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SysflagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(new_evcParser.NAME, 0)

        def FLOAT(self):
            return self.getToken(new_evcParser.FLOAT, 0)

        def getRuleIndex(self):
            return new_evcParser.RULE_sysflag




    def sysflag(self):

        localctx = new_evcParser.SysflagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sysflag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(new_evcParser.T__6)
            self.state = 73
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(new_evcParser.STRING, 0)

        def getRuleIndex(self):
            return new_evcParser.RULE_string_




    def string_(self):

        localctx = new_evcParser.String_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_string_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(new_evcParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





