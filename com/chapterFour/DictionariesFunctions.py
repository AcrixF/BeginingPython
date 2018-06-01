from copy import  deepcopy;

print('<><><><><><><><><><><deepCopy><><><><><><><><><><><>');

x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']};

y = x.copy();

print('X: ' , x );
print('Y: ', y );

y['username'] = 'mlh';

y['machines'].remove('bar');

print('X: ' , x );
print('Y: ', y );

d = {};

d['names'] = ['Alfred', 'Bertrand'];


c = d.copy();

print( 'd:' , d);
d['names'] = ['Alfred', 'Bertrand']
print( 'c: ', c);

dc = deepcopy( d );

d['names'].append('Clive');

print( c );

print( d );

print( dc );


print('<><><><><><><><><><><fromKeys><><><><><><><><><><><>');

x = {}.fromkeys(['names','ages']);

print( x );

print('<><><><><><><><><><><fromKeys setting default values><><><><><><><><><><><>');

y = {}.fromkeys(['names', 'ages'], '(unkwon)');

print( y );


print('<><><><><><><><><><><get><><><><><><><><><><><>');

d = {};
#Error but try with 'get'
#print( d['name'] );

print( "Default value: " , d.get('name') );

print("Default Value setting:", d.get('name','N/A'));

d ['name'] = 'Erick';

print( d.get('name') );

print('<><><><><><><><><><><items><><><><><><><><><><><>');

d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}

print( d .items() );

it = d.items();

print( len( it ) );

print( ('spam', 0) in it );