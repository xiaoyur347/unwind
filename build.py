#/usr/bin/env python

import os

source_dir = os.getcwd()


def get_cmake_path():
    sdk = os.environ["ANDROID_HOME"]
    cmake_version = "3.10.2.4988404"
    cmake_path = "{}/cmake/{}/bin/cmake".format(sdk, cmake_version)
    if os.path.exists(cmake_path):
        return cmake_path
    
    cmake_version = "3.6.4111459"
    cmake_path = "{}/cmake/{}/bin/cmake".format(sdk, cmake_version)
    if os.path.exists(cmake_path):
        return cmake_path

    cmake_version = "3.6.3155560"
    cmake_path = "{}/cmake/{}/bin/cmake".format(sdk, cmake_version)
    if os.path.exists(cmake_path):
        return cmake_path

    return "cmake"


def get_toolchain_file():
    ndk = os.environ["ANDROID_NDK_HOME"]
    return "-DCMAKE_TOOLCHAIN_FILE={}/build/cmake/android.toolchain.cmake".format(ndk)


def run_command(cmd):
    print(cmd)
    ret = os.system(cmd)
    if ret != 0:
        raise RuntimeError("run_command error")


def build_abi(abi):
    build_dir = "build/android-{}".format(abi)
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)
    os.chdir(build_dir)
    cmd = "{} {} {}".format(get_cmake_path(), get_toolchain_file(), source_dir)
    run_command("{} {} {}".format(get_cmake_path(), get_toolchain_file(), source_dir))
    run_command("make")


if __name__ == "__main__":
    build_abi("armeabi-v7a")
    build_abi("arm64-v8a")
    build_abi("x86")
    build_abi("x86_64")
