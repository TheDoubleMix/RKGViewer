# RKG File Reader CLI

A Command Line Interface (CLI) tool for reading and displaying the contents of `.rkg` files in a human-readable format. Perfect for inspecting or analyzing `.rkg` files with only a terminal.
## Features

- **Read `.rkg` files**: Decodes and displays the contents of `.rkg` files directly in your terminal.
- **User-Friendly**: Simple CLI options.
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
python app.py path/to/your/file.rkg
```
or
```bash
python app.py
```

This will display the encrypted contents of the `.rkg` file in the terminal.

### Example

```bash
python app.py sample.rkg
```

Output:

```
> Info
  Inputs
  Misc
  Options
Press ESC to quit/→ to select.
```

## Errors/Warnings

The CLI is designed to handle standard `.rkg` file formats, if you want to use any other option, it's possible.
if the you have a corrupted file/a non .rkg file, you get a warning about it.
Example:
```
01100110011100100110111101101101          First 32 bits
01010010010010110100011101000100           Correct bits
```

if there are too many arguments the program you will get a warning.
Example:
```
Too Many arguments!
If you want to you can still select the file you want to choose.
```
## Issues

For issues, please report them in the [issues section](https://github.com/yourusername/rkg-file-reader-cli/issues).

## License

This project doesn't have a licese yet.

---

Thank you for using the RKG File Reader CLI! 🎉
