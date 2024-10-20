def format_strings(*args):
    combined_string =''.join(args) # โดนให้ตัวแปรเท่ากับผลลัพธ์ทั้งหมดมารวมกัน
    formatted_string = combined_string.upper() # แล้วให้2ตัวแปรเท่ากันแล้วให้ตัวเป็นพิมพ์ใหญ่ทุกตัว
    if '' in combined_string: #เงื่อนไขถ้ามีช่องว่างในตัวแปร
        formatted_string=formatted_string.replace(' ','-') # ให้ตัวแปรเท่ากันแล้วถ้ามีช่องว่างก็ให้แทนที่ด้วยขีด
    return formatted_string # ให้ฟังก์ชันสามารถทำงานได้
    
if __name__ == '__main__':
    result = format_strings("Hello", "world", "this", "is", "a", "test")
    print(result)  # Output: "HELLOWORLDTHISISATEST"

    result = format_strings("Python", "is", "fun")
    print(result)  # Output: "PYTHONISFUN"

    result = format_strings("Hello world")
    print(result)  # Output: "HELLO-WORLD"
