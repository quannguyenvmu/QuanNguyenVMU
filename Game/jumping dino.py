from tkinter import*        	#Khai báo module tkinter
from time import sleep          #Khai báo hàm sleep của module time để set delay
from PIL import ImageTk, Image  #Khai báo thư viện hình ảnh PIL

img=[0,0,0]                    #Mảng để lưu hình ảnh

game=Tk()                      #Tạo một cửa sổ game
game.title("Jumping Dino")     #Đặt tên game
screen=Canvas(master=game,width=750,height=450,background='white')      #screen:Tên biến để set cửa sổ
                                                                       #Canvas():Tên hàm (thông số cửa sổ)
screen.pack()                   #Câu lệnh để đặt màn hình vào trong cửa sổ

img[0] = ImageTk.PhotoImage(Image.open("Photos/dino.jpg"))             # Khai báo các hình ảnh
img[1] = ImageTk.PhotoImage(Image.open("Photos/cloud.jpg"))            # Phải khai báo sau game=Tk()
img[2] = ImageTk.PhotoImage(Image.open("Photos/cactus.jpg"))

text=screen.create_text(375,150,text="WELCOME GAME",fill="cyan",font=("Times",20))  #In chữ ra màn hình ( x, y, nội dung text, màu text, phông text )
dino=screen.create_image(0,350,anchor=NW,image=img[0])
cloud= screen.create_image(700,50,anchor=NW,image=img[1])       #(Toạ độ x,y,định dạng ảnh , gán biến ảnh)
cactus= screen.create_image(700,350,anchor=NW,image=img[2])

screen.update()                 #Update để nhìn thấy khối chữ nhật

def dichuyenmay():                          #Khai báo hàm để di chuyển ảnh mây
    global cloud
    screen.move(cloud,-7.5,0)
    if screen.coords(cloud)[0]<-15:
        screen.delete(cloud)
        cloud = screen.create_image(700, 50, anchor=NW, image=img[1])
    screen.update()

def dichuyencay():                          #Khai báo hàm để di chuyển ảnh cây
    global cactus
    screen.move(cactus,-4,0)
    if screen.coords(cactus)[0]<-15:
        screen.delete(cactus)
        cactus = screen.create_image(700, 350, anchor=NW, image=img[2])
    screen.update()

ktnhay=False

def dichuyenkhunglong(): # Hàm này để di chuyển khủng long
    global ktnhay
    if ktnhay==False:
        ktnhay=True
        for i in range(0,30):
            screen.move(dino,0,-4)
            dichuyenmay()                # Lồng cả 2 lệnh di chuyển mây và cây trong vòng này để lúc khủng long nhảy thì đống này
            dichuyencay()               # vẫn chạy chứ k dừng.
            screen.update()
            sleep(0.01)
        for i in range(0,30):
            screen.move(dino,0,4)
            dichuyenmay()
            dichuyencay()
            screen.update()
            sleep(0.01)
            ktnhay=False

def kiemtraphim(event):                                 # Hàm kiểm tra nếu bấm space thì khủng long mới nhảy
    if event.keysym=="space":
        dichuyenkhunglong()

screen.bind_all("<KeyPress>",kiemtraphim)           # Kiểm tra phím để n

gameover=False        #Khai báo trò chơi kết thúc

while not gameover:                 #Khai báo để di chuyển vật thể
    dichuyenmay()
    dichuyencay()
    sleep(0.01)

game.mainloop()                 #Câu lệnh để game chạy
