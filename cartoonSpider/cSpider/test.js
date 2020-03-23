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


function getResult(base64Code){
    var photosr = new Array();
    packed = "ZXZhbChmdW5jdGlvbihwLGEsYyxrLGUsZCl7ZT1mdW5jdGlvbihjKXtyZXR1cm4oYzxhPycnOmUocGFyc2VJbnQoYy9hKSkpKygoYz1jJWEpPjM1P1N0cmluZy5mcm9tQ2hhckNvZGUoYysyOSk6Yy50b1N0cmluZygzNikpfTtpZighJycucmVwbGFjZSgvXi8sU3RyaW5nKSl7d2hpbGUoYy0tKXtkW2UoYyldPWtbY118fGUoYyl9az1bZnVuY3Rpb24oZSl7cmV0dXJuIGRbZV19XTtlPWZ1bmN0aW9uKCl7cmV0dXJuJ1xcdysnfTtjPTF9O3doaWxlKGMtLSl7aWYoa1tjXSl7cD1wLnJlcGxhY2UobmV3IFJlZ0V4cCgnXFxiJytlKGMpKydcXGInLCdnJyksa1tjXSl9fXJldHVybiBwfSgnZVsxXT0iYy9iL2EvZC9mL28uZy8wIjtlWzJdPSJjL2IvYS9kL2YvcC5nLzAiO2VbM109ImMvYi9hL2QvZi9yLmcvMCI7ZVs0XT0iYy9iL2EvZC9mL24uZy8wIjtlWzVdPSJjL2IvYS9kL2Yvcy5nLzAiO2VbNl09ImMvYi9hL2QvZi9sLmcvMCI7ZVs3XT0iYy9iL2EvZC9mL2guZy8wIjtlWzhdPSJjL2IvYS9kL2YvaS5nLzAiO2VbOV09ImMvYi9hL2QvZi9tLmcvMCI7ZVtqXT0iYy9iL2EvZC9mL2suZy8wIjtlW3FdPSJjL2IvYS9kL2YvdC5nLzAiO2VbQ109ImMvYi9hL2QvZi9CLmcvMCI7ZVtEXT0iYy9iL2EvZC9mL0UuZy8wIjtlW0ZdPSJjL2IvYS9kL2Yvei5nLzAiO2VbQV09ImMvYi9hL2QvZi92LmcvMCI7ZVt1XT0iYy9iL2EvZC9mL3cuZy8wIjtlW3hdPSJjL2IvYS9kL2YveS5nLzAiOycsNDIsNDIsJ3x8fHx8fHx8fHwwM3wyMDIwfGltYWdlc3wwNXxwaG90b3NyfDA2fGpwZ3w0MWJjZTRkZjQ5fDQxMTg4OWRhMjV8MTB8NDE3YTU1YTQyOHw0MThkNWZlZjMwfDQxZGI4Mzg1ZDd8NDE1MDdlMmJmNnw0MTYxMWM4Zjk4fDQxZGYwYjU2NTZ8MTF8NDFlMTMzMzU2Ynw0MTA0ZTQxN2ZifDQxYmVjNzA1MjR8MTZ8NDFkZWYwM2NjM3w0MWY2YzRkNmQ5fDE3fDQxNDllYzU5ZDh8NDE3ZTIwZjI3N3wxNXw0MTQ4YTgwMzE4fDEyfDEzfDQxYzJmYjNiNWF8MTQnLnNwbGl0KCd8JyksMCx7fSkpCg==";
    eval(eval(base64decode(packed).slice(4)));

    return photosr;
}