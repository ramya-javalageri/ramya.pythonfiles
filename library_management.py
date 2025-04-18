# class library:
#     books=['b1','b2','b3','b4']
#     def display_books(self):
#         print(self.books)
#     def lend_books(self,a):
#         if a in self.books:
#             self.books.remove(a)
#         else:
#             print("Not available")
#         # print(self.books)
#     def add_book(self,b):
#         self.books.append(b)
#         # print(self.books)
#     def return_books(self,c):
#         self.books.append(c)
#         # print(self.books)
# obj=library()
# obj.display_books()
# obj.add_book(input("Enter a book to add:"))
# obj.return_books(input("Enter a book you want to return:"))
# obj.lend_books(input("enter a book you want:"))
# obj.display_books()

# ,,,,,,,,,,,,,,,,,,,,,,,,,
class library:
    dic={'a':5,'b':5,'c':0,'d':10}
    # l=dic.values()
    # print(l)
    def __init__(self):
        print(self.dic)
    def display_books(self):
        print("available Books are:")
        print("Book_name-Count")
        for i,j in self.dic.items():
            print(f'   {i}     -   {j}')
    def add_books(self,book_name):
        if book_name in self.dic:
            self.dic.update({book_name:self.dic[book_name]+1})
        else:
            self.dic.update({book_name:1})
        # print(self.dic)
    def lend_books(self,book_name):
        if book_name in self.dic and self.dic[book_name]!=0:
            self.dic.update({book_name: self.dic[book_name] - 1})
        else:
            print("Book in currently unavailable")
        # print(self.dic)
    def return_book(self,book_name):
        self.dic.update({book_name: self.dic[book_name] +1})
        # print(self.dic)


o=library()
o.display_books()
o.add_books(input("Enter a book name to add:").lower())
o.display_books()
o.lend_books(input("Enter a book name you want to barrow:").lower())
o.display_books()
o.return_book(input("Enter a book name you want to return:").lower())
o.display_books()
