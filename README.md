# ANTLR-TimpPy
Repository containing the Python3 code for a parser of the TIMP language, generated using ANTLR4. TIMP is a very simple yet Turing-complete imperative language and it is often use as a benchmark example in Sofware Verification and Language Design, see for example the [Software Foundations](https://softwarefoundations.cis.upenn.edu/lf-current/Imp.html) book by Benjamin Pierce et al.

## Parser generation
To generate the parser you need to run the following command

`
cd grammar`
\
`
antlr -Dlanguage=Python3 -visitor IMP.g4 -o ../src/IMPUtils
`

## Examples
To run the parser on one of the examples just type the following code inside the root directory of the repo

`
python src/main.py < examples/e3.imp
`

