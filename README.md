# Ledger Ergo Application

This is a Ergo application for the Ledger devices.

## Prerequisite

Be sure to have your environment correctly set up (see [Getting Started](https://developers.ledger.com/docs/device-app/getting-started))
and [ledgerblue](https://pypi.org/project/ledgerblue/) and installed.

It is recommended to use [VSCode](https://code.visualstudio.com/) to build/test/load the application.

## Compilation

```bash
BOLOS_ENV=/opt/stax-ledger-sdk make DEBUG=1  # compile optionally with PRINTF
BOLOS_ENV=/opt/stax-ledger-sdk make load     # load the app on the Nano using ledgerblue
```

## Documentation

API documentation can be found in the [doc](doc/README.md) folder.

Ledger app developer documentation which can be generated with [doxygen](https://www.doxygen.nl)

```bash
doxygen .doxygen/Doxyfile
```

the process outputs HTML and LaTeX documentations in `doc/html` and `doc/latex` folders.

## Tests & Continuous Integration

The flow processed in [GitHub Actions](https://github.com/features/actions) is the following:

- Code formatting with [clang-format](http://clang.llvm.org/docs/ClangFormat.html)
- Compilation of the application for Ledger Nano S+ in [ledger-app-builder](https://github.com/LedgerHQ/ledger-app-builder)
- Unit tests of C functions with [cmocka](https://cmocka.org/) (see [unit-tests/](unit-tests/))
- Functional tests implemented with [Ragger](https://github.com/LedgerHQ/ragger) (see [tests/](tests/))
- Code coverage with [gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html)/[lcov](http://ltp.sourceforge.net/coverage/lcov.php)
  and upload to [codecov.io](https://about.codecov.io)
- Documentation generation with [doxygen](https://www.doxygen.nl)

It outputs 4 artifacts:

- `ergo-app-debug` within output files of the compilation process in debug mode
- `speculos-log` within APDU command/response when executing end-to-end tests
- `code-coverage` within HTML details of code coverage
- `documentation` within HTML auto-generated documentation
