def main():

    upper_vowel = {"A", "E", "I" , "O", "U"}
    lower_vowel = {"a", "e", "i", "o", "u"}

    vowel_string = input("Input:  ")

    for char in range(len(vowel_string)):
        if vowel_string[char] in upper_vowel or vowel_string[char] in lower_vowel:
            vowel_string = vowel_string.replace(vowel_string[char], "~")

    no_vowels = vowel_string.replace("~", "")

    print(f"Output: {no_vowels}")


if __name__ == "__main__":
    main()