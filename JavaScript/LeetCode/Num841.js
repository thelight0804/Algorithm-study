/**
 * Date: 23.07.04
 * Number: LeetCode 841
 * Title: Keys and Rooms
 * Level: Medium
 * Author: thelight0804
 */

var canVisitAllRooms = function (rooms) {
    var seen = new Set(); //visit room
    var visit = 1; //visit count

    function dfs(roomNum, seen) {
        keys = rooms[roomNum]; //keys of now room

        if (keys) {
        for (var key of keys) {
            if (!seen.has(key)) {
            visit++;
            dfs(key, seen.add(key));
            }
        }
        }
    }

    //first call dfs
    dfs(0, seen.add(0));

    return visit === rooms.length;
};
