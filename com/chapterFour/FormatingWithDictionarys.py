phonebook = { 'Alice': '2341', 'Beth': '9102', 'Cecil': '3258' };

print( "Cecil's number  is {Cecil}.".format_map( phonebook ) );

d = {};

print( d );

d['name'] = 'Gumby';

d['age'] = 42;

print( d );

returned_value = d.clear();

print( d );

print( returned_value );


x = {};

y = x;

x['key'] = 'value';

print( y );

x = {};

print( 'X:' , x );

x.clear();

print( 'Y:' , y );


x = {};

y = x;

x['key'] = 'value';

print('X: ' ,  x);

print('Y: ' , y );

x.clear();

print('X: ' ,  x);

print('Y: ' , y );


