# qrcode-labelmaker

Printer: Brother QL-500

Label Size: 62x29mm

## Installation
Get Python 3

```
pip install -r requirements.txt
```

## Usage:
Things without owner: 
```
./create.py "My awesome Thing" "https://wiki.darmstadt.ccc.de/awesome-thing"
```

Things with owner: 
```
./create.py -o "fleaz" "My private Thing" "https://wiki.darmstadt.ccc.de/private-thing"
```

If you add the `--printer` switch, the label will automatically get printed
after creating. We asume that the printer is called *Brother_QL-500*.

The label is also saved as *label.pdf* in the root of this project.
