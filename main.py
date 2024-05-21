def countWords(string: str):
    return len(string.split())

def letterCounts(string: str):
    letterCounts={}
    for x in string:
        x=x.lower()
        if letterCounts.get(x) !=None:
            letterCounts[x]=letterCounts[x]+1
        else:
            letterCounts[x]=1
    return letterCounts

def sort_on(dict):
    return dict["num"]

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt","r") as f:
        file_contants=f.read()
        words = countWords(file_contants)
        print(f"{words} words found in the document\n")
        letter_counts=letterCounts(file_contants)
        letter_count_list=[]
        for letter in letter_counts.keys():
            if letter.isalpha():
                letter_count_list.append({
                    "name":letter,"num":letter_counts[letter]
                })
        letter_count_list.sort(reverse=True,key=sort_on)
        for item in letter_count_list:
            print(f"The '{item["name"]}' character was found {item["num"]} times")
        print("--- End report ---")


main()