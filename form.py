import math

# สร้าง List สำหรับเก็บประวัติการคำนวณ
history = []

print("=== ยินดีต้อนรับสู่โปรแกรมคำนวณพื้นที่อัจฉริยะ ===")

while True:
    print("\n------------ เมนูหลัก ------------")
    print("1. รูปสี่เหลี่ยมมุมฉาก (ผืนผ้า)")
    print("2. รูปสี่เหลี่ยมจัตุรัส")
    print("3. รูปสามเหลี่ยม")
    print("4. รูปวงกลม")
    print("5. รูปสี่เหลี่ยมคางหมู")
    print("6. ดูประวัติการคำนวณ")
    print("7. ออกจากโปรแกรม")
    print("---------------------------------")
    
    choice = input("กรุณาเลือกเมนู (1-7): ")
    
    # 1. สี่เหลี่ยมมุมฉาก
    if choice == '1':
        width = float(input("ใส่ความกว้าง: "))
        length = float(input("ใส่ความยาว: "))
        area = width * length
        result_text = f"สี่เหลี่ยมมุมฉาก (กว้าง {width} x ยาว {length}) = {area:.2f} ตร.หน่วย"
        print(f"-> พื้นที่คือ: {area:.2f}")
        history.append(result_text)
        
    # 2. สี่เหลี่ยมจัตุรัส
    elif choice == '2':
        side = float(input("ใส่ความยาวด้าน: "))
        area = side * side
        result_text = f"สี่เหลี่ยมจัตุรัส (ด้าน {side}) = {area:.2f} ตร.หน่วย"
        print(f"-> พื้นที่คือ: {area:.2f}")
        history.append(result_text)
        
    # 3. สามเหลี่ยม
    elif choice == '3':
        base = float(input("ใส่ความยาวฐาน: "))
        height = float(input("ใส่ความสูง: "))
        area = 0.5 * base * height
        result_text = f"สามเหลี่ยม (ฐาน {base} x สูง {height}) = {area:.2f} ตร.หน่วย"
        print(f"-> พื้นที่คือ: {area:.2f}")
        history.append(result_text)
        
    # 4. วงกลม
    elif choice == '4':
        radius = float(input("ใส่ความยาวรัศมี (r): "))
        area = math.pi * (radius ** 2)
        result_text = f"วงกลม (รัศมี {radius}) = {area:.2f} ตร.หน่วย"
        print(f"-> พื้นที่คือ: {area:.2f}")
        history.append(result_text)
        
    # 5. สี่เหลี่ยมคางหมู
    elif choice == '5':
        height = float(input("ใส่ความสูง: "))
        side1 = float(input("ใส่ความยาวด้านคู่ขนานที่ 1: "))
        side2 = float(input("ใส่ความยาวด้านคู่ขนานที่ 2: "))
        area = 0.5 * height * (side1 + side2)
        result_text = f"สี่เหลี่ยมคางหมู (สูง {height}, ผลรวมด้านคู่ขนาน {side1+side2}) = {area:.2f} ตร.หน่วย"
        print(f"-> พื้นที่คือ: {area:.2f}")
        history.append(result_text)
        
    # 6. ดูประวัติการใช้งาน
    elif choice == '6':
        print("\n===== ประวัติการคำนวณ =====")
        if len(history) == 0:
            print("ยังไม่มีประวัติการคำนวณในระบบ")
        else:
            for i, record in enumerate(history, 1):
                print(f"{i}. {record}")
        print("==========================")
        
    # 7. ออกจากโปรแกรม
    elif choice == '7':
        print("ขอบคุณที่ใช้งานโปรแกรม! บ๊ายบายครับ/ค่ะ")
        break
        
    else:
        print("คำเตือน: เลือกเมนูไม่ถูกต้อง กรุณาเลือกพิมพ์เลข 1-7 เท่านั้น")