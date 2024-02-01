def main():
    text = input("File Name: ")
    listName = text.split(".")

    ext = listName[len(listName)-1]
    extension = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]
    if ext in extension:
        print(f"image/{ext}")
    else:
        print("application/octet-stream")

main()