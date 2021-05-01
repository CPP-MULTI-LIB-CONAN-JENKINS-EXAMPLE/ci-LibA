import os
from conans import ConanFile, CMake, tools


class LibA(ConanFile):
    name = "LibA"
    version = "0.0.2"
    default_user = "testuser"
    default_channel = "stable"

    description = "LibA Test library for ci testing, no dependencies"
    url = "https://github.com/CPP-MULTI-LIB-CONAN-JENKINS-EXAMPLE/ci-LibA.git"
    license = "MIT"
    author = "Frieder Pankratz"

    short_paths = True

    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    compiler = "cppstd"
    options = {
        "shared": [True, False],
        "with_tests": [True, False]
    }

    default_options = {
        "shared": True,
        "with_tests" : True
    }

    
    exports_sources = "include/*","src/*","tests/*", "CMakeLists.txt"

    def requirements(self):
        if self.options.with_tests:
            self.requires("gtest/1.10.0")


    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.verbose = True

        def add_cmake_option(option, value):
            var_name = "{}".format(option).upper()
            value_str = "{}".format(value)
            var_value = "ON" if value_str == 'True' else "OFF" if value_str == 'False' else value_str
            cmake.definitions[var_name] = var_value

        for option, value in self.options.items():
            add_cmake_option(option, value)

        cmake.configure()
        return cmake

    def configure(self):
        pass

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

