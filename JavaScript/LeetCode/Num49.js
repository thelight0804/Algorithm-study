/**
 * Date: 23.09.09
 * Number: LeetCode 49
 * Title: Group Anagrams
 * Level: Medium
 * Author: thelight0804
 */

// sort + hash table
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    if (strs.length < 2) return [strs]; // 1

    // initialize hash table 2
    var map = new Map();
	
		// 3
    strs.forEach(e => {
        // sort string
        var str = e.split("").sort().join("");

        // add string to value in hash table 4
        if (map.get(str)){
            var arr = map.get(str);
            arr.push(e);
            map.set(str, arr);
        }
        // add new key to hash table 5
        else {
            map.set(str, [e]);
        }
    })
    
    // convert values in hash table to array 6
    return Array.from(map.values());
};


// alphabet counting + hash table
var groupAnagrams = function (strs) {
    if (strs.length < 2) return [strs];

    // initialize hash table
    var map = new Map();

    strs.forEach(str => {
        var char = str.split("");
        var count = createTable();
        var key = "";

        // add alphabet count
        char.forEach(e => {
            count[e]++;
        })

        // create string key
        for (var val in count) {
            if (count[val] > 0) {
                var a = val + count[val].toString();
                key += a;
            }
        }

        // add key of hash map
        if (map.get(key)) {
            var arr = map.get(key);
            arr.push(str);
            map.set(key, arr);
        }
        else {
            map.set(key, [str]);
        }
    })
    console.log(map);

    // convert values in hash table to array
    return Array.from(map.values());
};

// create alphabet hash table
function createTable() {
    var alphabet = {
        a: 0,
        b: 0,
        c: 0,
        d: 0,
        e: 0,
        f: 0,
        g: 0,
        h: 0,
        i: 0,
        j: 0,
        k: 0,
        l: 0,
        m: 0,
        n: 0,
        o: 0,
        p: 0,
        q: 0,
        r: 0,
        s: 0,
        t: 0,
        u: 0,
        v: 0,
        w: 0,
        x: 0,
        y: 0,
        z: 0
    }

    return alphabet;
}