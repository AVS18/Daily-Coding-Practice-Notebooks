#create a list with 5 tuples and perform the below operations
def get_reshuffled(li):
    return [(item[1],item[2],item[0]) for item in li]
def sorted_key(li,index):
    return sorted(li,key=lambda x: x[index])
li=[('a brief history of time',2000,800),('Intro to Django',2014,1200),('bhagavan Rough Notes',1965,20),('Spiral Notes',1800,200),('introduction to Python',1995,2200)]
print('Original List\n',li,'\n',sep='\n')
#sorting based on name of the book
li_name=sorted_key(li,0)
print('Sorting based on name of the book\n',li_name,'\n',sep='\n')
#reshuffling to have the tuples as ('published year','price','bookname')
li_name_reshuffle=get_reshuffled(li_name)
print('Sorted and Reshuffled list based on name of the book\n',li_name_reshuffle,'\n',sep='\n')
#sorting based on price of the book
li_price=sorted_key(li,2)
print('Sorting based on price of the book\n',li_price,'\n',sep='\n')
#reshuffling to have the tuples as ('published year','price','bookname')
li_price_reshuffle=get_reshuffled(li_price)
print('Sorted and Reshuffled list based on price of the book\n',li_price_reshuffle,sep='\n')
