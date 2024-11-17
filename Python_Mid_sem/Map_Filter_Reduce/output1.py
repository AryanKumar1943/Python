def nMatchedChar(str1, str2):
    temp1 = str1.lower()  # Convert str1 to lowercase
    temp2 = str2.lower()  # Convert str2 to lowercase
    count = 0
    for ch1 in temp1:
        for ch2 in temp2:
            if ch1 == ch2:
                count += 1
    return count

def main():
    name1 = 'Ram Rahim'
    name2 = 'SAMARTHA RAHI'
    print(nMatchedChar(name1, name2))

if __name__ == '__main__':
    main()
