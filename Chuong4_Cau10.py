#Câu 10: Vẽ hình dùng Sleep
'''
Yêu cầu:
Vẽ 4 hình dưới đây, dùng sleep để xuất hiện từng hình sau 5 giây
                                 
            *
            *  *
            *  *  *
   *  *  *  *  *  *  *
   *  *  *
   *  *
   *

            *
            *  *
            *     *
   *  *  *  *  *  *  *
   *     *
   *  *
   *

         *  *  *  *
         *  *  *
         *  *
         *
      *  *
   *  *  *
*  *  *  *

         *  *  *  *
         *     *
         *  *
         *
      *  *
   *     *
*  *  *  *
'''
import time
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#Hình 1
def draw_shape_1():
    print("            *")
    print("            *  *")
    print("            *  *  *")
    print("   *  *  *  *  *  *  *")
    print("   *  *  *")
    print("   *  *")
    print("   *")
#Hình 2
def draw_shape_2():
    print("            *")
    print("            *  *")
    print("            *     *")
    print("   *  *  *  *  *  *  *")
    print("   *     *")
    print("   *  *")
    print("   *")
#Hình 3
def draw_shape_3():
    print("         *  *  *  *")
    print("         *  *  *")
    print("         *  *")
    print("         *")
    print("      *  *")
    print("   *  *  *")
    print("*  *  *  *")
#Hình 4
def draw_shape_4():
    print("         *  *  *  *")
    print("         *     *")
    print("         *  *")
    print("         *")
    print("      *  *")
    print("   *     *")
    print("*  *  *  *")
# Hiển thị từng hình sau 5 giây
if __name__ == "__main__":
    draw_shape_1()
    time.sleep(5)
    clear_screen()
    draw_shape_2()
    time.sleep(5)
    clear_screen()
    draw_shape_3()
    time.sleep(5)
    clear_screen()
    draw_shape_4()
    time.sleep(5)