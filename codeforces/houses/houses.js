var n = +(readline());
write(n);
write('\n');
var houses = readline().split(' ');

write(houses);
write('\n');
function search() {
    var step = 1;
    while (step <= n) {
        for (var i = 0; i < step; i++) {
            if (houses[i] != houses[i + (n - step)]) {
                return n - step
            }
        }
    }
    return 0;
}

write(search());
write('\n');