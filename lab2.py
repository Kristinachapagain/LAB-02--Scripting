def main(): 
    about_myself = { 
        'fullname' : 'kristina chapagain',
        'studentid' : '10284340.', 
  
        'my_fav_topings' : [
            'PEPPRONI', 
            'CHICKEN'
            'HAM AND PINEAPPLE'
        ], 

      'my_fav_movies' : [
        
        {'title':'three idiots' , 'genre' : 'comedy'},
        {'title':'the dark knight' ,'genre' : 'action'},
        {'title':'stranger things' ,'genre': 'supernatural'}
        
      ]
    }
    def print_about_myself(information): 

        full_name = information ['fullname']
        firstname = full_name.split()
        studentid = information['studentid']
        print(f'My full name is {full_name},but you can call me Ms {firstname[0]}.')
        print(f'My student id is {studentid}')

        #add another topings
        fav_topings = ['sausage','pepper','mushroom']
        about_myself['my_fav_topings'].append(fav_topings)
        print_my_fav_topings(fav_topings)

    def print_my_fav_topings(fav_topings):
        print ('My favourite pizza_topings are:')
        for toping in enumerate(fav_topings):
            print (f'* {toping[1]}')
        

    def print_movie_genre(genre):
        genre_string=list()
        for items in genre[0].values():
            genre_string.append(items)
        genre_string1=list()
        for items in genre[1].values():
            genre_string1.append(items)
        genre_string2=list()
        for items in genre[2].values():
            genre_string2.append(items)
        
        print(f'I am fond of watching {genre_string[1]},{genre_string1[1]} and {genre_string2[1]} movies.')

    def print_movie_titles(genre):
        genre_string=list()
        for items in genre[0].values():
            genre_string.append(items)
        genre_string1=list()
        for items in genre[1].values():
            genre_string1.append(items)
        genre_string2=list()
        for items in genre[2].values():
            genre_string2.append(items)
        
        print("list of my favourite movies are:")
        print(genre_string[0])
        print(genre_string1[0])
        print(genre_string2[0])
    print_about_myself(about_myself)
    print_movie_genre(about_myself['my_fav_movies'])
    print_movie_titles(about_myself['my_fav_movies'])

if __name__ == '__main__':
   main() 