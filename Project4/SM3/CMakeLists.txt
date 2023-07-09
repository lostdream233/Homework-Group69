cmake_minimum_required(VERSION 3.25)
project(SM3)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O2")

add_executable(SM3 main.cpp SM3.cpp SM3.h)
