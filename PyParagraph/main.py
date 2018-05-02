# ## Option 4: PyParagraph

# ![Language](Images/language.jpg)

# In this challenge, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

# Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:

# * Import a text file filled with a paragraph of your choosing.

# * Assess the passage for each of the following:

#   * Approximate word count

#   * Approximate sentence count

#   * Approximate letter count (per word)

#   * Average sentence length (in words)

# * As an example, this passage:

# > “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident - a blot of black upon a world of crimson and gold.”

# ...would yield these results:

# ```
# Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.56557377049
# Average Sentence Length: 24.4
# ```

# * **Special Hint:** You may find this code snippet helpful when determining sentence length (look into [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) if interested in learning more):

# ```python
# import re
# re.split("(?&lt;=[.!?]) +", paragraph)
# ```

import os
import csv

paragraph =""
words =0
sentences =0
letter_count =0
avg_letter =0.0
avg_sentence = 0.0

filepath = os.path.join("raw_data", "paragraph_1.txt")  #input path

with open(filepath) as f:

    paragraph = f.read()

    #words = the same number of spaces plus 1
    words = paragraph.count(" ") + 1         

    #sentences = the number of punctuation marks           
    sentences = paragraph.count(".") + paragraph.count("?") + paragraph.count("!")

    #letters = all characters minus space and punctuation marks
    letter_count = len(paragraph) - (words -1) - sentences


    avg_letter = letter_count / words
    avg_sentence = words / sentences




    # Paragraph Analysis
    # -----------------
    # Approximate Word Count: 122
    # Approximate Sentence Count: 5
    # Average Letter Count: 4.56557377049
    # Average Sentence Length: 24.4
    print("Paragraph Analysis")
    print("-" * 28)
    print(f"Approximate Word Count: {words}")
    print(f"Approximate Sentence Count: {sentences}")
    print(f"Average Letter Count: {avg_letter}")
    print(f"Average Sentence Length: {avg_sentence}")


    #I think they wanted us to use (import re)  and (re.split("(?&lt;=[.!?]) +", paragraph)) to split pargraph into sentence lists 
    #then count sentences (len(sentence_list) and then maybe splitting into words words=senteces.split(" ") but this way was easier






