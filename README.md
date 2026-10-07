# Inkrypt

**Inkrypt** is a lightweight Python desktop application that allows you to hide encrypted secret messages inside image files using steganography. It combines symmetric encryption via `cryptocode` with LSB (Least Significant Bit) steganography via `stegano` to ensure your hidden messages are both concealed and password-protected.

---

## Features

* **Symmetric Encryption:** Encrypts your secret message with a password before embedding it into the image.


* **LSB Steganography:** Hides the encrypted message seamlessly within image pixel data.


* **Simple GUI:** Intuitive desktop user interface built with Tkinter.


* **Supported Formats:** Open PNG, JPG, and JPEG files, with output saved securely as lossless PNG format.



---

## Requirements

* **Python:** 3.x
* **Libraries:**
* `stegano`
* `Pillow`
* `cryptocode`
* `tkinter` (usually included with standard Python installations)



---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/inkrypt.git
cd inkrypt

```


2. **Install required dependencies:**
```bash
pip install stegano Pillow cryptocode

```



---

## Usage

1. **Run the application:**
```bash
python main.py

```


2. **Hide/Encrypt a Message:**
* Click **Browse** to select a base image.


* Type your hidden message into the **Secret Message** text box.


* Enter a secure key in the **Password** field.


* Click **Encrypt** and select a destination path to save the steganographic PNG image.




3. **Reveal/Decrypt a Message:**
* Click **Browse** to select an image containing a hidden message.


* Enter the password used to encrypt the message in the **Password** field.


* Click **Decrypt** to display the original message in the text area.





---

## How It Works

1. **Encryption Layer:** Your raw text is encrypted with your provided password using `cryptocode`.


2. **Steganography Layer:** The resulting cipher text is embedded into the Least Significant Bits (LSB) of the image pixels using `stegano`.


3. **Decryption:** To retrieve the text, `stegano` extracts the hidden string from the image, and `cryptocode` decrypts it using the provided password.



---

## License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
