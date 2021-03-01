# Part 1:

## Step 1:
tutorial.cxx:

    // A simple program that computes the square root of a number
    #include <cmath>
    #include <iostream>
    #include <string>
    #include <TutorialConfig.h>

    int main(int argc, char* argv[])
    {
    if (argc < 2) {
        // report version
        std::cout << argv[0] << " Version " << Tutorial_VERSION_MAJOR << "."
                << Tutorial_VERSION_MINOR << std::endl;
        std::cout << "Usage: " << argv[0] << " number" << std::endl;
        return 1;
    }

    // convert input to double
    const double inputValue = atof(argv[1]);

    // calculate square root
    const double outputValue = sqrt(inputValue);
    std::cout << "The square root of " << inputValue << " is " << outputValue
                << std::endl;
    return 0;
    }

CMakeLists.txt:

    cmake_minimum_required(VERSION 3.10)

    project(Tutorial VERSION 1.0)

    set(CMAKE_CXX_STANDARD 11)
    set(CMAKE_CXX_STANDARD_REQUIRED True)

    configure_file(TutorialConfig.h.in TutorialConfig.h)

    add_executable(Tutorial tutorial.cxx)

    target_include_directories(Tutorial PUBLIC
                            "${PROJECT_BINARY_DIR}"
                            )

Tutorial Output:

![tut_output](tut.png)

<hr />

## Step 2:

tutorial.cxx:

    // A simple program that computes the square root of a number
    #include <cmath>
    #include <iostream>
    #include <string>

    #include "TutorialConfig.h"

    #ifdef USE_MYMATH
    #  include "MathFunctions.h"
    #endif

    int main(int argc, char* argv[])
    {
    if (argc < 2) {
        // report version
        std::cout << argv[0] << " Version " << Tutorial_VERSION_MAJOR << "."
                << Tutorial_VERSION_MINOR << std::endl;
        std::cout << "Usage: " << argv[0] << " number" << std::endl;
        return 1;
    }

    const double inputValue = std::stod(argv[1]);

    #ifdef USE_MYMATH
    const double outputValue = mysqrt(inputValue);
    #else
    const double outputValue = sqrt(inputValue);
    #endif

    std::cout << "The square root of " << inputValue << " is " << outputValue
                << std::endl;
    return 0;
    }

CMakeLists.txt:

    cmake_minimum_required(VERSION 3.10)

    project(Tutorial VERSION 1.0)

    set(CMAKE_CXX_STANDARD 11)
    set(CMAKE_CXX_STANDARD_REQUIRED True)

    option(USE_MYMATH "Use tutorial provided math implementation" ON)

    configure_file(TutorialConfig.h.in TutorialConfig.h)

    if(USE_MYMATH)
        add_subdirectory(MathFunctions)
        list(APPEND EXTRA_LIBS MathFunctions)
        list(APPEND EXTRA_INCLUDES "${PROJECT_SOURCE_DIR}/MathFunctions")
    endif()

    add_executable(Tutorial tutorial.cxx)

    target_link_libraries(Tutorial PUBLIC ${EXTRA_LIBS})

    target_include_directories(Tutorial PUBLIC
                            "${PROJECT_BINARY_DIR}"
                            ${EXTRA_INCLUDES}
                            )

Tutorial MyMath On:

![tut2_output](tut2.png)

Tutorial MyMath Off:

![tut3_output](tut3.png)

<hr />

## Step 3:

CMakeLists.txt:

    cmake_minimum_required(VERSION 3.10)

    # set the project name and version
    project(Tutorial VERSION 1.0)

    # specify the C++ standard
    set(CMAKE_CXX_STANDARD 11)
    set(CMAKE_CXX_STANDARD_REQUIRED True)

    # should we use our own math functions
    option(USE_MYMATH "Use tutorial provided math implementation" ON)

    # configure a header file to pass some of the CMake settings
    # to the source code
    configure_file(TutorialConfig.h.in TutorialConfig.h)

    if(USE_MYMATH)
        add_subdirectory(MathFunctions)
        list(APPEND EXTRA_LIBS MathFunctions)
    endif()

    # add the executable
    add_executable(Tutorial tutorial.cxx)

    target_link_libraries(Tutorial PUBLIC ${EXTRA_LIBS})

    target_include_directories(Tutorial PUBLIC
                            "${PROJECT_BINARY_DIR}"
                            )

MathFunctions/CMakeLists.txt:

    add_library(MathFunctions mysqrt.cxx)

    target_include_directories(MathFunctions
            INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
            )


Answers are the same as the previous step

Tutorial MyMath On:

![tut2_output](tut2.png)

Tutorial MyMath Off:

![tut3_output](tut3.png)


## Step 4:

CMakeLists.txt: 

    cmake_minimum_required(VERSION 3.10)

    project(Tutorial VERSION 1.0)

    set(CMAKE_CXX_STANDARD 11)
    set(CMAKE_CXX_STANDARD_REQUIRED True)

    option(USE_MYMATH "Use tutorial provided math implementation" ON)

    configure_file(TutorialConfig.h.in TutorialConfig.h)

    if(USE_MYMATH)
        add_subdirectory(MathFunctions)
        list(APPEND EXTRA_LIBS MathFunctions)
    endif()

    add_executable(Tutorial tutorial.cxx)
    target_link_libraries(Tutorial PUBLIC ${EXTRA_LIBS})

    target_include_directories(Tutorial PUBLIC
                            "${PROJECT_BINARY_DIR}"
                            )

    install(TARGETS Tutorial DESTINATION bin)
    install(FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"
    DESTINATION include
    )

    enable_testing()

    add_test(NAME Runs COMMAND Tutorial 25)

    add_test(NAME Usage COMMAND Tutorial)
    set_tests_properties(Usage
    PROPERTIES PASS_REGULAR_EXPRESSION "Usage:.*number"
    )

    function(do_test target arg result)
    add_test(NAME Comp${arg} COMMAND ${target} ${arg})
    set_tests_properties(Comp${arg}
        PROPERTIES PASS_REGULAR_EXPRESSION ${result}
        )
    endfunction(do_test)

    do_test(Tutorial 4 "4 is 2")
    do_test(Tutorial 9 "9 is 3")
    do_test(Tutorial 5 "5 is 2.236")
    do_test(Tutorial 7 "7 is 2.645")
    do_test(Tutorial 25 "25 is 5")
    do_test(Tutorial -25 "-25 is [-nan|nan|0]")
    do_test(Tutorial 0.0001 "0.0001 is 0.01")

MathFunctions/CMakeLists.txt:

    dd_library(MathFunctions mysqrt.cxx)
    target_include_directories(MathFunctions
            INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
            )

    install(TARGETS MathFunctions DESTINATION lib)
    install(FILES MathFunctions.h DESTINATION include)

ctest output:

![ctest](ctest.PNG)

## Step 5:

CMakeLists.txt:

    cmake_minimum_required(VERSION 3.10)

    project(Tutorial VERSION 1.0)

    set(CMAKE_CXX_STANDARD 11)
    set(CMAKE_CXX_STANDARD_REQUIRED True)

    option(USE_MYMATH "Use tutorial provided math implementation" ON)

    configure_file(TutorialConfig.h.in TutorialConfig.h)

    if(USE_MYMATH)
        add_subdirectory(MathFunctions)
        list(APPEND EXTRA_LIBS MathFunctions)
    endif()

    add_executable(Tutorial tutorial.cxx)
    target_link_libraries(Tutorial PUBLIC ${EXTRA_LIBS})

    target_include_directories(Tutorial PUBLIC
                            "${PROJECT_BINARY_DIR}"
                            )

    install(TARGETS Tutorial DESTINATION bin)
    install(FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"
    DESTINATION include
    )

    enable_testing()

    add_test(NAME Runs COMMAND Tutorial 25)

    add_test(NAME Usage COMMAND Tutorial)
    set_tests_properties(Usage
    PROPERTIES PASS_REGULAR_EXPRESSION "Usage:.*number"
    )

    function(do_test target arg result)
    add_test(NAME Comp${arg} COMMAND ${target} ${arg})
    set_tests_properties(Comp${arg}
        PROPERTIES PASS_REGULAR_EXPRESSION ${result}
        )
    endfunction(do_test)

    do_test(Tutorial 4 "4 is 2")
    do_test(Tutorial 9 "9 is 3")
    do_test(Tutorial 5 "5 is 2.236")
    do_test(Tutorial 7 "7 is 2.645")
    do_test(Tutorial 25 "25 is 5")
    do_test(Tutorial -25 "-25 is [-nan|nan|0]")
    do_test(Tutorial 0.0001 "0.0001 is 0.01")

MathFunctions/CMakeLists.txt:

    add_library(MathFunctions mysqrt.cxx)

    target_include_directories(MathFunctions
            INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
            )

    include(CheckSymbolExists)
    check_symbol_exists(log "math.h" HAVE_LOG)
    check_symbol_exists(exp "math.h" HAVE_EXP)
    if(NOT (HAVE_LOG AND HAVE_EXP))
    unset(HAVE_LOG CACHE)
    unset(HAVE_EXP CACHE)
    set(CMAKE_REQUIRED_LIBRARIES "m")
    check_symbol_exists(log "math.h" HAVE_LOG)
    check_symbol_exists(exp "math.h" HAVE_EXP)
    if(HAVE_LOG AND HAVE_EXP)
        target_link_libraries(MathFunctions PRIVATE m)
    endif()
    endif()

    if(HAVE_LOG AND HAVE_EXP)
    target_compile_definitions(MathFunctions
                                PRIVATE "HAVE_LOG" "HAVE_EXP")
    endif()

    install(TARGETS MathFunctions DESTINATION lib)
    install(FILES MathFunctions.h DESTINATION include)

Answers are the same as the previous step

Tutorial MyMath On:

![tut2_output](tut2.png)

Tutorial MyMath Off:

![tut3_output](tut3.png)

# Part Two

ls -la Output: (Dynamic Library is smaller!)

![lsla](ls-la.png)

Program Output:

![output](output.png)

CMakeLists.txt:

    cmake_minimum_required(VERSION 3.10)

    project(program)

    ADD_LIBRARY(static_block STATIC source/block.c)

    ADD_EXECUTABLE(program program.c) 

    TARGET_LINK_LIBRARIES(program static_block)

    project(dynamicprogram)

    ADD_LIBRARY(dynamic_block SHARED source/block.c)

    ADD_EXECUTABLE(dynamicprogram program.c)

    TARGET_LINK_LIBRARIES(dynamicprogram dynamic_block)

CMake Makefile:

    # CMAKE generated file: DO NOT EDIT!
    # Generated by "Unix Makefiles" Generator, CMake Version 3.16

    # Default target executed when no arguments are given to make.
    default_target: all

    .PHONY : default_target

    # Allow only one "make -f Makefile2" at a time, but pass parallelism.
    .NOTPARALLEL:


    #=============================================================================
    # Special targets provided by cmake.

    # Disable implicit rules so canonical targets will work.
    .SUFFIXES:


    # Remove some rules from gmake that .SUFFIXES does not remove.
    SUFFIXES =

    .SUFFIXES: .hpux_make_needs_suffix_list


    # Suppress display of executed commands.
    $(VERBOSE).SILENT:


    # A target that is always out of date.
    cmake_force:

    .PHONY : cmake_force

    #=============================================================================
    # Set environment variables for the build.

    # The shell in which to execute make rules.
    SHELL = /bin/sh

    # The CMake executable.
    CMAKE_COMMAND = /usr/bin/cmake

    # The command to remove a file.
    RM = /usr/bin/cmake -E remove -f

    # Escaping for special characters.
    EQUALS = =

    # The top-level source directory on which CMake was run.
    CMAKE_SOURCE_DIR = /home/na/repos/CSCI-4470-OpenSource/Modules/05.BuildSystems/Lab-BuildSystemsExample

    # The top-level build directory on which CMake was run.
    CMAKE_BINARY_DIR = /home/na/repos/CSCI-4470-OpenSource/Modules/05.BuildSystems/Lab-BuildSystemsExample/bu

    #=============================================================================
    # Targets provided globally by CMake.

    # Special rule for the target rebuild_cache
    rebuild_cache:
        @$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake to regenerate build system..."
        /usr/bin/cmake -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
    .PHONY : rebuild_cache

    # Special rule for the target rebuild_cache
    rebuild_cache/fast: rebuild_cache

    .PHONY : rebuild_cache/fast

    # Special rule for the target edit_cache
    edit_cache:
        @$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "No interactive CMake dialog available..."
        /usr/bin/cmake -E echo No\ interactive\ CMake\ dialog\ available.
    .PHONY : edit_cache

    # Special rule for the target edit_cache
    edit_cache/fast: edit_cache

    .PHONY : edit_cache/fast

    # The main all target
    all: cmake_check_build_system
        $(CMAKE_COMMAND) -E cmake_progress_start /home/na/repos/CSCI-4470-OpenSource/Modules/05.BuildSystems/Lab-BuildSystemsExample/bu/CMakeFiles /home/na/repos/CSCI-4470-OpenSource/Modules/05.BuildSystems/Lab-BuildSystemsExample/bu/CMakeFiles/progress.marks
        $(MAKE) -f CMakeFiles/Makefile2 all
        $(CMAKE_COMMAND) -E cmake_progress_start /home/na/repos/CSCI-4470-OpenSource/Modules/05.BuildSystems/Lab-BuildSystemsExample/bu/CMakeFiles 0
    .PHONY : all

    # The main clean target
    clean:
        $(MAKE) -f CMakeFiles/Makefile2 clean
    .PHONY : clean

    # The main clean target
    clean/fast: clean

    .PHONY : clean/fast

    # Prepare targets for installation.
    preinstall: all
        $(MAKE) -f CMakeFiles/Makefile2 preinstall
    .PHONY : preinstall

    # Prepare targets for installation.
    preinstall/fast:
        $(MAKE) -f CMakeFiles/Makefile2 preinstall
    .PHONY : preinstall/fast

    # clear depends
    depend:
        $(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 1
    .PHONY : depend

    #=============================================================================
    # Target rules for targets named dynamicprogram

    # Build rule for target.
    dynamicprogram: cmake_check_build_system
        $(MAKE) -f CMakeFiles/Makefile2 dynamicprogram
    .PHONY : dynamicprogram

    # fast build rule for target.
    dynamicprogram/fast:
        $(MAKE) -f CMakeFiles/dynamicprogram.dir/build.make CMakeFiles/dynamicprogram.dir/build
    .PHONY : dynamicprogram/fast

    #=============================================================================
    # Target rules for targets named program

    # Build rule for target.
    program: cmake_check_build_system
        $(MAKE) -f CMakeFiles/Makefile2 program
    .PHONY : program

    # fast build rule for target.
    program/fast:
        $(MAKE) -f CMakeFiles/program.dir/build.make CMakeFiles/program.dir/build
    .PHONY : program/fast

    #=============================================================================
    # Target rules for targets named dynamic_block

    # Build rule for target.
    dynamic_block: cmake_check_build_system
        $(MAKE) -f CMakeFiles/Makefile2 dynamic_block
    .PHONY : dynamic_block

    # fast build rule for target.
    dynamic_block/fast:
        $(MAKE) -f CMakeFiles/dynamic_block.dir/build.make CMakeFiles/dynamic_block.dir/build
    .PHONY : dynamic_block/fast

    #=============================================================================
    # Target rules for targets named static_block

    # Build rule for target.
    static_block: cmake_check_build_system
        $(MAKE) -f CMakeFiles/Makefile2 static_block
    .PHONY : static_block

    # fast build rule for target.
    static_block/fast:
        $(MAKE) -f CMakeFiles/static_block.dir/build.make CMakeFiles/static_block.dir/build
    .PHONY : static_block/fast

    program.o: program.c.o

    .PHONY : program.o

    # target to build an object file
    program.c.o:
        $(MAKE) -f CMakeFiles/dynamicprogram.dir/build.make CMakeFiles/dynamicprogram.dir/program.c.o
        $(MAKE) -f CMakeFiles/program.dir/build.make CMakeFiles/program.dir/program.c.o
    .PHONY : program.c.o

    program.i: program.c.i

    .PHONY : program.i

    # target to preprocess a source file
    program.c.i:
        $(MAKE) -f CMakeFiles/dynamicprogram.dir/build.make CMakeFiles/dynamicprogram.dir/program.c.i
        $(MAKE) -f CMakeFiles/program.dir/build.make CMakeFiles/program.dir/program.c.i
    .PHONY : program.c.i

    program.s: program.c.s

    .PHONY : program.s

    # target to generate assembly for a file
    program.c.s:
        $(MAKE) -f CMakeFiles/dynamicprogram.dir/build.make CMakeFiles/dynamicprogram.dir/program.c.s
        $(MAKE) -f CMakeFiles/program.dir/build.make CMakeFiles/program.dir/program.c.s
    .PHONY : program.c.s

    source/block.o: source/block.c.o

    .PHONY : source/block.o

    # target to build an object file
    source/block.c.o:
        $(MAKE) -f CMakeFiles/dynamic_block.dir/build.make CMakeFiles/dynamic_block.dir/source/block.c.o
        $(MAKE) -f CMakeFiles/static_block.dir/build.make CMakeFiles/static_block.dir/source/block.c.o
    .PHONY : source/block.c.o

    source/block.i: source/block.c.i

    .PHONY : source/block.i

    # target to preprocess a source file
    source/block.c.i:
        $(MAKE) -f CMakeFiles/dynamic_block.dir/build.make CMakeFiles/dynamic_block.dir/source/block.c.i
        $(MAKE) -f CMakeFiles/static_block.dir/build.make CMakeFiles/static_block.dir/source/block.c.i
    .PHONY : source/block.c.i

    source/block.s: source/block.c.s

    .PHONY : source/block.s

    # target to generate assembly for a file
    source/block.c.s:
        $(MAKE) -f CMakeFiles/dynamic_block.dir/build.make CMakeFiles/dynamic_block.dir/source/block.c.s
        $(MAKE) -f CMakeFiles/static_block.dir/build.make CMakeFiles/static_block.dir/source/block.c.s
    .PHONY : source/block.c.s

    # Help Target
    help:
        @echo "The following are some of the valid targets for this Makefile:"
        @echo "... all (the default if no target is provided)"
        @echo "... clean"
        @echo "... depend"
        @echo "... rebuild_cache"
        @echo "... edit_cache"
        @echo "... dynamicprogram"
        @echo "... program"
        @echo "... dynamic_block"
        @echo "... static_block"
        @echo "... program.o"
        @echo "... program.i"
        @echo "... program.s"
        @echo "... source/block.o"
        @echo "... source/block.i"
        @echo "... source/block.s"
    .PHONY : help



    #=============================================================================
    # Special targets to cleanup operation of make.

    # Special rule to run CMake to check the build system integrity.
    # No rule that depends on this can have commands that come from listfiles
    # because they might be regenerated.
    cmake_check_build_system:
        $(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 0
    .PHONY : cmake_check_build_system

My Makefile:

    all: dynamic_block static_block

    dynamic_block: program.c source/block.c
        gcc -c source/block.c
        gcc -shared block.o -o dynamic.so
        gcc program.c dynamic.so -o dynamic_block
        
    static_block: program.c source/block.c
        gcc program.c source/block.c -o static_block