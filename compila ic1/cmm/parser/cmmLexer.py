# Generated from /home/pizetta/Downloads/compila/cmm/parser/cmm.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2$")
        buf.write("\u00d6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\6\36\u00a6")
        buf.write("\n\36\r\36\16\36\u00a7\3\36\7\36\u00ab\n\36\f\36\16\36")
        buf.write("\u00ae\13\36\3\37\6\37\u00b1\n\37\r\37\16\37\u00b2\3 ")
        buf.write("\6 \u00b6\n \r \16 \u00b7\3 \3 \6 \u00bc\n \r \16 \u00bd")
        buf.write("\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5")
        buf.write("\"\u00ce\n\"\3#\6#\u00d1\n#\r#\16#\u00d2\3#\3#\2\2$\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$\3\2\6\4\2C\\")
        buf.write("c|\5\2\62;C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2\u00dc\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\3G\3\2\2\2\5K\3\2\2\2")
        buf.write("\7M\3\2\2\2\tO\3\2\2\2\13Q\3\2\2\2\rS\3\2\2\2\17U\3\2")
        buf.write("\2\2\21W\3\2\2\2\23Y\3\2\2\2\25_\3\2\2\2\27b\3\2\2\2\31")
        buf.write("h\3\2\2\2\33l\3\2\2\2\35s\3\2\2\2\37z\3\2\2\2!\177\3\2")
        buf.write("\2\2#\u0081\3\2\2\2%\u0083\3\2\2\2\'\u0085\3\2\2\2)\u0088")
        buf.write("\3\2\2\2+\u008b\3\2\2\2-\u008e\3\2\2\2/\u0091\3\2\2\2")
        buf.write("\61\u0093\3\2\2\2\63\u0095\3\2\2\2\65\u0097\3\2\2\2\67")
        buf.write("\u0099\3\2\2\29\u009f\3\2\2\2;\u00a5\3\2\2\2=\u00b0\3")
        buf.write("\2\2\2?\u00b5\3\2\2\2A\u00bf\3\2\2\2C\u00cd\3\2\2\2E\u00d0")
        buf.write("\3\2\2\2GH\7f\2\2HI\7g\2\2IJ\7h\2\2J\4\3\2\2\2KL\7*\2")
        buf.write("\2L\6\3\2\2\2MN\7+\2\2N\b\3\2\2\2OP\7.\2\2P\n\3\2\2\2")
        buf.write("QR\7}\2\2R\f\3\2\2\2ST\7\177\2\2T\16\3\2\2\2UV\7?\2\2")
        buf.write("V\20\3\2\2\2WX\7=\2\2X\22\3\2\2\2YZ\7r\2\2Z[\7t\2\2[\\")
        buf.write("\7k\2\2\\]\7p\2\2]^\7v\2\2^\24\3\2\2\2_`\7k\2\2`a\7h\2")
        buf.write("\2a\26\3\2\2\2bc\7y\2\2cd\7j\2\2de\7k\2\2ef\7n\2\2fg\7")
        buf.write("g\2\2g\30\3\2\2\2hi\7h\2\2ij\7q\2\2jk\7t\2\2k\32\3\2\2")
        buf.write("\2lm\7u\2\2mn\7y\2\2no\7k\2\2op\7v\2\2pq\7e\2\2qr\7j\2")
        buf.write("\2r\34\3\2\2\2st\7t\2\2tu\7g\2\2uv\7v\2\2vw\7w\2\2wx\7")
        buf.write("t\2\2xy\7p\2\2y\36\3\2\2\2z{\7e\2\2{|\7c\2\2|}\7u\2\2")
        buf.write("}~\7g\2\2~ \3\2\2\2\177\u0080\7<\2\2\u0080\"\3\2\2\2\u0081")
        buf.write("\u0082\7@\2\2\u0082$\3\2\2\2\u0083\u0084\7>\2\2\u0084")
        buf.write("&\3\2\2\2\u0085\u0086\7>\2\2\u0086\u0087\7?\2\2\u0087")
        buf.write("(\3\2\2\2\u0088\u0089\7@\2\2\u0089\u008a\7?\2\2\u008a")
        buf.write("*\3\2\2\2\u008b\u008c\7?\2\2\u008c\u008d\7?\2\2\u008d")
        buf.write(",\3\2\2\2\u008e\u008f\7#\2\2\u008f\u0090\7?\2\2\u0090")
        buf.write(".\3\2\2\2\u0091\u0092\7-\2\2\u0092\60\3\2\2\2\u0093\u0094")
        buf.write("\7/\2\2\u0094\62\3\2\2\2\u0095\u0096\7,\2\2\u0096\64\3")
        buf.write("\2\2\2\u0097\u0098\7\61\2\2\u0098\66\3\2\2\2\u0099\u009a")
        buf.write("\7k\2\2\u009a\u009b\7p\2\2\u009b\u009c\7r\2\2\u009c\u009d")
        buf.write("\7w\2\2\u009d\u009e\7v\2\2\u009e8\3\2\2\2\u009f\u00a0")
        buf.write("\7g\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2\7u\2\2\u00a2\u00a3")
        buf.write("\7g\2\2\u00a3:\3\2\2\2\u00a4\u00a6\t\2\2\2\u00a5\u00a4")
        buf.write("\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a8\u00ac\3\2\2\2\u00a9\u00ab\t\3\2\2")
        buf.write("\u00aa\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3")
        buf.write("\2\2\2\u00ac\u00ad\3\2\2\2\u00ad<\3\2\2\2\u00ae\u00ac")
        buf.write("\3\2\2\2\u00af\u00b1\t\4\2\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\u00b2\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3>\3\2\2\2\u00b4\u00b6\t\4\2\2\u00b5\u00b4\3\2\2")
        buf.write("\2\u00b6\u00b7\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8")
        buf.write("\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00bb\7\60\2\2\u00ba")
        buf.write("\u00bc\t\4\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be@\3\2\2")
        buf.write("\2\u00bf\u00c0\7P\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2\7")
        buf.write("p\2\2\u00c2\u00c3\7g\2\2\u00c3B\3\2\2\2\u00c4\u00c5\7")
        buf.write("V\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7w\2\2\u00c7\u00ce")
        buf.write("\7g\2\2\u00c8\u00c9\7H\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb")
        buf.write("\7n\2\2\u00cb\u00cc\7u\2\2\u00cc\u00ce\7g\2\2\u00cd\u00c4")
        buf.write("\3\2\2\2\u00cd\u00c8\3\2\2\2\u00ceD\3\2\2\2\u00cf\u00d1")
        buf.write("\t\5\2\2\u00d0\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\u00d5\b#\2\2\u00d5F\3\2\2\2\n\2\u00a7\u00ac\u00b2")
        buf.write("\u00b7\u00bd\u00cd\u00d2\3\b\2\2")
        return buf.getvalue()


class cmmLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    INPUT = 27
    ELSE = 28
    ID = 29
    INT = 30
    FLOAT = 31
    NULL = 32
    BOOLEAN = 33
    WS = 34

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'('", "')'", "','", "'{'", "'}'", "'='", "';'", "'print'", 
            "'if'", "'while'", "'for'", "'switch'", "'return'", "'case'", 
            "':'", "'>'", "'<'", "'<='", "'>='", "'=='", "'!='", "'+'", 
            "'-'", "'*'", "'/'", "'input'", "'else'", "'None'" ]

    symbolicNames = [ "<INVALID>",
            "INPUT", "ELSE", "ID", "INT", "FLOAT", "NULL", "BOOLEAN", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "INPUT", "ELSE", "ID", "INT", "FLOAT", "NULL", "BOOLEAN", 
                  "WS" ]

    grammarFileName = "cmm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


