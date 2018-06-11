judul = 'Game DnD: Sekolah atau Tidur?'
author = 'Programmer Kahfi & Eko'
tanggal = 'Juni 2018'

print(judul)
print(author)
print(tanggal)

tokoh = input('Namamu? ')
tokoh = tokoh.capitalize()
nilai = 0
print('Ketik help untuk mendapatkan bantuan')
print('--' * 20)

running = True
while running:
    print('Seorang anak bernama %s, terlihat sedang tertidur di tempat tidurnya, di awal waktu subuh' % tokoh)
    perintah = input('>')

    if perintah == 'tidur':
        print('Waduh, padahal sekarang sudah mau ujian akhir. Kok %s malah tidur' % tokoh)
        running = False
    elif perintah == 'help':
        print('Perintah yang dikenal adalah: bangun dan tidur\n')
    elif perintah == 'bangun':
        print('%s mengejapkan matanya dan melihat ke sekeliling. Dia melihat meja belajar, sajadah dan PC' %tokoh)

        masih_bangun = True
        masih_belajar = False
        masih_sholat = False
        masih_PC = False

        while masih_bangun:
            perintah = input('>')

            if perintah == 'help':
                print('Perintah yang dikenal adalah: berangkat sekolah, pakai PC, pakai sajadah dan pakai meja belajar')
            elif perintah == 'pakai meja belajar':
                if masih_belajar == False:
                    masih_belajar = True
                    nilai = nilai + 10
                    print('%s pergi ke meja belajar-nya dan melihat di jadwal, bahwa besok ada ulangan Matematika.\n'
                          '%s berkata dalam hati, "Owh besok ada ulangan matematika! Aku sudah siap sih, tapi coba aku cek lagi materinya.\n'
                          'Supaya lebih yakin saat ulangan nanti.'
                          ''
                          'Maka, %s pun mulai membuka-buka buku matematikanya."' % (tokoh,tokoh,tokoh))
                else:
                    print('Kamu sudah belajar')
            elif perintah == 'pakai sajadah':
                if masih_sholat == False:
                    masih_sholat = True
                    nilai = nilai + 20
                    print('Melihat jam dinding yang masih menunjukkan jam 4 pagi, maka %s bergegas mengambil wudhu,\n'
                          'dan menggelar sajadah untuk mendirikan sholat Tahajjud.\n'
                          '%s dengan khusyu menyelesaikan tahajjud dua raka''at dengan ringan dan selanjutnya berdoa,\n'
                          '"Ya Allah, mudahkanlah aku dalam belajar dan berprestasi. Amin"' %(tokoh,tokoh))
                else:
                    print('Sudah sholat')
            elif perintah == 'pakai PC':
                if masih_PC == False:
                    masih_PC = True
                    nilai = nilai + 4
                    print('%s menyalakan PC dan menunggu sampai desktop Windows muncul di layar.\n'
                          'Melihat-lihat sebentar, kemudian %s memutuskan untuk bermain salah satu game di Steam.\n'
                          '%s memutuskan untuk bermain Overload: salah satu game tembak-tembakan dengan pesawat tempur.\n'
                          'Game ini sebenarnya sudah mendukung VR, namun %s belum melengkapi PC-nya dengan sistem VR.'
                          % (tokoh,tokoh,tokoh,tokoh))
                else:
                    print('Sudah bermain')
            elif perintah == 'berangkat sekolah':
                masih_bangun = False
                running = False


    else:
        print('Perintah tidak di kenal')

print('--' * 20)
print('PERMAINAN SELESAI')
print('Nilai %s adalah %d' %(tokoh,nilai))
print('Terimakasih telah memainkan permainan ini.')
print('Untuk berkenalan, silahkan kirim email ke azanjabiil@gmail.com')
