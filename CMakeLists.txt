cmake_minimum_required (VERSION 2.6)
project (Demo)

add_executable(demo main.cpp)

ENABLE_TESTING()

add_test(NAME test_sr_100 COMMAND ./demo 100)
set_tests_properties (test_sr_100 PROPERTIES PASS_REGULAR_EXPRESSION "100 is 10")

add_test(NAME test_sr_25 COMMAND ./demo 25)
set_tests_properties (test_sr_25 PROPERTIES PASS_REGULAR_EXPRESSION "25 is 6")
