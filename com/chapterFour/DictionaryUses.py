names = [ 'Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl' ];

numbers = ['2341', '9102', '3158', '0142', '5551'];

print( numbers [names.index( 'Cecil') ] );

phonebook = { 'Alice': '2341', 'Beth': '9102', 'Cecil': '3258' };

print( phonebook );

print('<><><><><><><><><><>< dict Function><><><><><><><><><><><>');
#the dict function1 to construct dictionaries from other mappings.
items =  [('name', 'Gumby'), ('age', 42)];

d = dict( items );

print( d );

print(d['name']);

d = dict( name='Gumby', age=42);

print( d );

print( d['age']);