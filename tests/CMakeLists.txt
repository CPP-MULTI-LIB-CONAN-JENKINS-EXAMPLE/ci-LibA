
set(TEST_SOURCES
        test_main.cpp
        simple.cpp
        )

add_executable(testLibA ${TEST_SOURCES})

target_link_libraries(testLibA PUBLIC
        ${CONAN_PACKAGE_NAME}
        )

# conan weirdness ...
if (TARGET CONAN_PKG::GTest)
    target_link_libraries(testLibA PUBLIC CONAN_PKG::GTest)
else ()
    target_link_libraries(testLibA PUBLIC CONAN_PKG::gtest)
endif ()

if (WITH_COVERAGE)
    message("link gcov")
    target_link_libraries(testLibA PUBLIC gcov)
endif ()

target_include_directories(testLibA
        PRIVATE
        ${PROJECT_SOURCE_DIR}/include
        ${PROJECT_BINARY_DIR}/include
        ${PROJECT_BINARY_DIR}/src
        ${PROJECT_SOURCE_DIR}/src
        )

