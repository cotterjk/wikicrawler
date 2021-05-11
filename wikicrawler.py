import bs4
import requests

# A random featured article from the past
response = requests.get("https://en.wikipedia.org/wiki/Special:RandomInCategory/Featured_articles")

if response is not None:
    html = bs4.BeautifulSoup(response.text, 'html.parser')

    title = html.select("#firstHeading")[0].text
    paragraphs = html.select("p")

    shortest_s = ""
    current_s = ""
    #try tokenizing into array(?) and measuring from there.
    for para in paragraphs:
        p = list(para.text)
        for ch in p:
            if ch == ".":
                if shortest_s == "":
                    shortest_s = current_s
                    current_s = ""

                elif len(current_s) < len(shortest_s):
                    shortest_s = current_s
                    current_s = ""
            else:
                current_s += ch
    print (''.join(shortest_s))

    # TODO: parse through paragraphs to find shortest_s distance between two periods.
    # Test with some smaller, known article.
    # TODO: sort out periods that don't end sentences.
    # Hint: "Use negative look behind. regex (?<!Mr|Mrs|Dr|Ms)\."
    # Best lead: https://www.sitepoint.com/community/t/choose-whole-sentences-and-only-whole-sentences-reliably-with-regex/8075/4
    # Worth using a tokenizing package, not the manual if-elip above.
    # Count shortest sentence by characters or word count (spaces)?

    print ("FROM: " + title)
