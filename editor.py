
function = ["!help", "!done", "plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
markdown = []

def create_list(x):
    row = int(input("- Number of rows: "))
    while row < 1:
        print("The number of rows should be greater than zero")
        row = int(input("- Number of rows: "))
    else:
        if x == "unordered-list":
            temp_list = [input(f"- Row #{i}: ") for i in range(1, row + 1)]
            temp_list = [f"* {i}" for i in temp_list]
            return "\n".join(temp_list)
        else:
            temp_list = [input(f"- Row #{i}: ") for i in range(1, row + 1)]
            temp_list = [f"{temp_list.index(i)+1}. {i}" for i in temp_list]
            return "\n".join(temp_list)


def plain(x):
    return x


def bold(x):
    return f"**{x}**"


def italic(x):
    return f"*{x}*"


def inline_code(x):
    return f"`{x}`"


def header():
    symbol = "#"
    level = int(input("- Level: "))
    text = input("- Text: ")
    while level:
        if 6 >= level >= 1:
            return f"{level * symbol} {text}\n"
        else:
            print("The level should be within the range of 1 to 6")
            level = int(input("- Level: "))


def link():
    label = input("- Label: ")
    url = input("- URL: ")
    return f"[{label}]({url})"


def new_line():
    return "\n"


x = input("- Choose a formatter: ")
while x:
    if x not in function:
        print("Unknown formatting type or command")
        x = input("- Choose a formatter: ")
    if x in function:
        if x == "!done":
            with open("output.md", "w") as f:
                for i in markdown:
                    f.write(i)
            break
        elif x == "!help":
            print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
            print("Special commands: !help !done")
            x = input("- Choose a formatter: ")
        else:
            if x == "plain" or x == "bold" or x == "italic":
                text = input("- Text: ")
                markdown.append(eval(x)(text))
            elif x == "inline-code":
                text = input("- Text: ")
                markdown.append(inline_code(text))
            elif x == "header":
                markdown.insert(0, header())
            elif x == "link":
                markdown.append(link())
            elif x == "new-line":
                markdown.append(new_line())
            elif x == "ordered-list" or x == "unordered-list":
                markdown.append(create_list(x))
                markdown += "\n"

            print("".join(markdown))
            #if x == "ordered-list" or x == "unordered-list":
                #print()


            x = input("- Choose a formatter: ")
