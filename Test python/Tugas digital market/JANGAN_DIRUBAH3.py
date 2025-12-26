import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from datetime import datetime
import os

# File penyimpanan
PRODUK_FILE = "produk.xlsx"
PESANAN_FILE = "pesanan.xlsx"


class DigitalMartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PT Digital Mart - Manajemen Stok & Pesanan")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f4f8")

        # Load data
        self.load_data()
        self.edit_mode = False
        self.edit_id = None
        self.setup_ui()

    def load_data(self):
        # Muat produk
        try:
            self.produk_df = pd.read_excel(PRODUK_FILE, dtype={"ID": str})
            self.produk_df["ID"] = self.produk_df["ID"].fillna("").astype(str)
            self.produk_df["Nama"] = self.produk_df["Nama"].fillna("").astype(str)
            self.produk_df["Harga"] = pd.to_numeric(self.produk_df["Harga"], errors="coerce").fillna(0).astype(int)
            self.produk_df["Stok"] = pd.to_numeric(self.produk_df["Stok"], errors="coerce").fillna(0).astype(int)
        except FileNotFoundError:
            self.produk_df = pd.DataFrame(columns=["ID", "Nama", "Harga", "Stok"])
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat {PRODUK_FILE}: {e}")
            self.produk_df = pd.DataFrame(columns=["ID", "Nama", "Harga", "Stok"])

        # Muat pesanan
        try:
            self.pesanan_df = pd.read_excel(PESANAN_FILE)
            required_cols = ["ID Pesanan", "Pelanggan", "Produk", "Jumlah", "Total", "Tanggal"]
            for col in required_cols:
                if col not in self.pesanan_df.columns:
                    self.pesanan_df[col] = ""
            self.pesanan_df["Jumlah"] = pd.to_numeric(self.pesanan_df["Jumlah"], errors="coerce").fillna(0).astype(int)
            self.pesanan_df["Total"] = pd.to_numeric(self.pesanan_df["Total"], errors="coerce").fillna(0).astype(int)
            self.pesanan_df["Tanggal"] = self.pesanan_df["Tanggal"].fillna("")
        except FileNotFoundError:
            self.pesanan_df = pd.DataFrame(columns=["ID Pesanan", "Pelanggan", "Produk", "Jumlah", "Total", "Tanggal"])
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat {PESANAN_FILE}: {e}")
            self.pesanan_df = pd.DataFrame(columns=["ID Pesanan", "Pelanggan", "Produk", "Jumlah", "Total", "Tanggal"])

    def save_data(self):
        try:
            self.produk_df.to_excel(PRODUK_FILE, index=False)
            self.pesanan_df.to_excel(PESANAN_FILE, index=False)
            messagebox.showinfo("✅ Sukses", f"Data disimpan ke:\n- {PRODUK_FILE}\n- {PESANAN_FILE}")
        except Exception as e:
            messagebox.showerror("❌ Error", f"Gagal menyimpan file:\n{e}")

    def refresh_data(self):
        """Muat ulang data dari file dan perbarui tampilan"""
        self.load_data()
        self.refresh_produk()
        self.refresh_pesanan()
        # Perbarui daftar produk di combobox
        self.produk_list = list(self.produk_df["Nama"]) if not self.produk_df.empty else []
        self.combo_produk['values'] = self.produk_list
        messagebox.showinfo("✅ Refresh", "Data berhasil dimuat ulang!")

    def validate_angka(self, value_if_allowed):
        """Hanya izinkan input angka atau kosong"""
        if value_if_allowed == "":
            return True
        if value_if_allowed.isdigit():
            return True
        return False

    def setup_ui(self):
        # Judul
        title = tk.Label(
            self.root,
            text="📦 PT Digital Mart",
            font=("Arial", 24, "bold"),
            bg="#1a4f76",
            fg="white",
            pady=15
        )
        title.pack(fill="x")

        # Notebook (tab)
        notebook = ttk.Notebook(self.root)
        notebook.pack(pady=10, padx=20, fill="both", expand=True)

        # Tab 1: Manajemen Produk
        tab_produk = ttk.Frame(notebook)
        notebook.add(tab_produk, text="📦 Produk")

        # Form Produk
        frame_form = tk.LabelFrame(tab_produk, text="Tambah/Edit Produk", padx=10, pady=10)
        frame_form.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_form, text="ID Produk:").grid(row=0, column=0, sticky="w", pady=3)
        self.id_var = tk.StringVar()
        tk.Entry(frame_form, textvariable=self.id_var, width=20).grid(row=0, column=1, padx=5)

        tk.Label(frame_form, text="Nama Produk:").grid(row=0, column=2, sticky="w", pady=3)
        self.nama_var = tk.StringVar()
        tk.Entry(frame_form, textvariable=self.nama_var, width=30).grid(row=0, column=3, padx=5)

        tk.Label(frame_form, text="Harga (Rp):").grid(row=1, column=0, sticky="w", pady=3)
        self.harga_var = tk.StringVar()
        vcmd = (self.root.register(self.validate_angka), '%P')
        tk.Entry(
            frame_form,
            textvariable=self.harga_var,
            width=20,
            validate='key',
            validatecommand=vcmd
        ).grid(row=1, column=1, padx=5)

        tk.Label(frame_form, text="Stok:").grid(row=1, column=2, sticky="w", pady=3)
        self.stok_var = tk.IntVar()
        tk.Entry(frame_form, textvariable=self.stok_var, width=20).grid(row=1, column=3, padx=5)

        # Tombol
        self.btn_tambah = tk.Button(frame_form, text="➕ Tambah", command=self.tambah_produk, bg="#28a745", fg="white")
        self.btn_tambah.grid(row=2, column=0, pady=10, sticky="w")

        self.btn_edit = tk.Button(frame_form, text="🔁 Simpan Edit", command=self.simpan_edit_produk, bg="#ffc107", fg="black", state="disabled")
        self.btn_edit.grid(row=2, column=1, pady=10, padx=5)

        tk.Button(frame_form, text="↺ Reset", command=self.reset_form_produk, bg="#6c757d", fg="white").grid(row=2, column=2, pady=10)

        # Tabel Produk
        frame_tabel = tk.LabelFrame(tab_produk, text="Daftar Produk", padx=10, pady=10)
        frame_tabel.pack(fill="both", expand=True, padx=10, pady=5)

        tk.Label(frame_tabel, text="Cari:").pack(side="left")
        self.search_var = tk.StringVar()
        entry_cari = tk.Entry(frame_tabel, textvariable=self.search_var, width=30)
        entry_cari.pack(side="left", padx=5)
        entry_cari.bind("<KeyRelease>", self.cari_produk)

        tk.Button(frame_tabel, text="🔍 Cek Stok Rendah", command=self.cek_stok_rendah, bg="#ffc107").pack(side="right", padx=5)

        # Treeview
        self.tree_produk = ttk.Treeview(
            frame_tabel,
            columns=("ID", "Nama", "Harga", "Stok"),
            show="headings"
        )
        self.tree_produk.heading("ID", text="ID")
        self.tree_produk.heading("Nama", text="Nama")
        self.tree_produk.heading("Harga", text="Harga (Rp)")
        self.tree_produk.heading("Stok", text="Stok")
        self.tree_produk.column("ID", width=100)
        self.tree_produk.column("Nama", width=250)
        self.tree_produk.column("Harga", width=120)
        self.tree_produk.column("Stok", width=80)
        self.tree_produk.pack(fill="both", expand=True, pady=5)

        self.tree_produk.bind("<Double-1>", self.on_produk_select)

        # Tombol aksi produk
        frame_btn = tk.Frame(tab_produk)
        frame_btn.pack(pady=5)
        tk.Button(frame_btn, text="🗑️ Hapus", command=self.hapus_produk, bg="#dc3545", fg="white").pack(side="left", padx=5)
        tk.Button(frame_btn, text="🔄 Refresh", command=self.refresh_data, bg="#6f42c1", fg="white").pack(side="left", padx=5)
        tk.Button(frame_btn, text="💾 Simpan Data", command=self.save_data, bg="#007bff", fg="white").pack(side="right", padx=5)

        self.refresh_produk()

        # Tab 2: Pesanan
        tab_pesanan = ttk.Frame(notebook)
        notebook.add(tab_pesanan, text="🛒 Pesanan")

        frame_pesanan = tk.LabelFrame(tab_pesanan, text="Proses Pesanan", padx=10, pady=10)
        frame_pesanan.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_pesanan, text="Nama Pelanggan:").grid(row=0, column=0, sticky="w", pady=3)
        self.pelanggan_var = tk.StringVar()
        tk.Entry(frame_pesanan, textvariable=self.pelanggan_var, width=30).grid(row=0, column=1, padx=5)

        tk.Label(frame_pesanan, text="Produk:").grid(row=1, column=0, sticky="w", pady=3)
        self.produk_list = list(self.produk_df["Nama"]) if not self.produk_df.empty else []
        self.produk_var = tk.StringVar()
        self.combo_produk = ttk.Combobox(frame_pesanan, textvariable=self.produk_var, values=self.produk_list, state="readonly", width=40)
        self.combo_produk.grid(row=1, column=1, padx=5)
        self.combo_produk.bind("<<ComboboxSelected>>", self.update_harga_stok)

        tk.Label(frame_pesanan, text="Harga:").grid(row=2, column=0, sticky="w", pady=3)
        self.harga_produk_var = tk.IntVar()
        tk.Label(frame_pesanan, textvariable=self.harga_produk_var).grid(row=2, column=1, sticky="w", padx=5)

        tk.Label(frame_pesanan, text="Stok Tersedia:").grid(row=3, column=0, sticky="w", pady=3)
        self.stok_produk_var = tk.IntVar()
        tk.Label(frame_pesanan, textvariable=self.stok_produk_var).grid(row=3, column=1, sticky="w", padx=5)

        tk.Label(frame_pesanan, text="Jumlah:").grid(row=4, column=0, sticky="w", pady=3)
        self.jumlah_var = tk.IntVar(value=1)
        tk.Spinbox(frame_pesanan, from_=1, to=1000, textvariable=self.jumlah_var, width=10).grid(row=4, column=1, sticky="w", padx=5)

        tk.Label(frame_pesanan, text="Total:").grid(row=5, column=0, sticky="w", pady=3)
        self.total_var = tk.StringVar()
        tk.Label(frame_pesanan, textvariable=self.total_var, font=("Arial", 12, "bold"), fg="#1a4f76").grid(row=5, column=1, sticky="w", padx=5)

        tk.Button(frame_pesanan, text="✅ Proses Pesanan", command=self.proses_pesanan, bg="#28a745", fg="white").grid(row=6, column=0, columnspan=2, pady=10)

        # Tabel Pesanan
        frame_tabel_pesanan = tk.LabelFrame(tab_pesanan, text="Riwayat Pesanan", padx=10, pady=10)
        frame_tabel_pesanan.pack(fill="both", expand=True, padx=10, pady=5)

        self.tree_pesanan = ttk.Treeview(
            frame_tabel_pesanan,
            columns=("ID", "Pelanggan", "Produk", "Jumlah", "Total", "Tanggal"),
            show="headings",
            selectmode="extended"  # <-- izinkan multi-select (default, tapi eksplisit lebih aman)
        
        )
        self.tree_pesanan.heading("ID", text="ID Pesanan")
        self.tree_pesanan.heading("Pelanggan", text="Pelanggan")
        self.tree_pesanan.heading("Produk", text="Produk")
        self.tree_pesanan.heading("Jumlah", text="Jumlah")
        self.tree_pesanan.heading("Total", text="Total (Rp)")
        self.tree_pesanan.heading("Tanggal", text="Tanggal")
        self.tree_pesanan.column("ID", width=100)
        self.tree_pesanan.column("Pelanggan", width=150)
        self.tree_pesanan.column("Produk", width=200)
        self.tree_pesanan.column("Jumlah", width=70)
        self.tree_pesanan.column("Total", width=100)
        self.tree_pesanan.column("Tanggal", width=150)
        self.tree_pesanan.pack(fill="both", expand=True, pady=5)

        # Tombol di tab pesanan
        frame_btn_pesanan = tk.Frame(tab_pesanan)
        frame_btn_pesanan.pack(pady=5)
        tk.Button(frame_btn_pesanan, text="📥 Export ke Excel", command=self.export_excel, bg="#2c5aa0", fg="white").pack(side="left", padx=5)
        tk.Button(frame_btn_pesanan, text="🗑️ Hapus Pesanan", command=self.hapus_pesanan, bg="#dc3545", fg="white").pack(side="left", padx=5)
        tk.Button(frame_btn_pesanan, text="🔄 Refresh Data", command=self.refresh_data, bg="#6f42c1", fg="white").pack(side="left", padx=5)

        self.refresh_pesanan()

    # ----------------- PRODUK -----------------
    def refresh_produk(self):
        for item in self.tree_produk.get_children():
            self.tree_produk.delete(item)

        for _, row in self.produk_df.iterrows():
            try:
                harga = int(row["Harga"])
            except:
                harga = 0
            try:
                stok = int(row["Stok"])
            except:
                stok = 0

            self.tree_produk.insert("", "end", values=(
                row["ID"],
                row["Nama"],
                f"{harga:,}".replace(",", "."),
                stok
            ), tags=("rendah",) if stok < 5 else ())

        self.tree_produk.tag_configure("rendah", background="#ffebee", foreground="#c62828")

    def cari_produk(self, event=None):
        query = self.search_var.get().strip()
        if not query:
            self.refresh_produk()
            return

        query = query.lower()
        for item in self.tree_produk.get_children():
            self.tree_produk.delete(item)

        for _, row in self.produk_df.iterrows():
            try:
                id_val = str(row["ID"]).lower()
            except:
                id_val = ""
            try:
                nama_val = str(row["Nama"]).lower()
            except:
                nama_val = ""

            if query in id_val or query in nama_val:
                try:
                    harga_fmt = f"{int(row['Harga']):,}".replace(",", ".")
                except:
                    harga_fmt = "0"
                stok_val = int(row["Stok"]) if pd.notna(row["Stok"]) else 0
                self.tree_produk.insert("", "end", values=(
                    row["ID"],
                    row["Nama"],
                    harga_fmt,
                    stok_val
                ), tags=("rendah",) if stok_val < 5 else ())

    def tambah_produk(self):
        id_prod = self.id_var.get().strip()
        nama = self.nama_var.get().strip()
        harga_str = self.harga_var.get().strip()
        stok = self.stok_var.get()

        if not id_prod or not nama or stok < 0:
            messagebox.showerror("❌ Error", "Semua field wajib diisi dengan benar!")
            return

        if not harga_str.isdigit() or int(harga_str) <= 0:
            messagebox.showerror("❌ Error", "Masukkan informasi dengan benar")
            return
        harga = int(harga_str)

        if id_prod in self.produk_df["ID"].values:
            messagebox.showerror("❌ Error", "ID Produk sudah ada!")
            return

        new_row = pd.DataFrame([{
            "ID": id_prod,
            "Nama": nama,
            "Harga": harga,
            "Stok": stok
        }])
        self.produk_df = pd.concat([self.produk_df, new_row], ignore_index=True)
        self.refresh_produk()
        self.reset_form_produk()
        messagebox.showinfo("✅ Sukses", "Produk berhasil ditambahkan!")

    def simpan_edit_produk(self):
        if not self.edit_mode or not self.edit_id:
            messagebox.showerror("❌ Error", "Tidak ada produk yang sedang diedit!")
            return

        id_baru = self.id_var.get().strip()
        nama = self.nama_var.get().strip()
        harga_str = self.harga_var.get().strip()
        stok = self.stok_var.get()

        if not id_baru or not nama or stok < 0:
            messagebox.showerror("❌ Error", "Semua field wajib diisi dengan benar!")
            return

        if not harga_str.isdigit() or int(harga_str) <= 0:
            messagebox.showerror("❌ Error", "Masukkan informasi dengan benar")
            return
        harga = int(harga_str)

        existing_ids = set(self.produk_df["ID"].values)
        if id_baru != self.edit_id and id_baru in existing_ids:
            messagebox.showerror("❌ Error", "ID Produk sudah digunakan oleh produk lain!")
            return

        self.produk_df.loc[self.produk_df["ID"] == self.edit_id, ["ID", "Nama", "Harga", "Stok"]] = [id_baru, nama, harga, stok]
        self.refresh_produk()
        self.reset_form_produk()
        messagebox.showinfo("✅ Sukses", "Produk berhasil diperbarui!")

    def reset_form_produk(self):
        self.id_var.set("")
        self.nama_var.set("")
        self.harga_var.set("")
        self.stok_var.set(0)
        self.edit_mode = False
        self.edit_id = None
        self.btn_tambah.config(state="normal")
        self.btn_edit.config(state="disabled")

    def on_produk_select(self, event):
        selection = self.tree_produk.selection()
        if not selection:
            return
        item = selection[0]
        values = self.tree_produk.item(item, "values")
        
        self.id_var.set(values[0])
        self.nama_var.set(values[1])
        harga_str = str(values[2]).replace(".", "").replace(",", "")
        try:
            harga = int(harga_str)
        except ValueError:
            harga = 0
        self.harga_var.set(str(harga))
        try:
            stok = int(values[3])
        except (ValueError, IndexError):
            stok = 0
        self.stok_var.set(stok)

        self.edit_mode = True
        self.edit_id = values[0]
        self.btn_tambah.config(state="disabled")
        self.btn_edit.config(state="normal")

    def hapus_produk(self):
        item = self.tree_produk.selection()
        if not item:
            messagebox.showwarning("⚠️ Peringatan", "Pilih produk yang akan dihapus!")
            return
        if messagebox.askyesno("Konfirmasi", "Yakin hapus produk ini?"):
            id_hapus = self.tree_produk.item(item[0], "values")[0]
            mask = self.produk_df["ID"].astype(str) != str(id_hapus)
            self.produk_df = self.produk_df[mask].reset_index(drop=True)
            self.refresh_produk()
            self.reset_form_produk()
            messagebox.showinfo("✅ Sukses", "Produk berhasil dihapus!")

    def hapus_pesanan(self):
        items = self.tree_pesanan.selection()
        if not items:
            messagebox.showwarning("⚠️ Peringatan", "Pilih pesanan yang akan dihapus!")
            return

        if messagebox.askyesno("Konfirmasi", f"Yakin hapus {len(items)} pesanan terpilih?"):
            # Ambil semua ID Pesanan yang dipilih
            ids_to_delete = []
            for item in items:
                id_pesanan = self.tree_pesanan.item(item, "values")[0]
                ids_to_delete.append(id_pesanan)

            # Hapus dari DataFrame
            self.pesanan_df = self.pesanan_df[~self.pesanan_df["ID Pesanan"].isin(ids_to_delete)].reset_index(drop=True)

            # Perbarui tampilan
            self.refresh_pesanan()
            messagebox.showinfo("✅ Sukses", f"{len(ids_to_delete)} pesanan berhasil dihapus!")

    def cek_stok_rendah(self):
        rendah = self.produk_df[self.produk_df["Stok"] < 5]
        if rendah.empty:
            messagebox.showinfo("✅ Info", "Semua stok dalam kondisi aman!")
        else:
            msg = "⚠️ Stok Rendah:\n\n" + "\n".join([f"• {row['Nama']} ({row['Stok']})" for _, row in rendah.iterrows()])
            messagebox.showwarning("Stok Rendah", msg)

    # ----------------- PESANAN -----------------
    def update_harga_stok(self, event=None):
        nama = self.produk_var.get()
        if not nama:
            return
        row = self.produk_df[self.produk_df["Nama"] == nama]
        if row.empty:
            return
        row = row.iloc[0]
        self.harga_produk_var.set(int(row["Harga"]))
        self.stok_produk_var.set(int(row["Stok"]))
        self.hitung_total()

    def hitung_total(self, *args):
        harga = self.harga_produk_var.get()
        jumlah = self.jumlah_var.get()
        total = harga * jumlah
        self.total_var.set(f"Rp {total:,}".replace(",", "."))

    def proses_pesanan(self):
        pelanggan = self.pelanggan_var.get().strip()
        nama_produk = self.produk_var.get()
        jumlah = self.jumlah_var.get()

        if not pelanggan or not nama_produk:
            messagebox.showerror("❌ Error", "Isi nama pelanggan & pilih produk!")
            return

        if jumlah <= 0:
            messagebox.showerror("❌ Error", "Jumlah harus > 0!")
            return

        produk_row = self.produk_df[self.produk_df["Nama"] == nama_produk]
        if produk_row.empty:
            messagebox.showerror("❌ Error", "Produk tidak ditemukan!")
            return
        row = produk_row.iloc[0]

        if jumlah > row["Stok"]:
            messagebox.showerror("❌ Stok Habis", f"Stok tidak cukup! Tersedia: {row['Stok']}")
            return

        self.produk_df.loc[self.produk_df["Nama"] == nama_produk, "Stok"] -= jumlah
        id_pesanan = f"PSN-{str(len(self.pesanan_df) + 1).zfill(3)}"

        new_pesanan = pd.DataFrame([{
            "ID Pesanan": id_pesanan,
            "Pelanggan": pelanggan,
            "Produk": nama_produk,
            "Jumlah": jumlah,
            "Total": int(row["Harga"]) * jumlah,
            "Tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }])
        self.pesanan_df = pd.concat([self.pesanan_df, new_pesanan], ignore_index=True)

        self.refresh_pesanan()
        self.refresh_produk()
        self.pelanggan_var.set("")
        self.produk_var.set("")
        self.jumlah_var.set(1)
        self.total_var.set("Rp 0")
        messagebox.showinfo("✅ Sukses", f"Pesanan {id_pesanan} berhasil diproses!")

    def refresh_pesanan(self):
        for item in self.tree_pesanan.get_children():
            self.tree_pesanan.delete(item)

        for _, row in self.pesanan_df.iterrows():
            self.tree_pesanan.insert("", "end", values=(
                row["ID Pesanan"],
                row["Pelanggan"],
                row["Produk"],
                row["Jumlah"],
                f"{row['Total']:,}".replace(",", "."),
                row["Tanggal"]
            ))

    def export_excel(self):
        if self.pesanan_df.empty:
            messagebox.showwarning("⚠️ Kosong", "Tidak ada data pesanan untuk diekspor!")
            return

        filepath = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel Files", "*.xlsx")],
            initialfile=f"Pesanan_DigitalMart_{datetime.now().strftime('%Y%m%d')}.xlsx"
        )
        if filepath:
            try:
                self.pesanan_df.to_excel(filepath, index=False)
                messagebox.showinfo("✅ Sukses", f"Data pesanan berhasil disimpan ke:\n{filepath}")
            except Exception as e:
                messagebox.showerror("❌ Error", f"Gagal mengekspor:\n{e}")


# Jalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalMartApp(root)
    root.mainloop()