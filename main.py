# external
from googleapiclient.discovery import build
from bs4 import BeautifulSoup

# internal
import webbrowser
from os import getcwd
from os.path import join


def get_comment(youtube, id):

    return youtube.comments().list(
        part='snippet',
        id=id
    ).execute()


def main(api_key, input_file, output_file, open_in_browser=False, verbose=False):
    file = open(input_file)
    soup = BeautifulSoup(file.read(), 'html.parser')
    file.close()

    if soup.title.contents[0] != "Your YouTube Comments":
        return print("Incorrect file provided.")

    youtube = build("youtube", "v3", developerKey=api_key)

    children = soup.body.ul.findChildren("li")

    parsed_comments = []

    for child in children:
        comment = child.contents
        if comment[0] == 'You added a ' or comment[0] == 'You ':
            # the type of comment made is a comment or reply
            comment_link_element = comment[1]
            link = comment_link_element['href']
            id = link.split('&')[1].split('=')[1]
            if verbose:
                print("Getting comment info from YouTube API with ID: " + id)
            comment = get_comment(youtube, id)
            items = comment['items']
            if (not items or len(items) != 1):
                if verbose:
                    print("Could not find comment (most likely deleted, comments stopped on video, or ghost deleted). This comment will be excluded from the results.")
                child.decompose()
            else:
                snippet = items[0]['snippet']
                snippet['htmlElement'] = child
                parsed_comments.append(snippet)

        else:
            # the type of comment is some other comment
            if verbose:
                print("Incorrect statement")
            child.decompose()

    parsed_comments.sort(key=lambda x: x['likeCount'], reverse=True)

    for comment in parsed_comments:
        element = comment['htmlElement']
        element.append(f" ({comment['likeCount']} likes)")
        soup.body.ul.append(element)

    html = soup.prettify()

    file = open(output_file, 'w')
    file.write(html)
    file.close()

    if verbose:
        print(f"Done! Open {output_file} to see the sorted comments!")

    if open_in_browser:
        webbrowser.open_new_tab(f'file://${output_file}')


if __name__ == '__main__':
    key = input("Enter your Google API key: ")
    in_file = input("Enter the file path for your google takeout file: ")
    out_file = input(
        "Enter the file path where you would like to save your output file (optional): ")

    if out_file == '':
        out_file = join(getcwd(), 'my-comments-sorted.html')

    main(key, in_file, out_file, True, True)
