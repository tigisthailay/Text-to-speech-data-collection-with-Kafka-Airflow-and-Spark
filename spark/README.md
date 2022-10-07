# Apache Spark
Spark is a unified analytics engine for large-scale data processing. It provides high-level APIs in Scala, Java, Python, and R, and an optimized engine that supports general computation graphs for data analysis. 
it is possiable to find the latest Spark documentation, including a programming guide, on the project web page. However,this README file only contains basic setup instructions.
# Building Spark
spark is built using Apache Maven. To build Spark and its example programs, run:

                ./build/mvn -DskipTests clean package
                (You do not need to do this if you downloaded a pre-built package.)

- More detailed documentation is available from the project site, at "Building Spark".
- For general development tips, including info on developing Spark using an IDE, see "Useful Developer Tools".
# Interactive Scala Shell
The easiest way to start using Spark is through the Scala shell:

          ./bin/spark-shell
Try the following command, which should return 1,000,000,000:

        scala> spark.range(1000 * 1000 * 1000).count()
# Running Tests
Testing first requires building Spark. Once Spark is built, tests can be run using:

          ./dev/run-tests
Please see the guidance on how to run tests for a module, or individual tests.
# Configuration
Please refer to the Configuration Guide in the online documentation for an overview on how to configure Spark.
