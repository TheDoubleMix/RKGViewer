# RKG Viewer CLI
[![Tests](https://github.com/TheDoubleMix/RKGViewer/actions/workflows/python-app.yml/badge.svg)](https://github.com/TheDoubleMix/RKGViewer/actions/workflows/python-app.yml)

A Command Line Interface (CLI) tool for reading and displaying the contents of `.rkg` files in a human-readable format. Perfect for inspecting or analyzing `.rkg` files with only a terminal.
## Features

- **Read `.rkg` files**: Decodes and displays the contents of `.rkg` files directly in your terminal.
<!-- **User-Friendly**: Simple CLI options. -->
- **Readable Output**: Formats the file data for easy interpretation.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TheDoubleMix/RKGViewer.git
   cd RKGViewer
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make the script executable (optional):

   ```bash
   chmod +x app.py
   ```

### How to use

Run the tool with an `.rkg` file as input, or not:

```bash
python app.py /path/to/your/file.rkg
```
or
```bash
python app.py
```
If you don't pass a `.rkg` file as input, you will get a error. More in the Errors/Warnings section.

### Example:

```bash
python app.py sample.rkg
```

This will display a list of options to use on the `.rkg` file.

### Output:

```
> Info
  Inputs
  Misc
  Options
Press ESC to quit/→ to select.
```

The RKG Viewer CLI is still in beta, If you use the inputs or options menu, you will get a warning. More in the Errors/Warnings section.

## Errors/Warnings

The CLI is designed to handle standard `.rkg` file formats, if you want to use any other option, it's possible.
if the you have a corrupted file/a non .rkg file, you get a warning about it.
### Example:
```
01100110011100100110111101101101          First 32 bits
01010010010010110100011101000100           Correct bits
```

If there are too many arguments the program you will get a warning.
### Example:
```
Too Many arguments!
If you want to you can still select the file you want to choose.
```
If there are no arguments the program you will also get a warning.
### Example:
```
No RKG File argument given!
Type "exit" to exit rkgview
Give a path to a rkg file:
```
The RKG Viewer CLI is still in beta, If you use the inputs or options menu, you will get a warning.
### Example:
```
Not Implemented
Press ESC to quit this menu. 
```
## Issues

For issues, please report them in the [issues section](https://github.com/TheDoubleMix/RKGViewer/issues).

## License

This project uses the MIT License.

---

Thank you for using the RKG Viewer CLI! 🎉
