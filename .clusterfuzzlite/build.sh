#!/bin/bash -eu

# build fuzzers

pushd tests/fuzzing
cmake -DBOLOS_SDK=../../BOLOS_SDK -Bbuild -H.
make -C build
mv ./build/*_harness "${OUT}"
popd
