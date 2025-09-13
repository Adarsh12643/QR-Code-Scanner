# QR Code Scanner Using Pyzbar and OpenCV

A simple Python project that scans and decodes **QR codes** in real-time using **OpenCV** for image processing and **Pyzbar** for decoding.

## 🚀 Features

* Detects and decodes QR codes from **images** or **live webcam feed**
* Displays the decoded text on the video frame
* Supports multiple QR codes in a single frame
* Lightweight and easy to use

## 🛠️ Technologies Used

* [Python 3](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [Pyzbar](https://pypi.org/project/pyzbar/)

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Adarsh12643/qr-code-scanner.git
cd qr-code-scanner
```

Install dependencies:

```bash
pip install opencv-python pyzbar
```

## ▶️ Usage

### 1. Run QR Scanner with Webcam

```bash
python qr_scanner.py
```

### 2. Scan QR Code from an Image

```bash
python qr_scanner_image.py --image sample.png
```

## 📂 Project Structure

```
qr-code-scanner/
│── qr_scanner.py          # Scan QR codes from webcam
│── qr_scanner_image.py    # Scan QR codes from images
│── sample.png             # Sample QR code image
│── requirements.txt       # Dependencies
│── README.md              # Documentation
```

## 📸 Example Output

* **Webcam Mode:**
  The decoded QR code text will be displayed directly on the live video frame.

## 🔮 Future Enhancements

* Save decoded QR data into a file/database
* Add support for **barcode scanning**
* Create a **GUI-based scanner**

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📜 License

This project is licensed under the **MIT License**.

---
