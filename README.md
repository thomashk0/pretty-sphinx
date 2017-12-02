# Pretty Sphinx

A very simple [pandoc](https://pandoc.org/) filter to fix some conversion from HTML.

Current features:

* Correctly render syntax highlighting from sphinx HTML output

## Usage

Clone this repository, then run install the filter as a regular Python package:

```console
$ pip install .
```

Then, just use the executable ```pretty_sphinx``` it a normal pandoc filter:

```
$ pandoc -s --filter pretty_sphinx -o example0_out.docx test/example0_in.html
```