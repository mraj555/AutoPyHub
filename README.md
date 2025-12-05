# 🚀 AutoPyHub

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://www.python.org/)
[![Code Style](https://img.shields.io/badge/Code%20Style-Clean%20%26%20Readable-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Dependencies](https://img.shields.io/badge/Dependencies-watchdog%206.0.0-yellow.svg)](https://pypi.org/project/watchdog/)

**🤖 Intelligent File Management Automation Suite**

*Streamline your file organization with intelligent sorting and batch renaming capabilities*

</div>

---

## 📋 Table of Contents

- [🌟 Overview](#-overview)
- [🏗️ Architecture](#️-architecture)
- [🔧 Core Components](#-core-components)
- [📁 File Organization System](#-file-organization-system)
- [🔄 Batch Renaming Engine](#-batch-renaming-engine)
- [⚡ Real-time File Monitoring](#-real-time-file-monitoring)
- [💾 Data Flow & Interactions](#-data-flow--interactions)
- [🎯 Key Features](#-key-features)
- [📊 File Categories](#-file-categories)
- [🎮 User Interface Flow](#-user-interface-flow)
- [🔍 Code Examples](#-code-examples)
- [⚡ Performance Features](#-performance-features)

---

## 🌟 Overview

**AutoPyHub** is a powerful Python-based file management automation suite designed to simplify and streamline file organization tasks. The project consists of three main modules that work together to provide comprehensive file management solutions:

- **📁 File Pilot**: Intelligent file sorting and categorization
- **🏷️ Wander Sort**: Batch file renaming with preview capabilities  
- **🐺 Flow Wolf**: Real-time file monitoring and automatic organization

### 🎯 Mission
Transform chaotic file directories into organized, systematically structured folders with minimal user intervention.

---

## 🏗️ Architecture

```
AutoPyHub/
├── 📄 00_file_pilot.py          # File sorting & categorization engine
├── 📄 01_wander_sort.py         # Batch renaming utility
├── � 02_flow_wolf.py           # Real-time file monitoring
└── 📄 requirements.txt          # Python dependencies
```

### 🏛️ System Architecture

<div align="center">

```mermaid
graph TD
    A[🚀 AutoPyHub Suite] --> B[📁 File Pilot]
    A --> C[🏷️ Wander Sort]
    A --> D[🐺 Flow Wolf]
    
    B --> E[Extension Detection]
    B --> F[Category Mapping]
    B --> G[Folder Creation]
    B --> H[File Movement]
    
    C --> I[File Discovery]
    C --> J[Name Generation]
    C --> K[Preview System]
    C --> L[Batch Renaming]
    
    D --> M[Watchdog Observer]
    D --> N[Event Handler]
    D --> O[Auto-categorization]
    D --> P[Real-time Movement]
    
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
    style D fill:#fbf,stroke:#333,stroke-width:2px
```

</div>

---

## 🔧 Core Components

### 📁 File Pilot Module (`00_file_pilot.py`)

**Purpose**: Automatically organizes files into categorized folders based on file extensions

#### 🔑 Key Functions

| Function | Purpose | Input | Output |
|----------|---------|--------|---------|
| `get_destination_folder()` | Maps file extensions to categories | Filename (str) | Category folder name (str) |
| `sort_files()` | Main sorting orchestrator | Folder path (str) | Organized file structure |

#### 📋 Extension Mapping System

```python
EXTENSION_MAP = {
    "PDFs": [".pdf"],
    "Word Docs": [".docx"],
    "Excel Sheets": [".xlsx"],
    "PowerPoint Presentations": [".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mov", ".wmv"],
    "Audio Files": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Text Files": [".txt"],
    "Code Files": [".py", ".java", ".cpp", ".html", ".css", ".js"],
    # ... and more
}
```

### 🏷️ Wander Sort Module (`01_wander_sort.py`)

**Purpose**: Provides intelligent batch file renaming with preview functionality

#### 🔑 Key Functions

| Function | Purpose | Input | Output |
|----------|---------|--------|---------|
| `batch_rename()` | Batch renaming orchestrator | folder, base_name, extension | Renamed files with confirmation |

### 🐺 Flow Wolf Module (`02_flow_wolf.py`)

**Purpose**: Real-time file monitoring with automatic categorization using watchdog library

#### 🔑 Key Components

| Component | Purpose | Functionality |
|-----------|---------|---------------|
| `FileMoverHandler` | Event handler class | Processes file creation events |
| `on_created()` | File creation trigger | Automatically categorizes new files |
| `Observer` | Watchdog monitor | Watches Downloads folder for changes |

---

## 📁 File Organization System

### 🎯 Categorization Logic

<div align="center">

```mermaid
flowchart LR
    A[📄 File Input] --> B{Extension Check}
    B -->|Match Found| C[🏷️ Assign Category]
    B -->|No Match| D[📁 Others Folder]
    C --> E[📂 Create Category Folder]
    D --> E
    E --> F[🔄 Move File]
    
    style A fill:#ffe,stroke:#333,stroke-width:2px
    style F fill:#efe,stroke:#333,stroke-width:2px
```

</div>

### 📊 Supported File Categories

| 📁 Category | 🔤 Extensions | 🎯 Use Case |
|-------------|---------------|-------------|
| **Documents** | `.pdf`, `.docx`, `.xlsx`, `.pptx` | Office files, reports |
| **Media** | `.jpg`, `.png`, `.mp4`, `.mp3` | Photos, videos, audio |
| **Development** | `.py`, `.java`, `.html`, `.css` | Source code files |
| **Archives** | `.zip`, `.rar`, `.7z` | Compressed files |
| **System** | `.dll`, `.exe`, `.sys` | Windows system files |
| **Others** | *Unmatched extensions* | Miscellaneous files |

---

## 🔄 Batch Renaming Engine

### 🎮 Workflow Process

<div align="center">

```mermaid
sequenceDiagram
    participant U as 👤 User
    participant W as 🏷️ Wander Sort
    participant F as 📁 File System
    
    U->>W: Input folder path
    U->>W: Specify base name
    U->>W: Choose extension
    W->>F: Scan directory
    F-->>W: File list
    W->>W: Generate preview
    W-->>U: Show preview
    U->>W: Confirm (y/n)
    alt User confirms
        W->>F: Rename files
        F-->>W: Success status
        W-->>U: Completion message
    else User cancels
        W-->>U: Cancel message
    end
```

</div>

### 🔧 Renaming Pattern

```
Original: photo_001.jpg, photo_002.jpg, photo_003.jpg
Base Name: vacation
Result: vacation_1.jpg, vacation_2.jpg, vacation_3.jpg
```

---

## ⚡ Real-time File Monitoring

### 🎯 Flow Wolf Workflow

<div align="center">

```mermaid
flowchart TD
    A[🐺 Flow Wolf Start] --> B[📁 Watch Downloads]
    B --> C{New File Detected?}
    C -->|Yes| D[� Analyze Extension]
    C -->|No| B
    D --> E[🏷️ Determine Category]
    E --> F[📂 Check/Create Folder]
    F --> G[🔄 Move File]
    G --> H[✅ Success Message]
    H --> B
    
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style G fill:#efe,stroke:#333,stroke-width:2px
```

</div>

---

## �💾 Data Flow & Interactions

### 🌊 File Pilot Data Flow

```
User Input → Path Validation → File Discovery → Extension Analysis → 
Category Assignment → Folder Creation → File Movement → Success Feedback
```

### 🌊 Wander Sort Data Flow

```
User Input → Directory Scanning → File Filtering → Name Generation → 
Preview Display → User Confirmation → Batch Renaming → Completion Report
```

### 🌊 Flow Wolf Data Flow

```
File Creation → Event Trigger → Extension Detection → Category Lookup → 
Folder Creation → File Movement → Real-time Feedback
```

---

## 🎯 Key Features

### 🌟 File Pilot Features

- ✅ **Intelligent Categorization**: 18 predefined file categories
- ✅ **Safe Operation**: Non-destructive file moving
- ✅ **Auto-folder Creation**: Creates missing directories automatically
- ✅ **Progress Feedback**: Real-time operation status
- ✅ **Unicode Support**: Handles international filenames
- ✅ **Cross-platform**: Works on Windows, Linux, and macOS

### 🌟 Wander Sort Features

- ✅ **Preview System**: See changes before applying
- ✅ **Extension Filtering**: Target specific file types
- ✅ **Sequential Naming**: Automatic numbering system
- ✅ **User Confirmation**: Safety mechanism prevents accidents
- ✅ **Case-insensitive**: Handles mixed-case extensions
- ✅ **Error Handling**: Graceful failure with informative messages

### 🌟 Flow Wolf Features

- ✅ **Real-time Monitoring**: Watches Downloads folder continuously
- ✅ **Automatic Organization**: Files sorted immediately after download
- ✅ **Event-driven**: Responds to file system events instantly
- ✅ **Background Operation**: Runs silently without user intervention
- ✅ **Error Recovery**: Handles file locks and permission issues
- ✅ **Configurable**: Easy to modify watched folder and categories

---

## 📊 File Categories

### 📋 Complete Extension Mapping

| 🏷️ Category | 🔤 Supported Extensions |
|-------------|-------------------------|
| **PDFs** | `.pdf` |
| **Word Docs** | `.docx` |
| **Excel Sheets** | `.xlsx` |
| **PowerPoint** | `.pptx` |
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` |
| **Videos** | `.mp4`, `.avi`, `.mov`, `.wmv` |
| **Audio** | `.mp3`, `.wav`, `.aac`, `.flac` |
| **Archives** | `.zip`, `.rar`, `.7z` |
| **Text** | `.txt` |
| **Code** | `.py`, `.java`, `.cpp`, `.html`, `.css`, `.js` |
| **Spreadsheets** | `.xls` |
| **Presentations** | `.ppt` |
| **Databases** | `.db`, `.sqlite` |
| **Config** | `.ini`, `.cfg` |
| **Logs** | `.log` |
| **System** | `.dll`, `.sys` |
| **Executables** | `.exe` |
| **Others** | *All unmatched extensions* |

---

## 🎮 User Interface Flow

### 🖥️ Command Line Interface

All modules feature **interactive command-line interfaces** with:

- 📍 **Smart Defaults**: Current directory as default path
- ❓ **Input Validation**: Path verification and error handling
- 📊 **Progress Indicators**: Visual feedback during operations
- ✅ **Completion Messages**: Success/failure notifications

### 🎲 Interaction Examples

#### File Pilot Usage
```
Enter the folder path or leave empty to use current folder: 📁
📁 Moved: report.pdf to PDFs
📁 Moved: photo.jpg to Images
📁 Moved: song.mp3 to Audio Files
✅ Files sorted successfully.
```

#### Wander Sort Usage
```
Enter the folder path or leave empty to use current folder: 📁
Enter the base name for renaming: vacation
Enter the file extension to filter (e.g., .jpg, .png): .jpg
Renamed: IMG_001.jpg to vacation_1.jpg
Renamed: IMG_002.jpg to vacation_2.jpg
Are you sure you want to rename all files? (y/n): y
✅ Batch rename completed.
```

#### Flow Wolf Usage
```
👁️‍🗨️ Watching folder: C:\Users\Username\Downloads
✅ Moved: C:\Users\Username\Downloads\document.pdf to C:\Users\Username\Downloads\PDFs\document.pdf
✅ Moved: C:\Users\Username\Downloads\image.jpg to C:\Users\Username\Downloads\Images\image.jpg
```

---

## 🔍 Code Examples

### 📁 File Pilot - Core Logic

```python
def get_destination_folder(filename):
    """
    Determines the destination folder for a file based on its extension.
    
    Args:
        filename (str): The name of the file to categorize.
    
    Returns:
        str: The folder name from EXTENSION_MAP, or 'Others' if no match.
    """
    ext = os.path.splitext(filename)[1].strip().lower()
    for folder, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return folder
    return "Others"
```

### 🏷️ Wander Sort - Preview System

```python
# Preview the new filenames without actually renaming
for i, file in enumerate(files, start=1):
    new_name = f"{base_name}_{i}{extension}"
    print(f"Renamed: {file} to {new_name}")

# Ask user for confirmation before performing the actual rename
confirm = input("Are you sure you want to rename all files? (y/n): ").strip().lower()
```

### 🐺 Flow Wolf - Event Handler

```python
class FileMoverHandler(FileSystemEventHandler):
    """Handles file-system events; automatically moves new files to categorized folders."""
    
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        ext = os.path.splitext(file_path)[1].lower()
        folder_name = FILE_DESTS.get(ext, "Others")
        full_dest_path = os.path.join(WATCH_FOLDER, folder_name)
        os.makedirs(full_dest_path, exist_ok=True)
        
        move_to = os.path.join(full_dest_path, os.path.basename(file_path))
        try:
            shutil.move(file_path, move_to)
            print(f"✅ Moved: {file_path} to {move_to}")
        except Exception as e:
            print(f"❌ Error moving {file_path}: {e}")
```

---

## ⚡ Performance Features

### 🚀 Optimization Strategies

- **🎯 Targeted Operations**: Only processes specified file types
- **💾 Memory Efficient**: Processes files one at a time
- **⚡ Fast Extension Matching**: Dictionary-based lookup system
- **🔄 Safe File Operations**: Uses atomic move operations
- **🛡️ Error Recovery**: Continues operation on individual file failures
- **👁️‍🗨️ Event-driven**: Real-time response without polling overhead

### 📈 Performance Characteristics

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| File Categorization | O(n × m) | O(1) |
| Batch Renaming | O(n) | O(n) |
| Directory Scanning | O(n) | O(n) |
| Real-time Monitoring | O(1) per event | O(1) |

*Where n = number of files, m = number of extension categories*

---

<div align="center">

## 🎉 **AutoPyHub** - Your Intelligent File Management Companion

**🚀 Ready to transform your chaotic folders into organized masterpieces!**

*Choose your weapon: File Pilot for batch sorting, Wander Sort for intelligent renaming, or Flow Wolf for real-time organization!*

</div>

---

<div align="center">

### 🔗 **Made with ❤️ using Python**

*Clean code, powerful functionality, endless possibilities*

</div>