import os

def path():
    while True:
        PATH = input("フォルダパスを入力: ")
        try:
            os.chdir(PATH)
            break
        except:
            print("フォルダパスが正しくありません")
            continue
    
    return PATH

def main():
    PATH = path()

    files = [f for f in os.listdir(PATH) if os.path.isfile(os.path.join(PATH, f))]
    files.sort(key=lambda f: os.path.getmtime(os.path.join(PATH, f)))

    total_files = len(files)
    zero_filled_format = "{:0" + str(len(str(total_files)) + 1) + "d}"

    for i, file_name in enumerate(files, start=1):
        _, file_ext = os.path.splitext(file_name)
        new_file_name = zero_filled_format.format(i) + file_ext
        os.rename(os.path.join(PATH, file_name), os.path.join(PATH, new_file_name))

    print(f"{total_files} 個のファイルを連番リネームしました。")


while True:
    try:
        main()
    except KeyboardInterrupt:
        print("終了します")
        break