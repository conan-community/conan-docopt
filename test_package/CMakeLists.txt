PROJECT(MyHello)
cmake_minimum_required(VERSION 3.1)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(CMAKE_CXX_STANDARD 11)

message("LIBS: ${CONAN_LIBS}")

ADD_EXECUTABLE(example example.cpp)
TARGET_LINK_LIBRARIES(example ${CONAN_LIBS})
