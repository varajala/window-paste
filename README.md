# window-paste
A minimal GUI tool that captures text input and sends it to stdout. Perfect for quick text capture operations or as part of command line pipelines.

## Usage
Run the script directly:
```bash
python text_capture.py
```

Use it in a pipeline:
```bash
python text_capture.py | grep "something"
```

Or make it executable (Unix-like systems):
```bash
chmod +x text_capture.py
./text_capture.py
```

This opens a GUI window with a text area.
The application will simply write the contents of that text area to the stdout, when ENTER is pressed, or the window is closed.

Use SHIFT+ENTER to insert a newline.