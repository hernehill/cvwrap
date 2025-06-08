cmake_minimum_required(VERSION 2.6)
project(cvwrap)

set(PROJECT_PATH ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT})
# set(CMAKE_INSTALL_PREFIX ${PROJECT_PATH})  # REZ is controlling it
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules)

add_subdirectory(src)

configure_file("${CMAKE_CURRENT_SOURCE_DIR}/module.txt" "${CMAKE_INSTALL_PREFIX}/${PROJECT_NAME}.mod")

install(DIRECTORY scripts DESTINATION .)
