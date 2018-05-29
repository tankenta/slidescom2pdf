# slidescom2pdf
Short python script to export your slides (decks) created on slides.com as PDF files.

## Testing environment
### Ubuntu 14.04
* Python 3.6.3
	- selenium 3.11.0
* Chromium 65.0
* ChromeDriver 2.38
* ImageMagick 6.7.7

## Usage
Just run the script without arguments.
Then, you are prompted to enter information on the slides.com account and output destination, and the slides export begins.
```
./slidescom2pdf.py
```

By describing some information in `config.py`, it is possible to omit some information input at the time of script execution.

### Config parameters
* `SLIDE_SIZE`: Size of temporary screenshot files. (width, height)
* `SCREENSHOT_BASENAME`: Base name of temporary screenshot files.
* `UNAME`: Your account's ID on slides.com
* `EMAIL`: E-mail address you registered with slides.com
* `DECK_NAME`: Your deck's ID included in the URL.
* `SS_DIR`: Path to the temporary directory you save screenshots in.
* `PDF_FNAME`: Name of the PDF file you will get.

## ToDo
* [ ] Handle login with Google and Facebook
* [ ] Add slide position initialization process
