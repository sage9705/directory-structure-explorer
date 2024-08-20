# Directory Structure Explorer

Directory Structure Explorer is a PyQt6-based desktop application that generates and displays the structure of a directory in a visual tree format. It provides a user-friendly interface for selecting directories, excluding specific subfolders, and optionally including subdirectories in the output. The app features a progress bar that indicates the progress of directory structure generation, especially useful for large directories. The progress bar is visible if the structure is large.

## Features

- **Directory Selection**: Easily select the directory you want to analyze using a graphical interface.
- **Exclude Subfolders**: Specify subfolders to exclude from the directory structure.
- **Include/Exclude Subdirectories**: Toggle whether to include subdirectories in the structure.
- **Progress Bar**: Visual feedback on the progress of directory structure generation, especially useful for large directories.
- **Real-Time Display**: The directory structure is displayed in real-time in a text editor widget.
- **Optimized for Performance**: The directory structure generation is handled in a separate worker thread to keep the UI responsive, even with large directories.
- **UI Design**: A fairly sleek and modern user interface with updated color schemes, padding, and styles for improved user experience.

## Installation

### Prerequisites

- Python 3.x
- PyQt6

### Install Dependencies

Install the necessary dependencies using pip:

```bash
pip install PyQt6
```

## Clone the Repository

```bash
git clone https://github.com/sage9705/directory-structure-explorer.git
cd directory-structure-explorer

```

## Usage

Run the application:

```bash
python dir.py
```

1. Click the **Select Directory** button to choose the directory you want to analyze.

2. If needed, enter the subfolders you want to exclude, separated by commas (e.g., `node_modules,venv`).

3. Check or uncheck the **Include subdirectories** option to control whether subdirectories are included in the output.

4. The directory structure will be generated and displayed in the text area, with a progress bar indicating the generation status.

## Applications

**Directory Structure Explorer** can be useful in various real-world scenarios:

- **Codebase Navigation:** Developers can use this tool to visualize the structure of a large codebase, making it easier to navigate and understand the project's layout.

- **Backup and Archiving:** Before backing up or archiving a directory, users can generate a structure map to ensure that all important files and folders are included.

- **Documentation:** The generated directory structure can be used in documentation to provide a clear overview of a project's organization.

- **Auditing and Compliance:** Companies can use this tool to audit the contents of directories, ensuring that no unauthorized files or folders are present.

## Directory Structure Example

Here is an example of the directory structure output:

└── your_directory/
├── file1.txt
├── subfolder1/
│ ├── file2.txt
│ └── file3.txt
└── subfolder2/
└── file4.txt

## Customization

### Styling

The application's styling is controlled via the `style.css` file. You can customize the colors, fonts, and layouts to suit your preferences.

### Icons

You can replace the existing icons (`icon.png`, `folder.png`) with your custom icons by placing your icon files in the application directory.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

### Development Setup

1. Fork the repository.
2. Clone the repository to your local machine.
3. Create a new branch for your feature or bugfix.
4. Make your changes and commit them with descriptive messages.
5. Push your changes and open a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
