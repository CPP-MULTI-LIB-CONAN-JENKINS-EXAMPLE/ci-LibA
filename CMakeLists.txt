cmake_minimum_required(VERSION 3.9)

option(WITH_TESTS "Build Tests" ON)
option(WITH_COVERAGE "" ON)

# public header
set(LIB_HEADERS
        include/testproject/libA.h
        )

# rest of source code
set(LIB_SOURCES
        src/testproject/libA.cpp
        )

# conan is required hard, library name, version and description are configured from conan
if (EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
else ()
    message(FATAL_ERROR "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
endif ()

project(${CONAN_PACKAGE_NAME} VERSION ${CONAN_PACKAGE_VERSION})

conan_basic_setup(TARGETS)

if(WITH_COVERAGE)
    add_compile_options(-g -O0 -Wall -W -Wshadow -Wunused-variable -Wunused-parameter -Wunused-function -Wunused -Wno-system-headers -Wno-deprecated -Woverloaded-virtual -Wwrite-strings -fprofile-arcs -ftest-coverage)
    add_link_options(-fprofile-arcs -ftest-coverage)
endif()




add_library(${CONAN_PACKAGE_NAME} SHARED
        ${LIB_HEADERS}
        ${LIB_SOURCES}
        )

set_target_properties(${CONAN_PACKAGE_NAME} PROPERTIES VERSION ${CONAN_PACKAGE_VERSION})
set_target_properties(${CONAN_PACKAGE_NAME} PROPERTIES PUBLIC_HEADER ${LIB_HEADERS})

target_include_directories(${CONAN_PACKAGE_NAME} PRIVATE include)
target_include_directories(${CONAN_PACKAGE_NAME} PRIVATE src)

install(TARGETS ${CONAN_PACKAGE_NAME}
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

if (WITH_TESTS)
    add_subdirectory(tests)
endif ()

