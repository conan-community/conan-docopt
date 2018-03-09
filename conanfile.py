from conans import ConanFile, CMake, tools
import os

class DocoptConan(ConanFile):
    name = "docopt"
    version = "0.6.2"
    description = "docopt helps you create most beautiful command-line interfaces easily"
    license = "MIT and Boost"
    url = "https://github.com/conan-community/conan-docopt"
    homepage = "https://github.com/docopt/docopt.cpp"
    settings = "os", "compiler", "build_type", "arch", "cppstd"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        tools.get("%s/archive/v%s.zip" % (self.homepage, self.version))
        os.rename("docopt.cpp-%s" % self.version, "sources")
        tools.replace_in_file("sources/CMakeLists.txt", "include(GNUInstallDirs)", """include(GNUInstallDirs)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
""")

    def configure(self):
        if self.settings.cppstd == 98 or self.settings.cppstd == "gnu98":
            raise "docopt needs C++11 at least"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="sources")
        cmake.build()

    def package(self):
        self.copy("docopt.h", src="sources", dst="include")
        self.copy("docopt_value.h", src="sources", dst="include")
        self.copy("docopt_util.h", src="sources", dst="include")

        if self.options.shared:
            self.copy("*docopt.lib", dst="lib", keep_path=False) # Windows
            self.copy("*docopt.dll", dst="bin", keep_path=False) # Windows
            self.copy("*docopt.dll.a", dst="lib", keep_path=False) # Windows MinGW
            self.copy("*docopt.so", dst="lib", keep_path=False) # Linux
            self.copy("*docopt.dylib", dst="lib", keep_path=False) # Macos
        else:
            self.copy("*docopt_s.lib", dst="lib", keep_path=False) # Windows
            self.copy("*docopt.a", dst="lib", keep_path=False) # Linux & Windows MinGW
            self.copy("*docopt_s.a", dst="lib", keep_path=False) # Macos

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if self.settings.compiler == "Visual Studio" and self.options.shared:
            self.cpp_info.defines = ["DOCOPT_DLL"]
