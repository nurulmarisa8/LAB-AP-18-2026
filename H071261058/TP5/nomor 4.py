DOMAIN_RESMI = (".com", ".id", ".ac.id")


def deteksi_anomali_email(email):
    pelanggaran = []

    if email.count("@") != 1:
        pelanggaran.append("Harus memiliki tepat satu karakter @.")
        if " " in email:
            pelanggaran.append("Tidak boleh mengandung spasi.")
        return pelanggaran  

    local, domain = email.split("@")

    if local == "" or domain == "":
        pelanggaran.append(
            "Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong."
        )

    if " " in email:
        pelanggaran.append("Tidak boleh mengandung spasi.")

    if local.startswith(".") or local.endswith(".") or ".." in local:
        pelanggaran.append(
            "Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan."
            )

    if "." not in domain:
        pelanggaran.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        pelanggaran.append(
            "Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik."
        )

    if not email.lower().endswith(DOMAIN_RESMI):
        pelanggaran.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return pelanggaran


def cetak_daftar(daftar_email_valid, karakter_border):
    karakter_border = karakter_border[:1] or "="
    terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    lebar = terpanjang + 2  
    garis = "+" + karakter_border * lebar + "+"

    baris = [garis]
    for email in daftar_email_valid:
        baris.append("| " + email.ljust(terpanjang) + " |")
    baris.append(garis)
    return "\n".join(baris)


def main():
    print("--- Sistem Pencatatan email valid ---")
    border = input("Masukkan border dengan karakter bebas: ")
    print()
    print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

    daftar_valid = []
    while True:
        email = input("Masukkan email: ")
        if email.strip().lower() == "tutup":
            break

        pelanggaran = deteksi_anomali_email(email)

        sudah_ada = [e.lower() for e in daftar_valid]
        if email.lower() in sudah_ada:
            pelanggaran.append("Email sudah terdaftar (Duplikat).")

        if pelanggaran:
            print(">> Email DITOLAK karena:")
            for p in pelanggaran:
                print("   - " + p)
        else:
            print(">> Email VALID!")
            daftar_valid.append(email)

    print()
    print("--- HASIL EMAIL VALID ---")
    if daftar_valid:
        print(cetak_daftar(daftar_valid, border))
    else:
        print("(tidak ada email valid)")
main()