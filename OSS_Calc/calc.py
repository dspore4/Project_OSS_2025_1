import tkinter as tk
import numpy as np
from ast impoer literal_eval
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=' , 'rank/sol']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == 'rank/sol':
            try:
                # 입력 형식: [[계수행렬]]; [오른쪽 벡터]
                A_str, B_str = self.expression.split(';')
                A = literal_eval(A_str.strip())
                B = literal_eval(B_str.strip())

                A = np.array(A, dtype=float)
                B = np.array(B, dtype=float).reshape(-1, 1)

                # 첨가 행렬
                augmented = np.hstack([A, B])

                rank_A = np.linalg.matrix_rank(A)
                rank_aug = np.linalg.matrix_rank(augmented)
                n_vars = A.shape[1]

                if rank_A != rank_aug:
                    result = f"rank={rank_A}, count=none"
                elif rank_A == n_vars:
                    result = f"rank={rank_A}, count=unique"
                else:
                    result = f"rank={rank_A}, count=infinite"

                self.expression = result
            except:
                self.expression = "에러"
            
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



