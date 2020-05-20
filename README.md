# imNet: a Sequence Network Construction Toolkit

`imNet` is a software package for the generation and analysis of large-scale immunological and biological sequence networks. Used together with Apache Spark running on a computer cluster, `imNet` can be used to analyze network properties from samples of hundreds of thousands or even millions of sequences in a reasonable amount of time. 

## Installation from source

Make sure you have all the dependencies installed -- see [Dependencies](#dependencies) below. 

Clone the repository and install: 

```
$ git clone https://github.com/aihealthlab/imnet.git
$ pip install ./imnet
```

If you make changes to the cython code, you will need `cython` and a usable C compiler. 

## Dependencies

### basic python libraries

These should all be installable via `pip` or `conda`:
* click 
* python-Levenshtein 
* scipy 
* networkx 
* pandas
* cython (optional)

## Basic usage

Refer to the command-line help for usage: 

```
$ imnet-analyze --help
Usage: imnet-analyze [OPTIONS] COMMAND [ARGS]...

Options:
  --spark-config TEXT         Spark configuration directory
  --spark-master TEXT         Spark master
  --kind [graph|degrees|all]  Which kind of output to produce
  --outdir TEXT               Output directory
  --min-ld INTEGER            Minimum Levenshtein distance
  --max-ld INTEGER            Maximum Levenshtein distance
  --help                      Show this message and exit.

Commands:
  benchmark  Run a series of benchmarks for graph and...
  directory  Process a directory of CDR3 string files
  file       Process an individual file with CDR3 strings...
  random     Run analysis on a randomly generated set of...

$ imnet-analyze random --help
Usage: imnet-analyze random [OPTIONS]

  Run analysis on a randomly generated set of strings for testing

Options:
  --nstrings INTEGER    Number of strings to generate
  --min-length INTEGER  minimum number of characters per string
  --max-length INTEGER  maximum number of characters per string
  --help                Show this message and exit.
```

For an example of using the `imnet` python library, have a look at the [example notebook](notebooks/example_workflow.ipynb).



