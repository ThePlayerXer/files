import random
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def create_files():
    folderpath = "numbers"  
    os.makedirs(folderpath, exist_ok=True)  

    for i in range(1, 4):
        filename = f"file{i}.txt"
        with open(os.path.join(folderpath, filename), 'w') as file:
            for _ in range(10):
                number = random.randint(1, 10)
                file.write(f"{number}\n")
        print(f"Файл '{filename}' создан с случайными числами.")

def select_file_and_calculate_average():
    folderpath = "numbers"
    filepath = filedialog.askopenfilename(initialdir=folderpath, title="Выберите файл",
                                          filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if filepath:
        try:
            with open(filepath, 'r') as file:
                numbers = [int(line.strip()) for line in file]
            average = sum(numbers) / len(numbers)
            messagebox.showinfo("Результат", f"Содержимое файла: {numbers}\nСреднее значение: {average:.2f}")
        except (FileNotFoundError, ValueError) as e:
            messagebox.showerror("Ошибка", f"Ошибка при чтении файла: {e}")
    else:
        messagebox.showwarning("Предупреждение", "Файл не выбран.")

def save_numbers():
    numbers = entry.get().strip().split(',')
    try:
        numbers = [int(num) for num in numbers]
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, 'w') as file:
                for number in numbers:
                    file.write(f"{number}\n")
            messagebox.showinfo("Успех", "Числа успешно сохранены в файл.")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные целые числа, разделенные запятыми.")

root = tk.Tk()
root.title("Программа для работы с числами")
root.geometry("400x300")
root.configure(bg="#f0f0f0")  

frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
frame.pack(pady=20)

entry_label = tk.Label(frame, text="Введите числа (через запятую):", bg="#ffffff", font=("Arial", 12))
entry_label.pack()

entry = tk.Entry(frame, width=50, font=("Arial", 12))
entry.pack(pady=5)

save_button = tk.Button(frame, text="Сохранить числа в файл", command=save_numbers, bg="#4CAF50", fg="white", font=("Arial", 12))
save_button.pack(pady=5)

create_files_button = tk.Button(frame, text="Создать файлы с случайными числами", command=create_files, bg="#2196F3", fg="white", font=("Arial", 12))
create_files_button.pack(pady=5)

average_button = tk.Button(frame, text="Выбрать файл и вычислить среднее", command=select_file_and_calculate_average, bg="#FF9800", fg="white", font=("Arial", 12))
average_button.pack(pady=5)

root.mainloop()
