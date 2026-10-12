# Validasi Email

# --- FUNGSI VALIDASI EMAIL (Diletakkan di bagian paling atas) ---
def deteksi_anomali_email(e):
    errs = []
    if e.count('@') != 1:
        errs.append("Harus memiliki tepat satu karakter @.")
    else:
        l, d = e.split('@')
        if not l or not d:
            errs.append("Bagian local atau domain tidak boleh kosong.")
        if l.startswith('.') or l.endswith('.'):
            errs.append("Bagian local tidak boleh diawali atau diakhiri titik.")
        if '..' in l or '..' in d:
            errs.append("Bagian local/domain tidak boleh mengandung titik berurutan.")
        if '.' not in d or d.startswith('.') or d.endswith('.'):
            errs.append("Bagian domain tidak valid.")
            
    if ' ' in e:
        errs.append("Tidak boleh mengandung spasi.")
    if not e.endswith(('.com', '.id', '.ac.id')):
        errs.append("Wajib berakhiran dengan .com, .id, atau .ac.id.")
        
    return errs

# --- PROGRAM UTAMA INTERAKTIF (Diletakkan di bawah fungsi) ---
print("--- Sistem Pencatatan Email Valid ---")
border = input("Masukkan border dengan karakter bebas: ")
print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

tercatat, valid = [], []

while True:
    em = input("Masukkan email: ").strip()
    if em.lower() == 'tutup':
        break
    if not em:
        continue
        
    anomali = deteksi_anomali_email(em)
    if em in tercatat:
        anomali.append("Email sudah terdaftar (Duplikat).")
        
    if not anomali:
        tercatat.append(em)
        valid.append(em)
        print(">> Email VALID!")
    else:
        print(">> Email DITOLAK karena:")
        for err in anomali:
            print(f"   - {err}")

if valid:
    m = max(len(e) for e in valid) + 4
    print(f"\n--- HASIL EMAIL VALID ---\n{border * m}")
    for v in valid:
        spasi_sisa = m - len(v) - 2
        print(f"| {v}{' ' * spasi_sisa} |")
    print(f"{border * m}")
else:
    print("\nTidak ada email valid yang tercatat.")

