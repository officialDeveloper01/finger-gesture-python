import cv2
from cvzone.HandTrackingModule import HandDetector
import os
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import webbrowser
import warnings
import time 

# Suppress specific warning
warnings.filterwarnings("ignore", message="SymbolDatabase.GetPrototype() is deprecated. Please use message_factory.GetMessageClass() instead. SymbolDatabase.GetPrototype() will be removed soon.")

# Suppress TensorFlow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Initialize hand detector
detector = HandDetector(maxHands=1, detectionCon=0.8)

# Function to create an image with text
def create_image(text, filename):
    img = Image.new('RGB', (220, 280), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    try:
        fnt = ImageFont.truetype('arial.ttf', 100)
    except IOError:
        fnt = ImageFont.load_default()
    bbox = d.textbbox((0, 0), text, font=fnt)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (img.width - text_width) / 2
    y = (img.height - text_height) / 2
    d.text((x, y), text, font=fnt, fill=(0, 0, 0))
    img.save(filename)

# Create images for 0 to 5 fingers up
for i in range(6):
    create_image(str(i), f'finger_{i}.jpg')

# Paths to finger images
finger_images = {
    "0": cv2.imread("finger_0.jpg"),
    "1": cv2.imread("finger_1.jpg"),
    "2": cv2.imread("finger_2.jpg"),
    "3": cv2.imread("finger_3.jpg"),
    "4": cv2.imread("finger_4.jpg"),
    "5": cv2.imread("finger_5.jpg")
}

class HandTrackingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hand Tracking Interface")

        self.start_btn = tk.Button(self.root, text="Start", command=self.start_video)
        self.start_btn.pack()

        self.stop_btn = tk.Button(self.root, text="Stop", command=self.stop_video)
        self.stop_btn.pack()

        self.canvas = tk.Canvas(self.root, width=640, height=480)
        self.canvas.pack()

        self.video = None
        self.running = False
        self.url_opened = False

    def start_video(self):
        self.video = cv2.VideoCapture(0)  # Use 0 for built-in webcam, 1 for external webcam
        self.running = True
        self.update_frame()

    def stop_video(self):
        self.running = False
        if self.video:
            self.video.release()
        cv2.destroyAllWindows()

    def update_frame(self):
        if self.running:
            success, img = self.video.read()
            if success:
                img = cv2.flip(img, 1)
                hands, img = detector.findHands(img, draw=False)  # Get hands and image with hands drawn
                fing = finger_images["0"]
                if hands:
                    hand = hands[0]
                    lmlist = hand["lmList"]
                    if lmlist:
                        fingerup = detector.fingersUp(hand)
                        key = str(sum(fingerup))
                        if key in finger_images:
                            fing = finger_images[key]
                        # Open YouTube if one finger is detected and URL not opened yet
                        if fingerup == [0, 1, 0, 0, 0] and not self.url_opened:
                            webbrowser.open_new_tab("https://www.youtube.com")
                            # self.url_opened = True
                            time.sleep(5)                        
                        if fingerup == [0, 1, 1, 0, 0] and not self.url_opened:
                            webbrowser.open_new_tab("https://instagram.com/kuttyjain")
                            # self.url_opened = True
                            time.sleep(5)
                        if fingerup == [0, 1, 1, 1, 0] and not self.url_opened:
                            webbrowser.open_new_tab("https://linkedin.com/in/kuttyjain")
                            # self.url_opened = True
                            time.sleep(5)
                        if fingerup == [0, 1, 1, 1, 1] and not self.url_opened:
                            webbrowser.open_new_tab("https://portfolio-namanjain.vercel.app")
                            # self.url_opened = True
                            time.sleep(5)
                        if fingerup == [1, 1, 1, 1, 1] and not self.url_opened:
                            webbrowser.open_new_tab("")
                            # self.url_opened = True
                            time.sleep(5)
                    
                    # Check if image was loaded successfully
                if fing is not None:
                    fing = cv2.resize(fing, (220, 280))
                    img[50:330, 20:240] = fing

                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img_pil = Image.fromarray(img_rgb)
                img_tk = ImageTk.PhotoImage(img_pil)    
                self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
                self.canvas.image = img_tk  # Keep a reference to avoid garbage collection

            self.root.after(10, self.update_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = HandTrackingApp(root)
    root.mainloop()