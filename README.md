# YT-Comment-Sorter
A python script that allows you to sort your YouTube comments by most liked, to easily find out which comment of yours is the most liked out of hundreds!

Unfortnately, Google does not allow an easy way to sort your comments by most liked, and doesn't even provide liked comment information in their takeout file. Therefore, I had to make this program which contacts the YouTube API with the information from the takeout file to find out your most liked comments.


# Usage

## Part 1: Obtain your takeout file
1. Open Google takeout.
2. Click on "deselect all"
3. Check "YouTube and YouTube Music", then click on "All YouTube data included"
4. Click on "deselect all" again
5. Select "my-comments" and click "Next Step"
6. Click on "Create Export", download the .zip file, and extract the HTML file named "my-comments" in your Downloads folder.

## Part 2: Obtaining your API key
Follow [this tutorial](https://youtu.be/sVEytWDWYwM) to get a YouTube API key

## Part 3: Use the script
1. Install Python and PIP and make sure the "add to PATH" option is ticked during installation
2. Download this repository and unzip it, or clone it.
3. Open Terminal on Mac or Linux or Command Prompt on Windows. Then type `cd Downloads`. Then type `cd YT-Comment-Sorter` or whatever your unzipped folder is saved as.
4. Type `pip install -r requirements.txt`
5. Type `python3 main.py`
6. Follow what the script asks you to do, and be patient while the script does it's thing. As long as you have < 10,000 comments it should work but it will take some time.
