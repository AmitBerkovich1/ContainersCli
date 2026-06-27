# 🐳 CodeRunner CLI

A lightweight command-line tool that runs local code inside Docker containers with automatic image management and workspace mounting.

It allows developers to execute code in isolated environments without installing language runtimes locally.

---

## ✨ Features

- 🚀 Run code inside any Docker image (Python, Node.js, Go, etc.)
- 📁 Automatic mounting of local project directories into containers
- 📦 Auto-pull Docker images if missing locally
- 🧑‍💻 Interactive mode (open shell inside container)
- ⚡ Run single commands or multiple-step workflows
- 🧾 Structured logging with debug mode
- 🧪 Validation of environment (Docker, paths, etc.)

---

## 📦 Project Structure

```text
ContianerCli/
│
├── ContianerCli/
│   ├── .gitigonre
│   ├── main.py
│   ├── cli.py
│   ├── docker_runner.py
│   ├── validation.py
│   ├── utils.py
│   └── logger.py
│
├── pyproject.toml
└── README.md
```

---

## ⚙️ Requirements

- Python 3.10+
- Docker installed and running
- pip

---

## 📥 Installation

```bash
pip install -e .
```

---

## 🚀 Usage

### Interactive mode

```bash
coderunner --image python:3.12 --path .
```

### Run command

```bash
coderunner --image python:3.12 --path . --command python main.py
```

### Multiple commands

```bash
coderunner --image python:3.12 --path . \
  --command pip install -r requirements.txt \
  --command pytest \
  --command python main.py
```

### Debug mode

```bash
coderunner --image python:3.12 --path . --verbose
```

---

## 🧱 How It Works

1. Parse CLI arguments
2. Validate environment
3. Pull Docker image if needed
4. Mount project directory into `/workspace`
5. Run command or open shell

---

## 🧰 CLI Options

| Flag | Description |
|------|------------|
| --image | Docker image to use, if not exists on the machine the project will pull it automaticllay |
| --path | Local project path |
| --command | Command(s) to run |
| --name | Set name to the created container |

---

## 🚀 Future Improvements
- config file support (.coderunner.yml)
- environment variables
- prettier logs (Rich)
