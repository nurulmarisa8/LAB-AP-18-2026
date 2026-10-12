DOMAIN_RESMI = (".com", ".id", ".ac.id")


def deteksi_anomali_email(email):
    error = []

    if " " in email:
        error.append("Email tidak boleh mengandung spasi.")

    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error

    local, domain = email.split("@")
    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if local.startswith(".") or local.endswith(".") or ".." in local:
        error.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    if not email.lower().endswith(DOMAIN_RESMI):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        return ""
    terpanjang = 0
    for e in daftar_email_valid:
        if len(e) > terpanjang:
            terpanjang = len(e)
    garis = "+" + karakter_border * (terpanjang + 2) + "+"
    baris = [garis]
    for e in daftar_email_valid:
        baris.append("| " + e + " " * (terpanjang - len(e)) + " |")
    baris.append(garis)
    return "\n".join(baris)


def main():
    print("--- Sistem Pencatatan email valid ---")
    border = input("Masukkan border dengan karakter bebas: ")
    border = border[0] if border else "="
    print()
    print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

    valid = []
    while True:
        email = input("Masukkan email: ").strip()
        if email.lower() == "tutup":
            break

        error = deteksi_anomali_email(email)
        if not error and email.lower() in [e.lower() for e in valid]:
            error.append("Email sudah terdaftar (Duplikat).")

        if error:
            print(">> Email DITOLAK karena:")
            for e in error:
                print("   -", e)
        else:
            print(">> Email VALID!")
            valid.append(email)

    print()
    print("--- HASIL EMAIL VALID ---")
    if valid:
        print(cetak_daftar(valid, border))
    else:
        print("(tidak ada email valid)") 

if __name__ == "__main__":
    main()