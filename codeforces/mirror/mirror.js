var n = +readline();

var sm = Array.apply(null, Array(n)).map(() => Array(n));
var counters = Array(n).fill(0);

for (var i = 0; i < n; i++) {
    var [x, y] = readline().split('').map(i => +i);
    sm[x, y] = true;

    counters[x]++;
    counters[y]++;
}

counters.sort((a, b) => a - b);