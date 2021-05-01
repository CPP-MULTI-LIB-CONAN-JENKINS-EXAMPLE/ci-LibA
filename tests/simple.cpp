/* **********************************************************************************
Copyright (c) 2020 Frieder Pankratz
*************************************************************************************/

#include <gtest/gtest.h>
#include <testproject/libA.h>

TEST(LibTests, SimpleTest) {
  ASSERT_EQ(testproject::libAFunction(1), 2);
  ASSERT_EQ(testproject::libAFunction(2), 3);
  ASSERT_EQ(testproject::libAFunction(3), 4);

  ASSERT_EQ(testproject::libAFunction(11), 10);
  ASSERT_EQ(testproject::libAFunction(12), 11);
  ASSERT_EQ(testproject::libAFunction(13), 12);
}
