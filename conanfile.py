from conans import ConanFile, CMake, tools
import os

class DocoptConan(ConanFile):
    name = "docopt"
    version = "master"
    license = "MIT and Boost"
    url = "https://github.com/memsharded/conan-docopt.git"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/docopt/docopt.cpp.git")
        tools.replace_in_file("docopt.cpp/CMakeLists.txt", "include(GNUInstallDirs)", """include(GNUInstallDirs)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
""")

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake docopt.cpp %s' % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("docopt.h", "include", "docopt.cpp")
        self.copy("docopt_value.h", "include", "docopt.cpp")
        self.copy("docopt_util.h", "include", "docopt.cpp")
        self.copy("*docopt_s.lib", "lib", keep_path=False)
        self.copy("*docopt.lib", "lib", keep_path=False)   
        if self.options.shared:
            self.copy("*.dll", "bin", keep_path=False)
            self.copy("*.so", "lib", keep_path=False)
        else:
            self.copy("*.a", "lib", keep_path=False)
        
    def package_info(self):
        if self.options.shared:
            self.cpp_info.libs = ["docopt"]
        else:
            self.cpp_info.libs = ["docopt_s"]
        

