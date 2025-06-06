# PlagiaBot Pro 🤖

A modern Python automation tool for checking plagiarism on [Plagiarisma.net](https://plagiarisma.net) using Selenium. PlagiaBot Pro splits your text into chunks, submits them to Plagiarisma.net, and downloads plagiarism reports as PDFs. Perfect for batch-checking large documents, academic papers, essays, and research articles! 📄🔍

---

## Why PlagiaBot Pro?

- **Automate Plagiarisma.net**: No more manual copy-paste! PlagiaBot Pro automates the entire process of submitting text to Plagiarisma.net and downloading reports.
- **Bulk Plagiarism Checking**: Easily check large files, books, or multiple documents for plagiarism using Plagiarisma.net.
- **Save Time**: Download all your Plagiarisma.net PDF reports in one go.
- **Perfect for Students, Researchers, and Writers**: Ensure your work is original and properly cited.

---

## Features

- 📑 Splits large text files into manageable chunks for Plagiarisma.net
- 🤖 Automates registration and login on Plagiarisma.net
- 🖱️ Submits each chunk for plagiarism checking on Plagiarisma.net
- 📥 Downloads PDF reports automatically from Plagiarisma.net
- 🔄 Rotates users after every 4 chunks to avoid Plagiarisma.net limits

---

## Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/Deepanshu291/PlagiaBot-Pro.git
   cd PlagiaBot-Pro
   ```

2. **Install Python dependencies**

   - You can use the provided batch file for quick setup:
     ```sh
     install.bat
     ```
   - Or install manually:
     ```sh
     pip install selenium
     ```

3. **Download ChromeDriver**

   - Download the version matching your Chrome browser from [here](https://chromedriver.chromium.org/downloads)
   - Place `chromedriver.exe` in the `drivers/` folder

   > ⚠️ **If the program is not working:**
   >
   > - Your Chrome browser may have updated.
   > - Download the latest ChromeDriver version matching your browser and replace the old `chromedriver.exe` in the `drivers/` folder.

4. **Prepare your text file**
   - Place your text in `project.txt` or update the path in `app.py`

---

## Usage

- You can run the program using the batch file:
  ```sh
  run.bat
  ```
- Or run directly with Python:
  ```sh
  python app.py
  ```

- Reports will be saved in the `Data/` directory (or as configured).
- Each chunk is checked for plagiarism using Plagiarisma.net and a PDF report is downloaded.

---

## Requirements

- Python 3.7+
- Google Chrome browser
- Selenium

---

## Folder Structure

```
PlagiaBot-Pro/
├── app.py
├── project.txt
├── drivers/
│   └── chromedriver.exe
├── Data/
│   └── results.pdf
...
```

---

## Frequently Asked Questions (FAQ)

### 1. What is PlagiaBot Pro?

PlagiaBot Pro is an open-source Python tool that automates plagiarism checking on [Plagiarisma.net](https://plagiarisma.net) using Selenium. It is designed for bulk and automated plagiarism detection.

### 2. Is PlagiaBot Pro free?

Yes, PlagiaBot Pro is free and open-source. Plagiarisma.net may have its own usage limits or terms.

### 3. Can I use PlagiaBot Pro for academic research?

Absolutely! PlagiaBot Pro is perfect for students, researchers, and writers who need to check large documents for plagiarism using Plagiarisma.net.

### 4. Why do I need to update ChromeDriver?

PlagiaBot Pro uses Selenium and ChromeDriver to automate your browser. If your Chrome browser updates, you may need to update ChromeDriver to match.

---

## ⚠️ Disclaimer

- This tool is for educational and research purposes only.
- Respect the terms of service of [Plagiarisma.net](https://plagiarisma.net).
- PlagiaBot Pro is not affiliated with Plagiarisma.net.

---

Made with ❤️ using Python, Selenium, and Plagiarisma.net.
