var n = 9;
var h = [8, 8, 5, 7, 9, 8, 7, 4, 8];

var result = 0;

function solution(h) {
    if (h.length === 0) {
        return 0;
    }

    if (h.length === 1) {
        return 1;
    }

    var result = 1;

    var min = h[0];
    var indx = [0];
    for (var i = 1; i < h.length; i++) {
        if (h[i] < min) {
            min = h[i];
            indx = [i];
        } else if (h[i] === min) {
            indx.push(i);
        }
    }

    var lst = -1;
    for (var i = 0; i < indx.length; i++) {
        result += solution(h.slice(lst + 1, indx[i]));
        lst = indx[i];
    }
    result += solution(h.slice(lst + 1, h.length));

    return result;
}

console.log(solution(h))