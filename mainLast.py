class WebPage:
    def __init__(self, title, info, date):
        self.title = title
        self.info = info
        self.date = date

    def __str__(self):
        return f"Title: {self.title}\nInformation: {self.info}\nDate: {self.date}\n"


class WebSite:
    _webpages = []

    def __init__(self, name, URL):
        self.name = name
        self.URL = URL

    def show_info(self):
        print(f"Name: {self.name}\nURL: {self.URL}\n")

        for value in self._webpages:
            print(value)

    def add_page(self):
        webpage = WebPage(input("Enter title of page: "), input("Enter information on page: "), input("Enter date of publication: "))

        self._webpages.append(webpage)

    def delete_page(self):
        title = input("Enter title of page to delete: ")

        for value in self._webpages:
            if title == value.title:
                self._webpages.remove(value)
                return

        print(f"There are not any pages with title '{title}'")


w = WebSite("WebSite", f"file:///C:/Users/user/Downloads/%D0%9F%D0%97_%D0%9C%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_17_%D0%9F%D1%96%D0%B4%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%BD%D1%8F%20%D0%BF%D1%96%D0%B4%D1%81%D1%83%D0%BC%D0%BA%D1%96%D0%B2.%20%D0%86%D1%81%D0%BF%D0%B8%D1%82.pdf")

while True:
    choice = int(input("Enter your choice (1 - add page, 2 - delete page, 3 - show all pages, 0 - out): "))

    match choice:
        case 1:
            w.add_page()

        case 2:
            w.delete_page()

        case 3:
            w.show_info()

        case 0:
            print("See you soon !")
            break
