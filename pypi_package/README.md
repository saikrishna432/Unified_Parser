# Python_Unified_Parser

This parser attempts to unify the languages based on the Common Label Set. It is designed across all the languages capitalising on the syllable structure of Indian languages. The Unified Parser converts UTF-8 text to common label set, applies letter-to-sound rules and generates the corresponding phoneme sequences. The effort is a step towards natural language understanding system that operates on Indian languages and generates the parsed output. This structured method requires only knowledge of the basic language. With good lexicons it is possible to get more than 95% correctness of words in a language. This method can be further extended for a number of other Indian languages in minimal time and effort. Given the unity in the diversity of Indian languages, developing parsers for new languages is easy using the unified approach. 

Our python parser - [uparser.py](src/indic-unified-parser/uparser.py) - Combines lex and yacc functionality in a single python script using the [PLY](src/indic-unified-parser/ply) framework.

## Publications
[Baby, Arun, et al. "A unified parser for developing Indian language text to speech synthesizers." Text, Speech, and Dialogue: 19th International Conference, TSD 2016, Brno, Czech Republic, September 12-16, 2016, Proceedings 19. Springer International Publishing, 2016.](https://www.iitm.ac.in/donlab/tts/downloads/unified/unified.pdf)

## Installation

```bash
pip install indic_unified_parser
```

## How to use

```bash
from indic_unified_parser.uparser import wordparse
parsed_output_string = wordparse(<word : str>, <lsflag : int>, <wfflag : int>, <clearflag : int>)
```

1. `lsflag`: always 0. Deprecated.
2. `wfflag`: 0 for Monophone parsing, 1 for syllable parsing, 2 for Akshara Parsing"
3. `clearflag`: 1 for removing the lisp like format of output and to just produce space separated output. Otherwise, 0.

## Examples

## URLS
[Homepage](https://github.com/vikram-kv/Unified_Parser)

## Authors

Vikram K V, Dual Degree, Computer Science Dept, IIT Madras.