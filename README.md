# Patch ACF files with dataref patches

This python script takes ```.acf``` and ```.acf.txt``` files and will patch a new ```.acf.patched``` model file. This will not overwrite your existing acf model. It will generate a file with the ```.acf.patched``` extension. You'll need to backup your original model somewhere else and then rename the ```.acf.patched``` file to ```.acf```.

I highly advise you create a temporary directory with your model and patchfile incase something goes wrong. 

## Script Usage

This script requires that you have python installed.

Help text:

```bash
python3 converter.py -h
usage: converter.py [-h] -a --acf -p --patch

Patch ACF models from txt files

optional arguments:
  -h, --help  show this help message and exit
  -a --acf    filename of your acf model, ex: CarbonCub.acf
  -p --patch  patch file ending in .acf.txt
```

Example usage:

```bash
python3 converter.py -a CarbonCub.acf -p CarbonCub.acf.txt
```