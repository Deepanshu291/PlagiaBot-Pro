# 🕸️ Webscrap Plagiarism Checker 🚀

A modern Python automation tool that splits your text into chunks, submits them to Plagiarisma.net using Selenium, and downloads plagiarism reports as PDFs. Perfect for batch-checking large documents! 📄🔍

## Features

- 📑 Splits large text files into manageable chunks
- 🤖 Automates registration and login on Plagiarisma.net
- 🖱️ Submits each chunk for plagiarism checking
- 📥 Downloads PDF reports automatically
- 🔄 Rotates users after every 4 chunks to avoid limits

## Installation

1. **Clone the repository**

   ```sh
   git clone <your-repo-url>
   cd Webscrap
   ```

2. **Install Python dependencies**

   ```sh
   pip install selenium
   ```

3. **Download ChromeDriver**

   - Download the version matching your Chrome browser from [here](https://chromedriver.chromium.org/downloads)
   - Place `chromedriver.exe` in the `drivers/` folder

   > ⚠️ **If the program is not working:**
   > - Your Chrome browser may have updated.
   > - Download the latest ChromeDriver version matching your browser and replace the old `chromedriver.exe` in the `drivers/` folder.

4. **Prepare your text file**
   - Place your text in `project.txt` or update the path in `app.py`

## Usage

```sh
python app.py
```

- Reports will be saved in the `Data/` directory (or as configured).

## Requirements

- Python 3.7+
- Google Chrome browser
- Selenium

## Folder Structure

```
Webscrap/
├── app.py
├── project.txt
├── drivers/
│   └── chromedriver.exe
├── Data/
│   └── results.pdf
...
```

## ⚠️ Disclaimer

- This tool is for educational and research purposes only.
- Respect the terms of service of Plagiarisma.net.

---

Made with ❤️ using Python & Selenium.
