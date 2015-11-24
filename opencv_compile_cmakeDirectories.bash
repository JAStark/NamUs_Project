$ cmake -D CMAKE_BUILD_TYPE=RELEASE  \                                                                 #Indicates we're building release binary of OpenCV
  -D CMAKE_INSTALL_PREFIX=/usr/local \                                                                 #Base directory where OpenCV will be installed
	-D PYTHON2_PACKAGES_PATH=~/.virtualenvs/cv/lib/python2.7/site-packages \                             #Explicit path to where site-packages lives in cv venv
	-D PYTHON2_LIBRARY=/usr/local/Cellar/python/2.7.10/Frameworks/Python.framework/Versions/2.7/bin \    #Path to installation of python
	-D PYTHON2_INCLUDE_DIR=/usr/local/Frameworks/Python.framework/Headers \                              #Path to Python header files for compilation
	-D INSTALL_C_EXAMPLES=ON \                                                                           #Indicate we want to install C/C++ examples after compilation
  -D INSTALL_PYTHON_EXAMPLES=ON \                                                                      #Indicate we want to install Python examples after compilation
	-D BUILD_EXAMPLES=ON \                                                                               #Flag determines we want to include OpenCV examples compiled
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules ..                                             #Path to opencv_contrib repo - we want compiled too.


  $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
  	-D CMAKE_INSTALL_PREFIX=/Users/jenniferstark \
  	-D PYTHON3_PACKAGES_PATH=~/anaconda/lib/python3.4/site-packages \
  	-D PYTHON3_LIBRARY=~/anaconda/lib/libpython3.4m.dylib \
  	-D PYTHON3_INCLUDE_DIR=~/anaconda/include/python3.4m \
  	-D INSTALL_C_EXAMPLES=ON \
  	-D INSTALL_PYTHON_EXAMPLES=ON \
  	-D BUILD_EXAMPLES=ON \
  	-D BUILD_opencv_python3=ON \
  	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules ..

#This one below is what I ran for current installation
    $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/Users/jenniferstark \
      -D PYTHON3_PACKAGES_PATH=/Users/jenniferstark/anaconda/lib/python3.4/site-packages \
      -D PYTHON3_LIBRARY=/Users/jenniferstark/anaconda/lib/libpython3.4m.dylib \
      -D PYTHON3_INCLUDE_DIR=/Users/jenniferstark/anaconda/include/python3.4m \
      -D INSTALL_C_EXAMPLES=ON \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D BUILD_EXAMPLES=ON \
      -D BUILD_opencv_python3=ON \
      -D OPENCV_EXTRA_MODULES_PATH=/Users/jenniferstark/opencv_contrib/modules ..

#OpenCV website installation tutorial:
      $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/Users/jenniferstark \
        -D PYTHON3_PACKAGES_PATH=/Users/jenniferstark/anaconda/lib/python3.4/site-packages \
        -D PYTHON3_LIBRARY=/Users/jenniferstark/anaconda/lib/libpython3.4m.so \   #this line is different from PyImage tutorial
        -D PYTHON3_INCLUDE_DIR=/Users/jenniferstark/anaconda/include/python3.4m \
        -D INSTALL_C_EXAMPLES=ON \
        -D INSTALL_PYTHON_EXAMPLES=ON \
        -D BUILD_EXAMPLES=ON \
        -D BUILD_opencv_python3=ON \
        -D OPENCV_EXTRA_MODULES_PATH=/Users/jenniferstark/opencv_contrib/modules ..
