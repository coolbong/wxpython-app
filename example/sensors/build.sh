#!/bin/bash

MPTEST=mptest
MPTEST_I=${MPTEST}.i
MPTEST_WRAP_C=${MPTEST}_wrap.c
MPTEST_WRAP_O=${MPTEST}_wrap.o
MPTEST_SO=_${MPTEST}.so

LDFLAGS=-lrt
LIBS=sensors.lib
#LIBS=sensors.so


function print_var {
    echo "- mptest: ${MPTEST}"
    echo "- interface: ${MPTEST_I}"
    echo "- wrap.c: ${MPTEST_WRAP_C}"
    echo "- so: ${MPTEST_SO}"
}

function usage {
    echo ""
    echo "usage "
    echo "build : build.sh"
    echo "clean : build.sh clean"
    echo ""
}

function clean {
    rm -f ${MPTEST_WRAP_C}
    rm -f ${MPTEST_WRAP_O}
    rm -f ${MPTEST_SO}
    rm -f ${MPTEST}.py
}

function build_interface {
    echo "build_interface"
    swig -python ${MPTEST_I}
}

function build_wrap_c {
    echo "build_wrap_c"
    gcc -w -O2 -fPIC -c ${MPTEST_WRAP_C} -I/usr/include/python2.7
}

function build_so {
    g++ -shared ${MPTEST_WRAP_O} ${LIBS} ${LDFLAGS} -o ${MPTEST_SO}
}


##
print_var

if [ $# == 0 ]; then 
    build_interface
    build_wrap_c
    build_so
elif [ $# == 1 ]; then 
    if [ $1 == clean ]; then
        clean
    else
        usage
    fi
else 
    usage
fi

