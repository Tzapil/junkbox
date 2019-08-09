var q = +readline();

for(var i = 0; i < q; i++) {
    var arr = readline().split(' ').map(x => +x);
    var k = arr[0];
    var n = arr[1]
    var a = arr[2];
    var b = arr[3];

    if (b * n >= k) {
        write(-1, '\n');
    } else if (a * n < k) {
        write(n, '\n');
    } else {
        var x = (k - b*n) / (a - b);

        write(Math.floor(x), '\n');
    }
}