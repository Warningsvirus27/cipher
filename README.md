# cipher

The python program is for encryption and decryption of plain text
The algorithm use is as:

Encryption

Here we will add the ascii values of the last 2 character of the string
then the resultant ascii value's equivalent character(special character) is added to the start of the resultant string
The last character is kept as it is, till the end of the iterations follows, 
then finally the last character is added with the first characters ascii value
Hence we will get the fully encrypted string

ex:
suppose the plain text is 'hello'
start      : 'ohello'   ->  last character appended at the start<br>
iteration 1: 'ohel/'    ->  ascii(o) + ascii(l) = '/'<br>
iteration 2: '/ohe{'    ->  ascii(/) + ascii(l) = '{'<br>
iteration 3: '{/oh#'    ->  ascii({) + ascii(e) = '#'<br>
iteration 4: '#{/o!'    ->  ascii(#) + ascii(h) = '!'<br>
finally    : '!#{/&'    ->  ascii(!) + ascii(o) = '&'<br>

so the finaly encrypted string is '!#{/&'

Decryption
The decryption process follows the same as encryption in reverse pattern

ex:
suppose the plain text is '!#{/&'
start      : '!#{/o'    ->  last character replaced with acsii(&) - ascii(!) = o [decryption started from end]<br>
iteration 1: '!#{lo'    ->  ascii(/) + ascii(&) = 'l'<br>
iteration 2: '!#llo'    ->  ascii({) + ascii(/) = 'l'<br>
iteration 3: '!ello'    ->  ascii(#) + ascii({) = 'e'<br>
iteration 4: 'hello'    ->  ascii(!) + ascii(#) = 'h'<br>

so the decrypted string is 'hello'
