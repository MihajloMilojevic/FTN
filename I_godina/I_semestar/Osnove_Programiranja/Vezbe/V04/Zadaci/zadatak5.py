def calc(list):
    s = 0
    for a in list:
        s += a
    return s, s/len(list)

def main():
    fileUsers = open("users.txt", "r")
    fileAccounts = open("accounts.txt", "r")
    fileStatistics = open("statistics.txt", "w")

    users = [row[:-1].split("|") for row in fileUsers.readlines()]
    accounts = [[float(x) for x in row[:-1].split("|")] for row in fileAccounts.readlines()]

    statistic = []

    for i in range(len(users)):
        pass


    fileUsers.close()
    fileAccounts.close()
    fileStatistics.close()
        
if __name__ == "__main__":
    main()