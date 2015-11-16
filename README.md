# xd-demo
Demonstration of using XD for stellar classification.  Please have a look at the ipython notebook.

# Build and Dependencies
The Cython extensions built here depend on <a href="http://www.gnu.org/software/gsl/">GSL</a> and <a href="https://github.com/twiecki/CythonGSL">CythonGSL.</a>

To build the extension:
`python setup.py build_ext --inplace`

Also, this demo uses numpy, scikit-learn, matplotlib, pyfits, and a plotting routine from astroML.  I recommend installing using pip and/or anaconda.

# License
Copyright 2015 Ross Fadely.  Software is free to use under the MIT License. For details see the LICENSE file.
