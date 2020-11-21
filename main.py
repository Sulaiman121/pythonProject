from operator import itemgetter
#Method
def All_Members_Analysis():

 PagesNum = 0;
 booksNum= 0;
 CategoriesRank = [];
 MemberBookRank = [];
 MemberPagesRank = [];
 for membr in members:
    MemberBookRank.append((membr.Name,len(membr.books)));
    totalPages=0;
    for book in membr.books:
        totalPages += int(book.NumberOfPages);
        PagesNum += int (book.NumberOfPages);
        booksNum += 1;
        check = False;
        totalAppear= '';
        O = {};
        if len(CategoriesRank)>0:
            for cat in CategoriesRank:
              if cat[0] == book.Category:
                    O=cat;
                    totalAppear=str(int(cat[1])+1);
                    check=True;
                    break;

        if check == False:
           CategoriesRank.append((book.Category,'1'));
        else:
            CategoriesRank.remove(O);
            CategoriesRank.append((book.Category,totalAppear));

            check=False;
    MemberPagesRank.append((membr.Name,str(totalPages)));




 print ('Number of books read by the whole group members : '+str(booksNum));
 print ('Number of pages read by the whole group members : '+str(PagesNum));

 print ('Ranking of books categories mostly read by the group members : ')
 sorted (CategoriesRank, key=itemgetter(1));
 for c in reversed(CategoriesRank):
    print('                                               ',c);

 print ('Ranking of group members based on number of books read : ')
 sorted (MemberBookRank, key=itemgetter(1));
 for c in reversed(MemberBookRank):
    print('                                               ',c);

 print ('Ranking of group members based on number of pages read : ')
 sorted (MemberPagesRank, key=itemgetter(1));
 for c in reversed(MemberPagesRank):
    print('                                               ',c);





"""
CLASSES
"""

#class book
class Book:
  def __init__(self, Id, title,NumberOfPages,Category):
    self.Id = Id
    self.title = title
    self.NumberOfPages = NumberOfPages
    self.Category = Category

#class Member
class Member:
  def __init__(self, Id, Name,Mobile,Email,books):
    self.Id = Id
    self.Name = Name
    self.Mobile = Mobile
    self.Email = Email
    self.books =books;


# start Program here
lines = [line.rstrip('\n') for line in open('data.txt')]
books=[];
members=[]
i=0;
memberID="";
memberNAME="";
memberMOBILE="";
memberEMAIL="";
print();
print("statistical reports about the group : ")
print();
while i < len(lines):
    mline=lines[i].split(' ');
    if mline[0]=='Member':
        memberID=mline[1].strip();
        i+=1;
        mline = lines[i].split(':');
        memberNAME=mline[1].strip();
        i += 1;
        mline = lines[i].split (':');
        memberMOBILE = mline[1].strip();
        i += 1;
        mline = lines[i].split (':');
        memberEMAIL = mline[1].strip();
        i+=2;
    elif mline[0]=='Book':
        bookID = mline[1].strip();
        i += 1;
        mline = lines[i].split (':');
        bookTitle = mline[1].strip();
        i += 1;
        mline = lines[i].split (':');
        bookNUMOFPAGES = mline[1].strip();
        i += 1;
        mline = lines[i].split(':');
        bookCATEGORY = mline[1].strip();
        book = Book (bookID, bookTitle, bookNUMOFPAGES, bookCATEGORY);
        books.append(book);
        i+=2
        if i<len(lines):
            mline = lines[i].split(' ');
            if mline[0]=='Member':
              member=Member(memberID,memberNAME,memberMOBILE,memberEMAIL,books)
              members.append(member)
              books = [];
        else:
            member = Member (memberID, memberNAME, memberMOBILE, memberEMAIL, books)
            members.append (member)
            break;


All_Members_Analysis();




