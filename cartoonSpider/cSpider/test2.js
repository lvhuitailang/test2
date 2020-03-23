function base64decode(str) {
    var base64EncodeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var base64DecodeChars = new Array(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1);
    var c1, c2, c3, c4;
    var i, len, out;
    len = str.length;
    i = 0;
    out = "";
    while (i < len) {
        do {
            c1 = base64DecodeChars[str.charCodeAt(i++) & 255]
        } while (i < len && c1 == -1);
        if (c1 == -1) {
            break
        }
        do {
            c2 = base64DecodeChars[str.charCodeAt(i++) & 255]
        } while (i < len && c2 == -1);
        if (c2 == -1) {
            break
        }
        out += String.fromCharCode((c1 << 2) | ((c2 & 48) >> 4));
        do {
            c3 = str.charCodeAt(i++) & 255;
            if (c3 == 61) {
                return out
            }
            c3 = base64DecodeChars[c3]
        } while (i < len && c3 == -1);
        if (c3 == -1) {
            break
        }
        out += String.fromCharCode(((c2 & 15) << 4) | ((c3 & 60) >> 2));
        do {
            c4 = str.charCodeAt(i++) & 255;
            if (c4 == 61) {
                return out
            }
            c4 = base64DecodeChars[c4]
        } while (i < len && c4 == -1);
        if (c4 == -1) {
            break
        }
        out += String.fromCharCode(((c3 & 3) << 6) | c4)
    }
    return out
};
var ret_classurl = '/mh/419/';
var comicname = "一人之下";
var viewid = "286719";
var viewtype = "1";
var viewname = "438";
var photosr = new Array();
packed = "ZXZhbChmdW5jdGlvbihwLGEsYyxrLGUsZCl7ZT1mdW5jdGlvbihjKXtyZXR1cm4oYzxhPycnOmUocGFyc2VJbnQoYy9hKSkpKygoYz1jJWEpPjM1P1N0cmluZy5mcm9tQ2hhckNvZGUoYysyOSk6Yy50b1N0cmluZygzNikpfTtpZighJycucmVwbGFjZSgvXi8sU3RyaW5nKSl7d2hpbGUoYy0tKXtkW2UoYyldPWtbY118fGUoYyl9az1bZnVuY3Rpb24oZSl7cmV0dXJuIGRbZV19XTtlPWZ1bmN0aW9uKCl7cmV0dXJuJ1xcdysnfTtjPTF9O3doaWxlKGMtLSl7aWYoa1tjXSl7cD1wLnJlcGxhY2UobmV3IFJlZ0V4cCgnXFxiJytlKGMpKydcXGInLCdnJyksa1tjXSl9fXJldHVybiBwfSgnY1sxXT0iZC9lL2IvZi9hL24uZy8wIjtjWzJdPSJkL2UvYi9mL2EvbS5nLzAiO2NbM109ImQvZS9iL2YvYS9wLmcvMCI7Y1s0XT0iZC9lL2IvZi9hL3EuZy8wIjtjWzVdPSJkL2UvYi9mL2EvbC5nLzAiO2NbNl09ImQvZS9iL2YvYS9pLmcvMCI7Y1s3XT0iZC9lL2IvZi9hL2guZy8wIjtjWzhdPSJkL2UvYi9mL2Evai5nLzAiO2NbOV09ImQvZS9iL2YvYS9rLmcvMCI7Y1tvXT0iZC9lL2IvZi9hL3IuZy8wIjtjW2FdPSJkL2UvYi9mL2EvQi5nLzAiO2NbYl09ImQvZS9iL2YvYS95LmcvMCI7Y1tBXT0iZC9lL2IvZi9hL3guZy8wIjtjW3NdPSJkL2UvYi9mL2EvdS5nLzAiO2Nbdl09ImQvZS9iL2YvYS93LmcvMCI7Y1t0XT0iZC9lL2IvZi9hL3ouZy8wIjsnLDM4LDM4LCd8fHx8fHx8fHx8MTF8MTJ8cGhvdG9zcnxpbWFnZXN8MjAxOXwwOXxqcGd8MTNmYjExMTY0ZXwxM2Y3M2RjYjljfDEzZTljNjI0NDJ8MTNkNmZkYzQ0YXwxMzY4NDQ2MTkxfDEzNWY4NDBmMDh8MTNmZmZmNzYzYXwxMHwxMzQ1NTk3YzI3fDEzNTdkYWQzMzF8MTNlODM0NDdkZXwxNHwxNnwxMzMwM2MyN2ZlfDE1fDEzYmI3NjYzZGV8MTNmN2IyNjMxZnwxM2FiMDI0MTQ4fDEzYmJjMjZhNWZ8MTN8MTMyMTM3NTI0Yycuc3BsaXQoJ3wnKSwwLHt9KSkK";
eval(eval(base64decode(packed).slice(4)));
var maxpages = photosr.length - 1;