cmake_minimum_required(VERSION 3.8)
project(BMRPassive)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -std=c++11 -msse4.1 -pthread -maes -msse2 -mpclmul")

include_directories(OTExtnsion)
include_directories(util)

add_executable(BMRPassive
        OTExtnsion/basicSockets.cpp
        OTExtnsion/basicSockets.h
        OTExtnsion/BMR.cpp
        OTExtnsion/BMR.h
        OTExtnsion/BMR_BGW.cpp
        OTExtnsion/BMR_BGW.h
        OTExtnsion/BMR_BGW_aux.cpp
        OTExtnsion/BMR_BGW_aux.h
        OTExtnsion/BMR_BGW_Latincrypt.cpp
        OTExtnsion/BMR_BGW_Latincrypt.h
        OTExtnsion/main.cpp
        OTExtnsion/myDefs.h
        OTExtnsion/secCompMultiParty.cpp
        OTExtnsion/secCompMultiParty.h
        util/aes.h
        util/Config.h
        util/main_gf_funcs.cpp
        util/main_gf_funcs.h
        util/MatrixMeasurement.h
        util/socket.h
        util/TedKrovetzAesNiWrapperC.cpp
        util/TedKrovetzAesNiWrapperC.h)
