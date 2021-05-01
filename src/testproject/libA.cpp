/* **********************************************************************************
Copyright (c) 2020 Frieder Pankratz
*************************************************************************************/

#include <testproject/libA.h>

int testproject::libAFunction(int i) {
  if (i <= 10)
    return i + 4;
  else
    return i - 1;
}
