diff([
    {id: 1, info: "foo"},
    {id: 2, info: "bar"},
    {id: 3, info: "foobar"}
  ], 
  [
    {id: 2, info: "bar"},
    {id: 3, info: "foo_bar"},
    {id: 4, info: "foo"},
  ], 
  "id"
);

function isEqual(obj1, obj2) {
    if (Object.keys(obj1).length !== Object.keys(obj2).length) {
        return false;
    }

    let equal = true;
    for (let key in obj1) {
        if (obj1.hasOwnProperty(key)) {
            if (obj1[key] !== obj2[key]) {
                equal = false;
                break
            }
        }
    }

    return equal;
}

function diff(arr1, arr2, key) {
    const answer = {
        changed: [],
        added: [],
        removed: []
    };

    arr1.sort((a, b) => a.key > b.key);
    arr2.sort((a, b) => a.key > b.key);

    let i = 0;
    let j = 0;
    while (j < arr2.length && i < arr1.length) {
        if (arr1[i][key] === arr2[j][key]) {
            if (!isEqual(arr1[i], arr2[j])) {
                answer.changed.push([arr1[i], arr2[j]]);
            }
            i++;
            j++;
        } else {
            if (arr1[i][key] < arr2[j][key]) {
                answer.removed.push(arr1[i]);
                i++;
            } else {
                answer.added.push(arr2[j]);
                j++;
            }
        }
    }

    for (let ii = i; ii < arr1.length; ii++) {
        answer.removed.push(arr1[ii]);
    }

    for (let jj = j; jj < arr2.length; jj++) {
        answer.added.push(arr2[jj]);
    }

    return answer;
}