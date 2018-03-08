# conan-docopt

![conan-docopt image](/images/conan-docopt.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/docopt%3Aconan/images/download.svg)](https://bintray.com/conan-community/conan/docopt%3Aconan/_latestVersion)
[![Build status](https://ci.appveyor.com/api/projects/status/jyeh443gn0l0f3bi/branch/stable/0.6.2?svg=true)](https://ci.appveyor.com/project/memsharded/conan-docopt/branch/stable/0.6.2)

[Conan.io](https://conan.io) package for [docopt](https://bitbucket.org/docopt/docopt) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/conan-community/conan/docopt%3Aconan).

## For Users: Use this package

### Basic setup

    $ conan install docopt/0.6.2@conan/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    docopt/0.6.2@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)
