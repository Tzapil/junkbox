var a = readline().split(' ');
var n = a[0];
var m = a[1];

write(Math.pow((2 << m - 1) - 1, n));
write('\n');