import tkinter as tk


class CalculatorApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Moj Kalkulator")
        self.root.resizable(False, False)
        self.root.configure(bg="#111827")

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self.colors = {
            "bg": "#111827",
            "panel": "#1f2937",
            "text": "#f9fafb",
            "muted": "#9ca3af",
            "num": "#374151",
            "op": "#2563eb",
            "special": "#ef4444",
            "equal": "#10b981",
        }

        self._build_ui()
        self._bind_keys()

    def _build_ui(self) -> None:
        container = tk.Frame(self.root, bg=self.colors["bg"], padx=10, pady=10)
        container.grid(row=0, column=0, sticky="nsew")

        display = tk.Entry(
            container,
            textvariable=self.display_var,
            font=("Segoe UI", 24, "bold"),
            justify="right",
            bd=0,
            state="readonly",
            readonlybackground=self.colors["panel"],
            fg=self.colors["text"],
            insertbackground=self.colors["text"],
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=4, pady=(4, 10), ipady=12)

        buttons = [
            ("C", 1, 0), ("(", 1, 1), (")", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2, 2),
        ]

        for item in buttons:
            if len(item) == 3:
                text, row, col = item
                colspan = 1
            else:
                text, row, col, colspan = item

            command = self._clear if text == "C" else self._calculate if text == "=" else lambda t=text: self._append(t)

            bg = self.colors["num"]
            fg = self.colors["text"]
            if text == "C":
                bg = self.colors["special"]
            elif text == "=":
                bg = self.colors["equal"]
            elif text in {"+", "-", "*", "/", "(", ")"}:
                bg = self.colors["op"]

            tk.Button(
                container,
                text=text,
                font=("Segoe UI", 16, "bold"),
                command=command,
                width=4,
                height=2,
                bd=0,
                bg=bg,
                fg=fg,
                activebackground="#4b5563",
                activeforeground=self.colors["text"],
                highlightthickness=0,
            ).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=4, pady=4)

        for i in range(6):
            container.grid_rowconfigure(i, weight=1)
        for i in range(4):
            container.grid_columnconfigure(i, weight=1)

    def _bind_keys(self) -> None:
        self.root.bind("<Return>", lambda _event: self._calculate())
        self.root.bind("<KP_Enter>", lambda _event: self._calculate())
        self.root.bind("<Escape>", lambda _event: self._clear())
        self.root.bind("<BackSpace>", lambda _event: self._backspace())

        for char in "0123456789.+-*/()":
            self.root.bind(char, lambda event, c=char: self._append(c))

    def _append(self, char: str) -> None:
        if self.display_var.get() == "Błąd":
            self.expression = ""
        self.expression += char
        self.display_var.set(self.expression)

    def _backspace(self) -> None:
        if self.display_var.get() == "Błąd":
            self._clear()
            return
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression if self.expression else "0")

    def _clear(self) -> None:
        self.expression = ""
        self.display_var.set("0")

    def _calculate(self) -> None:
        try:
            if not self.expression:
                return
            result = eval(self.expression, {"__builtins__": {}}, {})
            self.expression = str(result)
            self.display_var.set(self.expression)
        except Exception:
            self.expression = ""
            self.display_var.set("Błąd")


def main() -> None:
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

