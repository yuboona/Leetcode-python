/cmake_minimum_required(VERSION 3.15)
project(tree)

set(CMAKE_CXX_STANDARD 14)

add_executable(tree src/main.cpp BST.cpp BST.h)