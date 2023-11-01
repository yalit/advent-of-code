class File:
    def __init__(self, name: str, size: str):
        self.name: str = name
        self.size: int = int(size)


class Folder:
    def __init__(self, name, parent=None):
        self.files: list[File] = []
        self.directories: dict[str, Folder] = {}
        self.name: str = name
        self.parent: Folder = parent
        self.size: int = 0


def setSize(folder: Folder):
    for d in folder.directories.values():
        setSize(d)
    folder.size = sum([f.size for f in folder.files]) + sum(d.size for d in folder.directories.values())


def initTreeFolder(lines: list[str]) -> Folder:
    root = Folder('root')
    currentNode = root
    for line in lines:
        if line[0:4] == '$ ls':
            continue
        if line[0:3] == 'dir':
            currentNode.directories[line[4:]] = Folder(line[4:], currentNode)
            continue
        if line[0:4] == "$ cd" and line[5:] == '..':
            currentNode = currentNode.parent
            continue
        if line[0:4] == "$ cd":
            currentNode = currentNode.directories[line[5:]]
            continue

        fileInfo = line.split(' ')
        currentNode.files.append(File(fileInfo[1], fileInfo[0]))

    setSize(root)
    return root


def getAllFolderSizes(folder: Folder) -> list[int]:
    if (len(folder.directories)) == 0:
        return [folder.size]

    allFolderSize = [folder.size]
    for f in folder.directories.values():
        allFolderSize += getAllFolderSizes(f)

    return allFolderSize


def handle_part_1(lines: list[str]) -> int:
    root = initTreeFolder(lines[1:])
    return sum([x for x in getAllFolderSizes(root) if x <= 100000])


def handle_part_2(lines: list[str]) -> int:
    root = initTreeFolder(lines[1:])
    return [x for x in sorted(getAllFolderSizes(root)) if root.size - x <= 40000000][0]
