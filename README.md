# Pixeled

## A DOM parser and renderer for the CLI

### What is Pixeled?
Pixelled is a DOM parser and renderer for the CLI. It allows you to create a JSON file with Elements that get parsed into a DOM and rendered in the terminal. It is written in Python and uses the PyInstaller library to create a standalone executable

### How to use Pixeled?
1. Create a JSON file with the desired elements. For example:
```json
[
    {
        "type": "TextBox",
        "nodeName": "Text1",
        "nodeID": 1,
        "priority": 0,
        "Text": "Hello, World!",
        "Color": "blue"
    },
    {
        "type": "TextBox",
        "nodeName": "Text2",
        "nodeID": 2,
        "priority": 1,
        "Text": "Bye, World!",
        "Color": "red"
    }
]
```
2.
Make the executable:
```bash
make
```
3.
Run the executable:
```bash
./dist/Pixeled/Pixeled path/to/your/file.json -d # -d is for debug mode, it will print ALOT of information
```

### Contributing
If you want to contribute to Pixeled, feel free to fork the repository and create a pull request. Any contributions are welcome!

## License
This project is licensed under the BSD 3-Clause License. See the LICENSE file for more details.