def deteksi_anomali_email(email):
    error = []

    # 1. Harus memiliki tepat satu karakter @
    if email.count("@") != 1:
        error.append(
            "Harus memiliki tepat satu karakter @."
        )

    # 2. Bagian local dan domain tidak boleh kosong
    if email.count("@") == 1:
        posisi_at = email.find("@")

        local = email[:posisi_at]
        domain = email[posisi_at + 1:]

        if local == "" or domain == "":
            error.append(
                "Bagian sebelum @ (local) atau setelah @ (domain) "
                "tidak boleh kosong."
            )

    # 3. Tidak boleh mengandung spasi
    if email.find(" ") != -1:
        error.append(
            "Email tidak boleh mengandung spasi."
        )

    # 4. Bagian local tidak boleh diawali/diakhiri titik
    #    dan tidak boleh mengandung titik berurutan
    if email.count("@") == 1:
        posisi_at = email.find("@")
        local = email[:posisi_at]

        if local != "":
            if local[0] == "." or local[-1] == ".":
                error.append(
                    "Bagian local tidak boleh diawali atau "
                    "diakhiri titik."
                )

            if local.find("..") != -1:
                error.append(
                    "Bagian local tidak boleh mengandung "
                    "titik berurutan."
                )

    # 5. Bagian domain wajib memiliki minimal satu titik
    #    tidak boleh titik berurutan
    #    dan tidak boleh diakhiri titik
    if email.count("@") == 1:
        posisi_at = email.find("@")
        domain = email[posisi_at + 1:]

        # Domain kosong juga tidak memiliki titik
        if domain.find(".") == -1:
            error.append(
                "Bagian domain wajib memiliki minimal satu titik."
            )

        if domain != "":
            if domain.find("..") != -1 or domain[-1] == ".":
                error.append(
                    "Bagian domain tidak boleh mengandung titik "
                    "berurutan atau diakhiri titik."
                )

    # 7. Wajib berakhiran .com, .id, atau .ac.id
    if email.count("@") == 1:
        posisi_at = email.find("@")
        domain = email[posisi_at + 1:]

        if not (
            domain.endswith(".com")
            or domain.endswith(".id")
            or domain.endswith(".ac.id")
        ):
            error.append(
                "Wajib berakhiran dengan .com, .id, atau .ac.id"
            )

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    panjang_maksimal = 0

    # Mencari email terpanjang
    for email in daftar_email_valid:
        if len(email) > panjang_maksimal:
            panjang_maksimal = len(email)

    # Tambahan 2 spasi: kiri dan kanan
    lebar = panjang_maksimal + 2

    hasil = ""

    # Garis atas
    hasil += "+" + karakter_border * lebar + "\n"

    # Isi bingkai
    for email in daftar_email_valid:
        jumlah_spasi = panjang_maksimal - len(email)

        hasil += "| " + email
        hasil += " " * jumlah_spasi
        hasil += " |\n"

    # Garis bawah
    hasil += "+" + karakter_border * lebar

    return hasil


# =========================
# PROGRAM UTAMA
# =========================

try:
    print("--- Sistem Pencatatan email valid ---")

    karakter_border = input(
        "Masukkan border dengan karakter bebas: "
    )

    # ValueError untuk border kosong
    if karakter_border == "":
        raise ValueError(
            "Karakter border tidak boleh kosong."
        )

    # Border harus satu karakter
    if len(karakter_border) != 1:
        raise ValueError(
            "Karakter border harus satu karakter."
        )

    print()

    print(
        "Ketik 'tutup' untuk mengakhiri masukan "
        "dan mencetak email."
    )

    daftar_email_valid = []

    # Menerima email sampai mengetik "tutup"
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
        print(
            cetak_daftar(
                daftar_email_valid,
                karakter_border
            )
        )

except ValueError as error_border:
    print("Error:", error_border)