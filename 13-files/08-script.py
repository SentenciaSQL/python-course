js_code = """
console.log('Hello World desde JS');
function suma(a,b) {
    return a+b;
}
"""

with open("script.js", "w") as file:
    file.write(js_code)