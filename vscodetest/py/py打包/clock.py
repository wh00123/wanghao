import time
import tkinter as tk


class Clock(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # 设置窗口初始位置
        self.x, self.y = 0, 0
        # 设置窗口初始大小
        self.window_size = '265x30'
        # 设置窗口置顶
        self.attributes("-topmost", 1)
        # 初始化时间字符串
        self.time_text = ""
        # 去掉标题栏
        self.overrideredirect(1)
        # 设置透明度(取值范围:[0,1])
        self.attributes("-alpha", 0.4)
        # 添加窗口移动事件
        self.bind("<B1-Motion>", self.move)
        # 设置字符标签
        self.lbl = tk.Label(self,
                            # 文本内容是时间字符串
                            text=self.time_text,
                            # 设置字体大小及格式
                            font=("ds-digital", 20),
                            # 设置背景色
                            background="black",
                            # 设置字体颜色
                            foreground="cyan")
        # 添加到窗口
        self.lbl.pack()
        # 更新时间
        self.update_time()

    def move(self, event):
        """窗口移动事件"""
        self.geometry(
            f"{self.window_size}+{(event.x - self.x) + self.winfo_x()}+{(event.y - self.y) + self.winfo_y()}")

    def update_time(self):
        # 设置时间格式
        self.lbl.config(text=time.strftime("%Y-%m-%d %H:%M:%S"))
        # 设置更新时间频率
        self.after(1000, self.update_time)


# 程序主函数
Clock().mainloop()
