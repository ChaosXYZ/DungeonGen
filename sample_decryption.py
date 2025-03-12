def decrypt(a):
    print("Number of Missions: ", a[0:2])
    print("Missions: ", ','.join([a[2+i:6+i] for i in range(0,37,4)]))
    return "Success"

if __name__ == '__main__':
    inp = "780024063201520532014505250135025702340624"
    print(decrypt(inp))