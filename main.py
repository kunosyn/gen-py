__version__ = "0.0.1";

import os, sys;

class c:
    def out(x: str):
        print(x);
    
    def clr():
        os.system("clear");

    def warn(x: str):
        print(f"\u001b[33m* Warning: {x}\u001b[37m");
    
    def err(x: str):
        print(f"\u001b[31m* Error: {x}\u001b[37m")

class com:
    def exit(*x: str) -> None:
        if len(x) < 1:
            sys.exit(1);
        else:
            sys.exit(x[0]);
    
    def invoke(x: str, y) -> None:
        if type(y) is type:
            err = y(x);
            raise err from None;
        else:
            err = "Type of argument \"y\" must be an Error.";
            com.invoke(err, SyntaxError);