 [![b0ri5](https://circleci.com/gh/b0ri5/solvents.svg?style=shield)](https://circleci.com/gh/b0ri5/solvents)

**A repository for learning about problems.**

The idea is to make it easy to casually do
  * [project euler](http://projecteuler.net),
  * [codejam](https://code.google.com/codejam), 
  * [topcoder](http://www.topcoder.com), 
  * problems from books???
or other problems while learning new languages and beating each other up in code reviews.

## Setup ##

The code reporistory is hosted on github at https://github.com/b0ri5/solvents.

There are samples for each language located in the [samples](samples) directory.

The code is checked for style/lint and passing tests via [travis-ci](https://travis-ci.org/b0ri5/solvents).

## Adding a solution ##

Here's how to do it exclusively via the github web interface.

1. Pick a problem. For example, the first project euler problem: http://projecteuler.net/problem=1
2. Create a new branch [via the github interface](https://github.com/blog/1377-create-and-delete-branches) called, say `b0ri5-euler-1`
3. [Create a new file](https://github.com/blog/1327-creating-files-on-github) for whatever solution you'd like to add, say `projecteuler/0001/sum_divisors.js` (unsure if this is okay to be used as a package name for java or go but lets go with it).
4. Write the solution in the github web editor
5. Commit the file the branch (at the bottom of the editor)
5. Write the test `projecteuler/0001/sum_divisors_test.js` and commit that as well
6. You should then be able to check [travis-ci](https://travis-ci.org/b0ri5/solvents) to see if it's started trying to build your newly added solution. It should complain if there are any lint or tests that don't pass.
7. [Create a pull request](https://help.github.com/articles/creating-a-pull-request) to merge the branch into master.
8. Bug someone to review the code (assigning should probably work)
9. Once you get the "Looks good to me" or "LGTM" and travis-ci reports a passing build, merge it into master and delete the remote branch.

And here's how to do it via commandline.

TODO(b0ri5): Add instructions on how to work on stuff from the commandline.

## Language support ##

* C++
  * version 3.5 with c++11
  * built by [clang](http://clang.llvm.org)
  * tested with [gtest](https://code.google.com/p/googletest/)
  * checked by [clang-format](http://clang.llvm.org/docs/ClangFormat.html). TODO(b0ri5): Check with [clang-modernize](http://clang.llvm.org/extra/clang-modernize.html) and [cpplint](http://google-styleguide.googlecode.com/svn/trunk/cpplint/cpplint.py)
* Go
  * built and tested by [go tool](http://golang.org/cmd/go/)
  * checked by [gofmt](http://golang.org/cmd/gofmt/) and [go vet](http://godoc.org/code.google.com/p/go.tools/cmd/vet)
* Haskell
  * TODO(b0ri5): Learn how to do a code+test only setup with haskell on travis-ci. Bug @negativek about this.
* Java
  * version 1.7
  * built by [gradle](http://www.gradle.org/).
  * tested with [junit4](http://junit.org/)
  * TODO(b0ri5): Check style with [checkstyle](http://checkstyle.sourceforge.net/)
* Javascript
  * run by [nodejs](http://nodejs.org/)
  * tested with [mocha](http://visionmedia.github.io/mocha/)
  * checked by [gjslint](https://developers.google.com/closure/utilities)
  * TODO(b0ri5): When we have enough js code, evaluate jshint.
* Python
  * version 3.3
  * tested with [unittest](http://docs.python.org/3.3/library/unittest.html) run via [nose](http://nose.readthedocs.org/en/latest/)
  * checked by [pylint](http://www.pylint.org/)


