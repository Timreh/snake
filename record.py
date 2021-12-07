import csv
from turtle import Turtle


class Records:
    def __init__(self, size, score) -> None:
        self.size = size
        self.size_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
        self.score = score

    def read_csv(self):
        r = dict()
        with open("record.csv", newline='') as csvfile:
            rows = csv.DictReader(csvfile)
            for i in rows:
                for j in i:
                    if j not in r:
                        r[j] = []
                    r[j].append(i[j])
        return r

    def write_csv(self, record):
        with open("record.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            firstrow = []
            for i in record:
                firstrow.append(i)
            writer.writerow(firstrow)
            for i in range(5):
                row = []
                for j in record:
                    row.append(record[j][i])
                writer.writerow(row)

    def record_judge(self, record):
        player_size = self.size_dict[self.size]
        # print(int(self.record[player_size][4][4:]))
        if self.score > int(record[player_size][4].split(' ')[1]):
            name = input("New Record! , please enter name:")
            for i in range(len(record[player_size])):
                new_record = name + ' ' + str(self.score)
                if self.score > int(record[player_size][i].split(' ')[1]):
                    record[player_size].insert(i, new_record)
                    break
            record[player_size].pop()
            return True, record
        else:
            return False, record

    def display(self, record):
        display_tt = Turtle()
        display_tt.hideturtle()
        # for i in record:
        #     record[i].insert(0, i)

        # 不知道怎麼轉置
        # record[i].insert(0, i)
        # maxstrlen = max(list(map(len, record[i]))) + 2
        # for j in record[i]:
        #     diff = maxstrlen - len(j)
        #     if diff % 2 != 0:
        #         diff += 1
        #     space = diff / 2
        #     app = ""
        #     for k in range(int(space)):
        #         app += " "
        #     j = app + j + app
        #     single_record.append(j)
        # display_board.append(single_record)
        k = 250
        display_tt.goto(0, k)
        display_tt.write("Leader Board",  align="center", font='Arial')
        for i in record:
            k -= 40
            display_tt.goto(0, k)
            display_tt.write(f"snake size {i}: {record[i]}",
                             align="center", font='Arial')

    def exec(self):
        record = self.read_csv()
        new_rc, rc = self.record_judge(record)
        if new_rc:
            self.write_csv(rc)
        self.display(rc)

    def csv_init(self):
        # create an original csv file
        with open('record.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["one", "two", "three", "four", "five"])
            for i in range(5):
                writer.writerow(['na: 0', 'na: 0', 'na: 0', 'na: 0', 'na: 0'])
