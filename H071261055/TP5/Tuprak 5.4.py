def deteksi_anomali_email(email):
    """Cek 6 aturan validasi. Return list deskripsi aturan yang dilanggar."""
    error = []

    # Aturan 1: tepat satu '@'
    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error

    local, domain = email.split("@")

    # Aturan 2: local & domain tidak kosong
    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    # Aturan 3: tidak boleh ada spasi
    if " " in email:
        error.append("Tidak boleh mengandung spasi.")

    # Aturan 4: aturan titik pada local
    if local != "" and (local.startswith(".") or local.endswith(".") or ".." in local):
        error.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    # Aturan 5: aturan domain
    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")
    if domain != "" and (".." in domain or domain.endswith(".")):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    # Aturan 7: domain resmi
    if not email.lower().endswith((".com", ".id", ".ac.id")):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    """Bangun string multi-baris berbingkai; lebar mengikuti email terpanjang."""
    if not daftar_email_valid:
        return "(Tidak ada email valid)"

    terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    garis = "+" + karakter_border * (terpanjang + 2) + "+"
    baris = [garis]
    for email in daftar_email_valid:
        baris.append("| " + email + " " * (terpanjang - len(email)) + " |")
    baris.append(garis)
    return "\n".join(baris)


def main():
    daftar_email_valid = []

    try:
        print("--- Sistem Pencatatan email valid ---")
        karakter_border = input("Masukkan border dengan karakter bebas: ")

        # ValueError untuk border kosong
        if karakter_border == "":
            raise ValueError("Karakter border tidak boleh kosong.")
        karakter_border = karakter_border[0]

        print()
        print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

        while True:
            try:
                email = input("Masukkan email: ")

                # Mengakhiri input
                if email.lower() == "tutup":
                    break

                # ValueError untuk email kosong
                if email == "":
                    raise ValueError(
                        "Email tidak boleh kosong."
                    )

                # Memeriksa aturan email
                error = deteksi_anomali_email(email)

                # 6. Tidak boleh ada email duplikat
                if len(error) == 0:
                    if email in daftar_email_valid:
                        error.append(
                            "Email sudah terdaftar (Duplikat)."
                        )
                    else:
                        daftar_email_valid.append(email)

                # Email valid
                if len(error) == 0:
                    print(">> Email VALID!")

                # Email tidak valid
                else:
                    print(">> Email DITOLAK karena:")

                    for i in range(len(error)):
                        print("   - " + error[i])

            except ValueError as error_input:
                print(">> Email DITOLAK karena:")
                print("   - " + str(error_input))

        # =========================
        # HASIL EMAIL VALID
        # =========================

        print()
        print("--- HASIL EMAIL VALID ---")

        if len(daftar_email_valid) > 0:
            print(cetak_daftar(daftar_email_valid, karakter_border))

    except ValueError as error_border:
        print("Error:", error_border)

if __name__ == "__main__":
    main()