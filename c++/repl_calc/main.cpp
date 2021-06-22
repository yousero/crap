#include <iostream>
#include <string>
using namespace std;
int main()
{
  string str;
  string operation;
  long double buff = 0;
  cout << "> ";
  while (cin >> str)
  {
    if (str == "exit")
    {
      break;
    }
    else if (str == "show")
    {
      cout << buff << endl;
    }
    else if (str == "clear")
    {
      buff = 0;
    }
    else
    {
      bool isnumber = true;
      bool dot = true;
      for (char c : str)
      {
        if (dot && c == '.')
        {
          dot = false;
          continue;
        }
        if (!isdigit(c))
        {
          isnumber = false;
          break;
        }
      }
      if (isnumber)
      {
        long double number = atof(str.c_str());
        if (operation == "plus")
        {
          buff += number;
        }
        else if (operation == "multiply")
        {
          buff *= number;
        }
        else if (operation == "minus")
        {
          buff -= number;
        }
        else if (operation == "divide")
        {
          buff /= number;
        }
        else
        {
          buff = number;
        }
        operation.clear();
      }
      else
      {
        operation = str;
      }
    }
    cout << "> ";
  }
  return 0;
}
