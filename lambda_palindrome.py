def run():
    word = input('Write a word: ')
    palindrome = lambda string: string == string[ :: -1]
    if palindrome(word):
        print( word + ' is a palindrome word')
    else:
        print( word + ' is not a palindrome word')

if __name__ == '__main__':
    run()