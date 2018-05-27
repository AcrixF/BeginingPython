# Accessing elements
print('################### ACCESING #########################');

x = [1,2,3,4,5];

print( x[1] );

print( x );

# Deleting elements

print('################### DELETING #########################');

names = [ 'Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl' ];

print( names );

del names[ 2 ];

print( names );

# Slices
print('################### SLICES #########################');
name_1 = list('Perl');

print( name_1 );

name_1[2:] = list('ar');

print( name_1 );

name_1 = list('Perl');

print( name_1 );

name_1[1:] = list('ython');

print( name_1 );

numbers = [ 1 , 5 ];

print( numbers );

numbers[1:1] = [ 2, 3, 4 ];

print( numbers );

numbers[1:4] = [];

print( numbers );

# append method
print('################### APPEND #########################');

lst = [ 1, 2, 3 ];

lst.append( 4 );

print( lst );

# clear method
print('################### CLEAR #########################');

lst.clear();

# or

lst[:] = [];

print( lst );

print('################### COPY #########################');

a = [ 1, 2, 3 ];

print( a );

b = a;

print( b);

b[1] = 4;

print( b );

print( a );

b = a.copy();

b[1] = 5 ;

print( b );

print( a );

print('################### COUNT #########################');

words = ['to', 'be', 'or', 'not', 'to', 'be'];

print( words.count( 'or' ) );

x = [[1, 2], 1, 1, [2, 1, [1, 2]]];

print( x.count( [1, 2] ) );

print('################### EXTENDS #########################');

a = [1, 2, 3 ];

b = [4, 5, 6 ];

a.extend( b );

print( a );

print('################### INDEX #########################');

knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni'];

print( 'index of: ' , knights.index( 'who') );

#print( knights.index('all') );

print('################### INSERT #########################');

numbers = [ 1, 2, 3, 4, 5, 6 ];

print( numbers );

numbers.insert( 3 ,'four');

print( numbers );

numbers = [1, 2, 3, 5, 6, 7];

print( numbers );

numbers[3:3] = ['four'];

print( numbers );

print('################### POP #########################');

x = [ 1, 2 ,3 ];

print( x );

print( x.pop() );

print( x );

x.pop( 0 );

print( x );

print('################### REMOVE #########################');

x = ['to', 'be', 'or', 'not', 'to', 'be'];

print( x );

x.remove( 'be' );

print( x );


print('################### REVERSE #########################');

x = [ 1, 2, 3 ];

print( x );

print( x.reverse() );

print('################### SORT #########################');

x = [4, 6, 2, 1, 7, 9];

print( x );

x.sort();

print( x );
