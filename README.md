# ✅ PyTodo — Command-Line To-Do App

> A simple, lightweight to-do list manager that runs right in your terminal — built with Python and powered by JSON file storage.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 About the Project

**PyTodo** is a beginner-friendly command-line application that helps you manage your daily tasks without leaving the terminal. Tasks are saved to a local file so your list is always there when you come back.

This project was built to practice core Python concepts such as:
- **File I/O** — reading and writing files using Python's built-in `open()`
- **JSON handling** — storing and loading structured task data using the `json` module
- **Functions and conditionals** — clean, reusable logic
- **Lists and loops** — managing and displaying task data
- **User input handling** — interactive terminal menus

---

## ✨ Features

| Feature         | Description                                      |
|-----------------|--------------------------------------------------|
| ➕ Add Tasks     | Quickly add new tasks to your list               |
| 🗑️ Delete Tasks  | Remove tasks you no longer need                  |
| ✅ Mark Complete | Check off tasks when you're done                 |
| 💾 JSON Storage  | Tasks are saved in a structured `.json` file and persist across sessions |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3** installed on your machine.

```bash
python --version
# or
python3 --version
```

If you don't have Python, download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/pytodo.git
   ```

2. **Navigate into the project folder**
   ```bash
   cd pytodo
   ```

3. **Run the app**
   ```bash
   python todo.py
   ```

> ✅ No third-party libraries required — uses only Python's built-in `json` and `os` modules!

---

## 🖥️ Usage

Once you run the app, you'll see a menu like this:

```
============================
      📝 PyTodo App
============================
1. View all tasks
2. Add a new task
3. Mark a task as complete
4. Delete a task
5. Exit
============================
Enter your choice:
```

### Examples

**Adding a task:**
```
Enter your choice: 2
Enter task: Buy groceries
✅ Task added successfully!
```

**Viewing tasks:**
```
Enter your choice: 1

Your Tasks:
-----------
1. [ ] Buy groceries
2. [✓] Call the dentist
3. [ ] Finish homework
```

**Marking a task complete:**
```
Enter your choice: 3
Enter task number to mark complete: 1
✅ Task marked as complete!
```

**Deleting a task:**
```
Enter your choice: 4
Enter task number to delete: 2
🗑️  Task deleted!
```

---

## 📁 Project Structure

```
pytodo/
│
├── todo.py          # Main application file (all logic lives here)
├── tasks.json       # Auto-generated JSON file where tasks are stored
└── README.md        # Project documentation
```

### How Data is Stored

Tasks are saved in `tasks.json` as a structured list of objects. Each task looks like this:

```json
[
  {
    "id": 1,
    "task": "Buy groceries",
    "completed": false
  },
  {
    "id": 2,
    "task": "Call the dentist",
    "completed": true
  }
]
```

The app uses Python's built-in `json` module to **read** the file on startup and **write** back to it after every change — so your tasks are never lost.

## 👨‍💻 Developer

Made with ❤️ by **[Your Name]**  
🔗 GitHub: [@your-username](https://github.com/your-username)

---

> ⭐ If you found this project helpful, please give it a star on GitHub!
