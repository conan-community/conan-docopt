from conans import ConanFile, CMake
import os


class DocoptTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch", "cppstd"
    generators = "cmake"

    def configure(self):
        if not self.settings.cppstd:
            if self.settings.os == "Windows":
                self.settings.cppstd = 11
            else:
                self.settings.cppstd = "gnu11"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy(pattern="*.dll", src="bin", dst="bin")
        self.copy(pattern="*.dylib", src="lib", dst="bin")

    def test(self):
        bin_path = os.path.join("bin", "example")
        self.run(bin_path + " --help")
