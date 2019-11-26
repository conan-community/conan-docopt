from conans import ConanFile

class DocoptConan(ConanFile):
    name = "docopt"
    version = "0.6.2"
    description = "docopt helps you create most beautiful command-line interfaces easily"
    license = "MIT and Boost"
    url = "https://github.com/conan-community/conan-docopt"
    homepage = "https://github.com/docopt/docopt.cpp"
    alias = "docopt/0.6.2"

    def configure(self):
        self.output.warn("[DEPRECATED] Package docopt/0.6.2@conan/stable is being deprecated. Change yours to require docopt/0.6.2 instead")
