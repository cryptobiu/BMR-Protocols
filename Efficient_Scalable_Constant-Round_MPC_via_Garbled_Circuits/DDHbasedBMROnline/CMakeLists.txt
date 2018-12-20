cmake_minimum_required(VERSION 2.8)
project(NTLWrapper)

include_directories($ENV{HOME}/ntl-9.10.0/include)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -msse4.2 -maes -O3")

set(SOURCE_FILES main.cpp NTLWrapper.cpp ZZPrecomputeExp.cpp ZZPrecomputeExp_Sec.cpp MPZPrecomputeExp.cpp
        MPZPrecomputeExp_Sec.cpp  secCompMultiParty.cpp homBMR.cpp )

add_executable(HomOnlineTest.out ${SOURCE_FILES})


target_link_libraries(HomOnlineTest.out $ENV{HOME}/ntl-9.10.0/src/ntl.a gmp crypto)
