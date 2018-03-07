from conans import ConanFile, CMake, tools
import os

class DocoptConan(ConanFile):
    name = "docopt"
    version = "0.6.2"
    license = "MIT and Boost"
    url = "https://github.com/docopt/docopt.cpp"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        # https://github.com/docopt/docopt.cpp/archive/v0.6.2.zip
        tools.get("%s/archive/v%s.zip" % (self.url, self.version))
        os.rename("docopt.cpp-%s" % self.version, "sources")
        tools.replace_in_file("sources/CMakeLists.txt", "include(GNUInstallDirs)", """include(GNUInstallDirs)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
""")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="sources")
        cmake.build()

    def package(self):
        self.copy("docopt.h", "include", "sources")
        self.copy("docopt_value.h", "include", "sources")
        self.copy("docopt_util.h", "include", "sources")
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
