import os
from conans import ConanFile, CMake, tools

class DocoptConan(ConanFile):
    name = "docopt"
    version = "0.6.2"
    description = "docopt helps you create most beautiful command-line interfaces easily"
    license = "MIT and Boost"
    url = "https://github.com/conan-community/conan-docopt"
    homepage = "https://github.com/docopt/docopt.cpp"
    settings = "os", "compiler", "build_type", "arch"
    exports = "LICENSE"
    options = {"shared": [True, False],
               "use_boost_regex": [True, False]}
    default_options = "shared=False", "use_boost_regex=False"
    generators = "cmake"

    @property
    def source_subfolder(self):
        return "sources"

    def configure(self):
        if (self.settings.compiler == "Visual Studio" and
                self.settings.compiler.version in ["8", "9", "10", "11", "12"]):
            raise Exception("Visual Studio %s is not able to compile C++11, not supported" %
                            self.settings.compiler.version)

    def requirements(self):
        if self.options.use_boost_regex:
            self.requires("boost/1.66.0@conan/stable")

    def source(self):
        tools.get("%s/archive/v%s.zip" % (self.homepage, self.version))
        os.rename("docopt.cpp-%s" % self.version, self.source_subfolder)
        tools.replace_in_file("%s/CMakeLists.txt" % self.source_subfolder,
                              "include(GNUInstallDirs)",
                              """include(GNUInstallDirs)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
""")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["USE_BOOST_REGEX"] = self.options.use_boost_regex
        cmake.configure(source_folder=self.source_subfolder)
        cmake.build()

    def package(self):
        self.copy("*LICENSE*", src=self.source_subfolder, dst="licenses")
        self.copy("docopt.h", src=self.source_subfolder, dst="include")
        self.copy("docopt_value.h", src=self.source_subfolder, dst="include")
        self.copy("docopt_util.h", src=self.source_subfolder, dst="include")

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
