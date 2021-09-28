import glob


def getFolder():
    srcStr = r"""
Please input the full destination folder(ex. C:\Users\abcd1\Class\Embedded System):
    >"""
    srcDir = input(srcStr)
    print()
    return srcDir


def heicChanger(files1, files2):
    import tqdm

    for f in tqdm.tqdm(files1):
        print()
        print(f)
        convert(f)

    for f in tqdm.tqdm(files2):
        print()
        print(f)
        convert(f)


def convert(f):
    import os
    from wand.image import Image  # wand needs imagemagick
    import wand

    try:
        img = Image(filename=f)
        img.format = "jpg"
        img.save(filename=(f[:-4] + "jpg"))
        img.close()
        os.remove(f)

    except BaseException as e:
        print(e.args)
        pass


if __name__ == "__main__":
    srcPath = getFolder()

    files1 = [f for f in glob.glob(srcPath + "**/*.heic", recursive=True)]  # heic
    files2 = [f for f in glob.glob(srcPath + "**/*.heif", recursive=True)]  # heic

    heicChanger(files1, files2)
