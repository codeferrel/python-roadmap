import tkinter as tk
from tkinter import ttk, messagebox
import itertools
import string
import threading
import time

# ── Karakter set ──────────────────────────────────────────────
CHARSETS = {
    "Angka (0-9)":       string.digits,
    "Huruf kecil (a-z)": string.ascii_lowercase,
    "Huruf besar (A-Z)": string.ascii_uppercase,
    "Huruf + Angka":     string.ascii_letters + string.digits,
    "Semua karakter":    string.printable[:94],
}

# ── Tema warna ────────────────────────────────────────────────
BG      = "#0f1117"
SURFACE = "#1a1d27"
CARD    = "#22253a"
ACCENT  = "#7c6ff7"
ACCENT2 = "#4ecdc4"
SUCCESS = "#2ecc71"
DANGER  = "#e74c3c"
WARN    = "#f39c12"
TEXT    = "#eaeaf0"
MUTED   = "#6b7080"
BORDER  = "#2e3149"
DIM     = "#3a3d52"


class PasswordCrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Brute Force — Password Cracker Visualizer")
        self.configure(bg=BG)
        self.resizable(True, True)

        self._running  = False
        self._thread   = None
        self._start_ts = 0.0
        self._delay    = 0.0
        self._char_boxes = []

        self._build_ui()
        # Maximize saat startup (cross-platform)
        try:
            self.state("zoomed")          # Windows & beberapa Linux
        except tk.TclError:
            self.attributes("-zoomed", True)  # Linux fallback
        # Bind F11 toggle fullscreen, Esc keluar fullscreen
        self.bind("<F11>",  self._toggle_fullscreen)
        self.bind("<Escape>", self._exit_fullscreen)
        self._fullscreen = False

    def _toggle_fullscreen(self, event=None):
        self._fullscreen = not self._fullscreen
        self.attributes("-fullscreen", self._fullscreen)

    def _exit_fullscreen(self, event=None):
        if self._fullscreen:
            self._fullscreen = False
            self.attributes("-fullscreen", False)

    # ══════════════════════════════════════════════════════════
    #  UI
    # ══════════════════════════════════════════════════════════
    def _build_ui(self):
        # ── Canvas + Scrollbar agar konten bisa di-scroll ────
        self._canvas = tk.Canvas(self, bg=BG, highlightthickness=0)
        self._scrollbar = ttk.Scrollbar(self, orient="vertical",
                                        command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=self._scrollbar.set)
        self._scrollbar.pack(side="right", fill="y")
        self._canvas.pack(side="left", fill="both", expand=True)

        outer = tk.Frame(self._canvas, bg=BG, padx=24, pady=20)
        self._win_id = self._canvas.create_window((0, 0), window=outer,
                                                  anchor="nw")

        # Update scroll region setiap outer berubah ukuran
        outer.bind("<Configure>", self._on_frame_configure)
        self._canvas.bind("<Configure>", self._on_canvas_configure)

        # Scroll mouse wheel
        self.bind_all("<MouseWheel>",      self._on_mousewheel)        # Windows
        self.bind_all("<Button-4>",        lambda e: self._canvas.yview_scroll(-1, "units"))  # Linux
        self.bind_all("<Button-5>",        lambda e: self._canvas.yview_scroll(1,  "units"))  # Linux

        tk.Label(outer, text="Brute Force",
                 font=("Courier New", 26, "bold"), fg=ACCENT, bg=BG).pack(anchor="w")
        tk.Label(outer, text="Password Cracker Visualizer ",
                 font=("Courier New", 11), fg=MUTED, bg=BG).pack(anchor="w", pady=(0, 16))

        # ── Baris atas: input | stats ─────────────────────────
        row1 = tk.Frame(outer, bg=BG)
        row1.pack(fill="x")

        left  = self._card(row1)
        left.pack(side="left", fill="both", expand=True, padx=(0, 8))
        right = self._card(row1)
        right.pack(side="left", fill="both", expand=True, padx=(8, 0))

        # Panel kiri: input
        self._section(left, "Target Password")
        self.var_target = tk.StringVar(value="ab3")
        self._entry(left, self.var_target)

        self._section(left, "Karakter Set", top=14)
        self.var_charset = tk.StringVar(value="Huruf + Angka")
        ttk.Combobox(left, textvariable=self.var_charset,
                     values=list(CHARSETS.keys()), state="readonly",
                     font=("Courier New", 11), width=26).pack(anchor="w", pady=(4, 0))

        self._section(left, "Panjang Maks", top=14)
        self.var_maxlen = tk.IntVar(value=4)
        sf = tk.Frame(left, bg=CARD)
        sf.pack(anchor="w", pady=(4, 0))
        for v in (2, 3, 4, 5, 6):
            tk.Radiobutton(sf, text=str(v), variable=self.var_maxlen, value=v,
                           bg=CARD, fg=TEXT, selectcolor=ACCENT,
                           activebackground=CARD,
                           font=("Courier New", 11)).pack(side="left", padx=6)

        self._section(left, "Kecepatan Visualisasi", top=14)
        spd_row = tk.Frame(left, bg=CARD)
        spd_row.pack(anchor="w", fill="x", pady=(4, 0))
        tk.Label(spd_row, text="Cepat", font=("Courier New", 9),
                 fg=MUTED, bg=CARD).pack(side="left")
        self.var_speed = tk.IntVar(value=0)
        tk.Scale(spd_row, from_=0, to=100, orient="horizontal",
                 variable=self.var_speed, showvalue=False,
                 bg=CARD, fg=ACCENT, troughcolor=SURFACE,
                 highlightthickness=0, length=140,
                 command=self._on_speed).pack(side="left", padx=6)
        tk.Label(spd_row, text="Lambat", font=("Courier New", 9),
                 fg=MUTED, bg=CARD).pack(side="left")
        self.lbl_spd = tk.Label(spd_row, text="(auto)",
                                font=("Courier New", 9), fg=ACCENT2, bg=CARD)
        self.lbl_spd.pack(side="left", padx=(8, 0))

        tk.Frame(left, bg=BORDER, height=1).pack(fill="x", pady=14)

        btn_row = tk.Frame(left, bg=CARD)
        btn_row.pack(anchor="w")
        self.btn_start = tk.Button(btn_row, text="▶  Mulai Crack",
                                   command=self._toggle,
                                   bg=ACCENT, fg="white", relief="flat",
                                   font=("Courier New", 11, "bold"),
                                   cursor="hand2", padx=14, pady=8)
        self.btn_start.pack(side="left")
        self.btn_reset = tk.Button(btn_row, text="↺  Reset",
                                   command=self._reset,
                                   bg=SURFACE, fg=MUTED, relief="flat",
                                   font=("Courier New", 10),
                                   cursor="hand2", padx=14, pady=8)
        self.btn_reset.pack(side="left", padx=(10, 0))

        # Panel kanan: stats
        self._section(right, "Percobaan Saat Ini")
        self.lbl_current = tk.Label(right, text="—",
                                    font=("Courier New", 26, "bold"),
                                    fg=ACCENT2, bg=CARD, anchor="w")
        self.lbl_current.pack(anchor="w", pady=(4, 0))

        tk.Frame(right, bg=BORDER, height=1).pack(fill="x", pady=10)

        stats = tk.Frame(right, bg=CARD)
        stats.pack(fill="x")
        self.lbl_count = self._stat(stats, "Percobaan", "0")
        self.lbl_speed = self._stat(stats, "Kecepatan",  "0 /s")
        self.lbl_time  = self._stat(stats, "Waktu",      "0.0 s")
        self.lbl_len   = self._stat(stats, "Panjang",    "—")

        tk.Frame(right, bg=BORDER, height=1).pack(fill="x", pady=10)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("BF.Horizontal.TProgressbar",
                        troughcolor=SURFACE, background=ACCENT,
                        thickness=12, borderwidth=0)
        self.progress = ttk.Progressbar(right, style="BF.Horizontal.TProgressbar",
                                        mode="indeterminate")
        self.progress.pack(fill="x", pady=(0, 4))
        self.lbl_status = tk.Label(right, text="Siap memulai…",
                                   font=("Courier New", 10), fg=MUTED, bg=CARD)
        self.lbl_status.pack(anchor="w")

        # ══════════════════════════════════════════════════════
        #  VISUALISASI KARAKTER — fitur baru
        # ══════════════════════════════════════════════════════
        vis_frame = self._card(outer, pady=16)
        vis_frame.pack(fill="x", pady=(14, 0))

        self._section(vis_frame, "Visualisasi Karakter Per Karakter")
        tk.Label(vis_frame,
                 text="Hijau = cocok dengan target  |  Kuning = sedang dicoba  |  Abu = belum dicoba",
                 font=("Courier New", 9), fg=MUTED, bg=CARD).pack(anchor="w", pady=(2, 10))

        self.char_frame = tk.Frame(vis_frame, bg=CARD)
        self.char_frame.pack(anchor="w")

        # Baris perbandingan
        cmp1 = tk.Frame(vis_frame, bg=CARD)
        cmp1.pack(anchor="w", pady=(12, 0), fill="x")
        tk.Label(cmp1, text="Target  :", font=("Courier New", 11), fg=MUTED, bg=CARD).pack(side="left")
        self.lbl_target_display = tk.Label(cmp1, text="—",
                 font=("Courier New", 13, "bold"), fg=ACCENT, bg=CARD)
        self.lbl_target_display.pack(side="left", padx=(6, 0))

        cmp2 = tk.Frame(vis_frame, bg=CARD)
        cmp2.pack(anchor="w", pady=(4, 0), fill="x")
        tk.Label(cmp2, text="Dicoba  :", font=("Courier New", 11), fg=MUTED, bg=CARD).pack(side="left")
        self.lbl_attempt_colored = tk.Label(cmp2, text="—",
                 font=("Courier New", 13, "bold"), fg=ACCENT2, bg=CARD)
        self.lbl_attempt_colored.pack(side="left", padx=(6, 0))

        self.match_canvas = tk.Canvas(vis_frame, bg=CARD, height=8,
                                      highlightthickness=0)
        self.match_canvas.pack(anchor="w", pady=(8, 0), fill="x")

        # ── Log ───────────────────────────────────────────────
        log_frame = self._card(outer, pady=14)
        log_frame.pack(fill="x", pady=(12, 0))
        self._section(log_frame, "Log Percobaan")
        self.log_box = tk.Text(log_frame, height=8,
                               bg=BG, fg=TEXT, font=("Courier New", 10),
                               relief="flat", state="disabled",
                               selectbackground=ACCENT)
        self.log_box.pack(fill="x", pady=(6, 0))
        self.log_box.tag_config("hit",   foreground=SUCCESS)
        self.log_box.tag_config("try",   foreground=MUTED)
        self.log_box.tag_config("info",  foreground=ACCENT)
        self.log_box.tag_config("error", foreground=DANGER)

        # ── Hasil ─────────────────────────────────────────────
        res_frame = self._card(outer, pady=14)
        res_frame.pack(fill="x", pady=(12, 0))
        self._section(res_frame, "Hasil")
        self.lbl_result = tk.Label(res_frame, text="Belum ada hasil.",
                                   font=("Courier New", 13), fg=TEXT, bg=CARD,
                                   anchor="w", wraplength=680, justify="left")
        self.lbl_result.pack(anchor="w", pady=(4, 0))

    # ── Scroll helpers ────────────────────────────────────────
    def _on_frame_configure(self, event=None):
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))

    def _on_canvas_configure(self, event=None):
        self._canvas.itemconfig(self._win_id, width=event.width)

    def _on_mousewheel(self, event):
        self._canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # ── Helper ────────────────────────────────────────────────
    def _card(self, parent, pady=18):
        return tk.Frame(parent, bg=CARD, padx=18, pady=pady,
                        highlightthickness=1, highlightbackground=BORDER)

    def _section(self, parent, text, top=0):
        tk.Label(parent, text=text.upper(), font=("Courier New", 9, "bold"),
                 fg=MUTED, bg=CARD).pack(anchor="w", pady=(top, 0))

    def _entry(self, parent, var):
        tk.Entry(parent, textvariable=var,
                 bg=SURFACE, fg=TEXT, insertbackground=TEXT,
                 font=("Courier New", 14), relief="flat", width=24,
                 highlightthickness=1, highlightbackground=BORDER,
                 highlightcolor=ACCENT).pack(anchor="w", pady=(6, 0))

    def _stat(self, parent, label, value):
        f = tk.Frame(parent, bg=CARD)
        f.pack(side="left", expand=True, padx=4)
        tk.Label(f, text=label, font=("Courier New", 9), fg=MUTED, bg=CARD).pack()
        lbl = tk.Label(f, text=value, font=("Courier New", 13, "bold"), fg=TEXT, bg=CARD)
        lbl.pack()
        return lbl

    def _on_speed(self, val):
        v = int(val)
        if v == 0:
            self._delay = 0.0
            self.lbl_spd.config(text="(auto)")
        else:
            self._delay = 0.001 * (1.5 ** (v / 10))
            self.lbl_spd.config(text=f"{self._delay*1000:.0f} ms/try")

    # ══════════════════════════════════════════════════════════
    #  Visualisasi kotak karakter
    # ══════════════════════════════════════════════════════════
    def _build_char_boxes(self, n):
        for w in self.char_frame.winfo_children():
            w.destroy()
        self._char_boxes = []
        for _ in range(n):
            cell = tk.Frame(self.char_frame, bg=DIM, width=52, height=52,
                            highlightthickness=1, highlightbackground=BORDER)
            cell.pack_propagate(False)
            cell.pack(side="left", padx=3)
            lbl = tk.Label(cell, text="?", font=("Courier New", 18, "bold"),
                           fg=MUTED, bg=DIM)
            lbl.place(relx=0.5, rely=0.5, anchor="center")
            self._char_boxes.append((cell, lbl))

    def _update_char_boxes(self, attempt, target):
        n = len(self._char_boxes)
        for i, (cell, lbl) in enumerate(self._char_boxes):
            if i < len(attempt):
                ch = attempt[i]
                if i < len(target) and ch == target[i]:
                    bg, fg, bd = "#1a3a2a", SUCCESS, SUCCESS
                else:
                    bg, fg, bd = "#3a2800", WARN, WARN
                lbl.config(text=ch, fg=fg, bg=bg)
                cell.config(bg=bg, highlightbackground=bd)
            else:
                lbl.config(text="·", fg=MUTED, bg=DIM)
                cell.config(bg=DIM, highlightbackground=BORDER)

    def _flash_all_green(self, attempt):
        for i, (cell, lbl) in enumerate(self._char_boxes):
            ch = attempt[i] if i < len(attempt) else ""
            lbl.config(text=ch, fg="#0f1117", bg=SUCCESS)
            cell.config(bg=SUCCESS, highlightbackground=SUCCESS)

    def _draw_match_bar(self, attempt, target):
        self.match_canvas.delete("all")
        self.update_idletasks()
        w = self.match_canvas.winfo_width() or 500
        if not attempt or not target:
            self.match_canvas.create_rectangle(0, 0, w, 8, fill=DIM, outline="")
            return
        matched = sum(1 for i, c in enumerate(attempt)
                      if i < len(target) and c == target[i])
        pct = matched / len(target)
        self.match_canvas.create_rectangle(0, 0, w, 8, fill=DIM, outline="")
        if pct > 0:
            color = SUCCESS if pct == 1.0 else WARN
            self.match_canvas.create_rectangle(0, 0, int(w * pct), 8,
                                               fill=color, outline="")

    # ══════════════════════════════════════════════════════════
    #  Kontrol
    # ══════════════════════════════════════════════════════════
    def _toggle(self):
        if self._running:
            self._running = False
            self.btn_start.config(text="▶  Mulai Crack", bg=ACCENT)
            self._log("[ Dihentikan oleh pengguna ]", "error")
            self.progress.stop()
            self.lbl_status.config(text="Dihentikan.")
        else:
            self._start()

    def _reset(self):
        self._running = False
        self.btn_start.config(text="▶  Mulai Crack", bg=ACCENT)
        self.lbl_current.config(text="—", fg=ACCENT2)
        self.lbl_count.config(text="0")
        self.lbl_speed.config(text="0 /s")
        self.lbl_time.config(text="0.0 s")
        self.lbl_len.config(text="—")
        self.lbl_status.config(text="Siap memulai…")
        self.lbl_result.config(text="Belum ada hasil.", fg=TEXT)
        self.lbl_attempt_colored.config(text="—", fg=ACCENT2)
        self.lbl_target_display.config(text="—")
        self.progress.stop()
        self.match_canvas.delete("all")
        for w in self.char_frame.winfo_children():
            w.destroy()
        self._char_boxes = []
        self.log_box.config(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.config(state="disabled")

    def _start(self):
        target  = self.var_target.get()
        charset = CHARSETS.get(self.var_charset.get(),
                               string.ascii_lowercase + string.digits)
        maxlen  = self.var_maxlen.get()

        if not target:
            messagebox.showwarning("Input kosong", "Masukkan target password dulu!")
            return
        if len(target) > maxlen:
            messagebox.showwarning("Panjang maks",
                f"Target lebih panjang dari {maxlen} karakter.\nNaikkan panjang maks!")
            return

        self._reset()
        self._running  = True
        self._start_ts = time.time()
        self.btn_start.config(text="■  Stop", bg=DANGER)
        self.progress.start(12)
        self.lbl_status.config(text="Proses berjalan…")
        self.lbl_target_display.config(text=target)
        self._log(f"Target: '{target}' | Charset: {len(charset)} karakter | Maks: {maxlen}", "info")
        self._build_char_boxes(len(target))

        self._thread = threading.Thread(
            target=self._crack_worker,
            args=(target, charset, maxlen),
            daemon=True)
        self._thread.start()

    # ══════════════════════════════════════════════════════════
    #  Worker thread
    # ══════════════════════════════════════════════════════════
    def _crack_worker(self, target, charset, maxlen):
        found    = False
        count    = 0
        LOG_UI   = 300
        LOG_TEXT = 2000
        prev_len = -1

        for length in range(1, maxlen + 1):
            if not self._running:
                break

            if length != prev_len:
                prev_len = length
                self.after(0, self._rebuild_boxes, length, len(target))
                self.after(0, self.lbl_len.config, {"text": str(length)})
                self._log(
                    f"── Mencoba panjang {length} "
                    f"({len(charset)**length:,} kombinasi) ──", "info")

            for combo in itertools.product(charset, repeat=length):
                if not self._running:
                    break

                attempt = "".join(combo)
                count  += 1
                delay   = self._delay

                if delay > 0:
                    self.after(0, self._update_all, attempt, target, count)
                    time.sleep(delay)
                elif count % LOG_UI == 0:
                    self.after(0, self._update_all, attempt, target, count)

                if count % LOG_TEXT == 0:
                    matched = sum(1 for i, c in enumerate(attempt)
                                  if i < len(target) and c == target[i])
                    self._log(
                        f"  {count:>10,}  →  {attempt!r:<10}  "
                        f"({matched}/{len(target)} karakter cocok)", "try")

                if attempt == target:
                    elapsed = time.time() - self._start_ts
                    speed   = int(count / elapsed) if elapsed > 0 else 0
                    self.after(0, self._on_found, attempt, count, speed, elapsed)
                    found = True
                    break

            if found:
                break

        if not found and self._running:
            self.after(0, self._on_not_found, count)

        self._running = False
        self.after(0, self.btn_start.config, {"text": "▶  Mulai Crack", "bg": ACCENT})
        self.after(0, self.progress.stop)

    def _rebuild_boxes(self, attempt_len, target_len):
        self._build_char_boxes(max(attempt_len, target_len))

    def _update_all(self, attempt, target, count):
        elapsed = time.time() - self._start_ts
        speed   = int(count / elapsed) if elapsed > 0 else 0

        self.lbl_current.config(text=attempt[:22], fg=ACCENT2)
        self.lbl_count.config(text=f"{count:,}")
        self.lbl_speed.config(text=f"{speed:,} /s")
        self.lbl_time.config(text=f"{elapsed:.1f} s")
        self.lbl_attempt_colored.config(text=attempt)

        n_needed = max(len(attempt), len(target))
        if len(self._char_boxes) != n_needed:
            self._build_char_boxes(n_needed)
        self._update_char_boxes(attempt, target)
        self._draw_match_bar(attempt, target)

    def _on_found(self, attempt, count, speed, elapsed):
        self.lbl_current.config(text=attempt, fg=SUCCESS)
        self.lbl_count.config(text=f"{count:,}")
        self.lbl_speed.config(text=f"{speed:,} /s")
        self.lbl_time.config(text=f"{elapsed:.2f} s")
        self.lbl_status.config(text="✓ Password ditemukan!")
        self.lbl_attempt_colored.config(text=attempt, fg=SUCCESS)

        if len(self._char_boxes) != len(attempt):
            self._build_char_boxes(len(attempt))
        self._flash_all_green(attempt)
        self._draw_match_bar(attempt, attempt)

        self.lbl_result.config(fg=SUCCESS,
            text=f"✓  BERHASIL!  Password '{attempt}' ditemukan "
                 f"setelah {count:,} percobaan dalam {elapsed:.2f} detik "
                 f"({speed:,} percobaan/detik).")
        self._log(
            f"[ DITEMUKAN: '{attempt}' — {count:,} percobaan / {elapsed:.2f}s ]", "hit")

    def _on_not_found(self, count):
        self.lbl_result.config(fg=DANGER,
            text=f"✗  GAGAL — Tidak ditemukan setelah {count:,} percobaan. "
                 "Coba perluas charset atau naikkan panjang maks.")
        self._log(f"[ TIDAK DITEMUKAN setelah {count:,} percobaan ]", "error")
        self.lbl_status.config(text="Tidak ditemukan.")

    def _log(self, msg, tag="try"):
        def _do():
            self.log_box.config(state="normal")
            self.log_box.insert("end", msg + "\n", tag)
            self.log_box.see("end")
            self.log_box.config(state="disabled")
        self.after(0, _do)


if __name__ == "__main__":
    app = PasswordCrackerApp()
    app.mainloop()