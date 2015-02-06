

def remove_html_markup(data):
    tag = False
    out = []

    for char in data:
        if char == '<':
            tag = True
        elif char == '>':
            tag = False
        elif not tag:
            out.append(char)

    return ''.join(out)


def main():
    data = input("Enter html data: ")
    value = remove_html_markup(data)
    print ("Data is: %s" % value)


if __name__ == '__main__':
    main()
