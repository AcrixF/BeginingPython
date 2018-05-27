
permission = 'rw';

print( 'w' in permission );

print( 'x' in permission );

users = ['mlh', 'foo', 'bar'];
input('Enter your user name: ' ) in users;

subject = '$$$ Get rich now!!! $$$';
print('$$$' in subject );

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
];

username = input('User name: ');
pin = input('PIN code: ');

if [username, pin] in database : print('Acess granted');