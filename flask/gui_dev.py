import tkinter as tk

def main():

    app_window = tk.Tk()
    app_window.title("Herovired Simple GUI")
    app_window.geometry("300x200") 

    # Add some widgets to the window
    label = tk.Label(app_window, text="Hello, welcome to the Herovired simple GUI!")
    label.pack(pady=20)

    button = tk.Button(app_window, text="Start Learning", command=lambda: label.config(text="Well Done"))
    button.pack(pady=20)

    # Step 4: Run the Tkinter event loop
    app_window.mainloop()


if __name__ == "__main__":
    main()