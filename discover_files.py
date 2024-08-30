from os import walk

from os.path import join

def discover_files(path):

    exfiltrating_files = []

    for root, dir, files in walk(path, ):
        for file in files:
            if file.endswith(".txt") or file.endswith(".bin") or file.endswith(".py"):
                exfiltrating_files.append(join(root, file))
    
    return exfiltrating_files


if __name__ == "__main__":
    
    path = input("Type in the path \n")

    discover_files(path)