"""
For this prompt I chose question B.

Default parameters in Python can help programmers by providing an easy way to set default values
inside of functions. There are several reasons why a programmer might do this one of them being
that you can create functions with optional parameters. This way, users do not need to supply
all of the arguments required in order to use the function unless they want the extended functionality.

Another benefit is that default/keyword parameters prevent you from having to supply the function
with None/null values just to get to the parameter that you want. You will see this inside of languages
such as C++ and C inside of the windows.h library where you need to supply NULL/0/nullptr so that the function knows that you are wanting
to use the default value.

#include <windows.h>
#include <iostream>

int main()
{
    HANDLE h = CreateFile(
        "test.txt",    // name of the file
        GENERIC_WRITE, // open for writing
        0,             // sharing mode, none in this case
        0,             // use default security descriptor
        CREATE_ALWAYS, // overwrite if exists
        FILE_ATTRIBUTE_NORMAL,
        0 // no template file
    );
    if (h)
    {
        std::cout << "CreateFile() succeeded\n";
        CloseHandle(h);
    }
    else
    {
        std::cerr << "CreateFile() failed:" << GetLastError() << "\n";
    }
    return 0;
}

As you can see this is very confusing and requires the user to remember all of the arguments
for the function including the ones that they aren't even using.

I personally like Python's implementation of default values because they are supplied as keyword
arguments. You do not need to write extra code to check if the parameter is None and then set
the value which is the typical approach within other programming languages.
"""
