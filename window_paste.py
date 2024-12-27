import tkinter as tk


def create_gui():
    root = tk.Tk()
    root.title("window-paste")
    text_area = tk.Text(root, wrap=tk.WORD, width=80, height=30)
    text_area.pack(padx=0, pady=0, expand=True, fill='both')
    text_area.focus_set()
    return root, text_area


def get_text_content(text_area):
    return text_area.get("1.0", tk.END).strip()


def handle_return(event, root):
    # SHIFT + ENTER for a newline.
    if event.state & 0x1:
        return None

    root.quit()
    return "break"  # Prevents the newline from being added


def handle_window_close():
    root.quit()


def main():
    global root
    root, text_area = create_gui()

    text_area.bind("<Return>", lambda e: handle_return(e, root))
    root.protocol("WM_DELETE_WINDOW", handle_window_close)

    root.mainloop()

    content = get_text_content(text_area)
    print(content)

    root.destroy()


if __name__ == "__main__":
    main()