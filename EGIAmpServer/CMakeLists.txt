cmake_minimum_required(VERSION 3.5)
project(EGIAmpServer
	LANGUAGES CXX
	VERSION 1.13.0)
include(Findliblsl.cmake)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
find_package(Qt5 REQUIRED COMPONENTS Widgets)
cmake_policy(SET CMP0074 NEW)  # <- Required to avoid conflict between BOOST_ROOT and Boost_ROOT
find_package(Boost REQUIRED)
find_package(Threads REQUIRED)

add_executable(${PROJECT_NAME} MACOSX_BUNDLE WIN32
	main.cpp
	EGIAmpWindow.cpp
	EGIAmpWindow.h
	EGIAmpWindow.ui
)
target_link_libraries(${PROJECT_NAME}
	PRIVATE
	Qt5::Widgets
	Threads::Threads
	LSL::lsl
	Boost::boost
)
message(STATUS ${Boost_VERSION})
if(Boost_VERSION LESS 106900)
	find_package(Boost COMPONENTS system REQUIRED)
	target_link_libraries(${PROJECT_NAME} PRIVATE Boost::system)
endif()

set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 14)
target_compile_definitions(${PROJECT_NAME} PRIVATE BOOST BOOST_DATE_TIME_NO_LIB BOOST_REGEX_NO_LIB)

installLSLApp(${PROJECT_NAME})
installLSLAuxFiles(${PROJECT_NAME}
	ampserver_config.cfg
)
LSLGenerateCPackConfig()
