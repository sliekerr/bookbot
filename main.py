def main():
    with open("books/frankenstein.txt") as f:
        # Read the file, store it into a workable var
        file_contents = f.read()

    # Run the function to count words
    total_words = word_count(file_contents)
    # Run the function to count chars
    total_chars = count_characters(file_contents)

    # Print the outcome of my function(s)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document")
    
    for item in total_chars:
        print(f"The {item['char']} character was found {item['num']} times")
    print("--- End report ---")
    
def count_characters(string_contents):
    char_count_dict = {}
    char_count_list = []

    # First lower-case the whole strong
    lower_case_string = string_contents.lower()
    # Iterate over the total lower_case_string and count/store it in a Dictionary
    for char in lower_case_string:
        if char in char_count_dict and char.isalpha():
            char_count_dict[char] += 1
        elif char not in char_count_dict and char.isalpha():
            char_count_dict[char] = 1
    
    # Convert dictionary of chars to list of dictionaries:
    for char in char_count_dict:
        char_count_list.append({"char":char,"num":char_count_dict[char]})

    # A function that takes a dictionary and returns the value of the "num" key
    # This is how the `.sort()` method knows how to sort the list of dictionaries
    def sort_on(dict):
        return dict["num"]
    
    # Then sort with the func above and return the list...
    char_count_list.sort(reverse=True, key=sort_on)

    return char_count_list

def word_count(string_contents):
    # Split the file contents into words
    words = string_contents.split()
    
    # Count the number of words
    word_count = len(words)
    

    return word_count
    
main()