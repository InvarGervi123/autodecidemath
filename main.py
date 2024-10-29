import tkinter as tk
from tkinter import messagebox
from sympy import symbols, Eq, solve, sympify
import re

# יצירת הנעלם עבור המשוואה
x = symbols('x')

def add_multiplication_signs(equation_str):
    # הוספת סימני כפל במקומות המתאימים, כמו לפני נעלם או סוגריים
    equation_str = re.sub(r'(\d)(x)', r'\1*x', equation_str)  # הוספת כפל לפני x
    equation_str = re.sub(r'(\d)\(', r'\1*(', equation_str)  # הוספת כפל לפני סוגריים
    return equation_str

def solve_equation():
    # קבלת המשוואה מהקלט
    equation_str = entry.get()
    try:
        # בדיקת קיום שווה
        if "=" not in equation_str:
            raise ValueError("המשוואה צריכה להכיל סימן שווה (=).")
        
        # הוספת סימני כפל אוטומטיים
        equation_str = add_multiplication_signs(equation_str)

        # פיצול המשוואה לשני אגפים
        left_side, right_side = equation_str.split("=")
        
        # המרה של הקלט לביטוי מתמטי סימבולי
        left_expr = sympify(left_side.replace("^", "**"))
        right_expr = sympify(right_side.replace("^", "**"))
        
        # יצירת המשוואה והפתרון שלה
        equation = Eq(left_expr, right_expr)
        solutions = solve(equation, x)
        
        # הצגת התוצאה
        result_label.config(text=f"תוצאה: {solutions}")
    except ValueError as ve:
        messagebox.showerror("שגיאה", str(ve))
    except Exception as e:
        messagebox.showerror("שגיאה", f"שגיאה בעיבוד המשוואה: {e}")

# יצירת החלון הראשי
root = tk.Tk()
root.title("פתרון משוואות עם נעלם")

# יצירת תווית
label = tk.Label(root, text="הכנס משוואה מתמטית (לדוגמה: '2^x + x = 3x - 12'):")
label.pack(pady=10)

# יצירת שדה קלט
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# יצירת כפתור לחישוב המשוואה
solve_button = tk.Button(root, text="חשב", command=solve_equation)
solve_button.pack(pady=5)

# יצירת תווית להצגת התוצאה
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# הרצת החלון הראשי
root.mainloop()
