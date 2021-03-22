import json
import os


class Icswriter(object):
    def __init__(self, year=50, file_loc='calender.json', save_dir='输出目录'):
        '''
        :param year: 想生成多少年的，比如10年的生日
        :param file_loc: 日历json的位置，一般不用管
        :param save_dir: 输出文件夹
        '''
        self.year = year
        self.dir = save_dir
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        with open(file_loc, 'r') as f:
            self.jsondata = json.load(f)

    def run(self, name: str, month: int, day: int):
        '''
        :param name: 姓名
        :param month:  农历月份，输入数字
        :param day: 农历日份，输入数字
        :return:
        '''
        if month not in range(1, 13) or day not in range(1, 31):
            return 'error'
        f = open(os.path.join(self.dir, name + '.ics'), 'w', encoding='utf-8')
        f.write('BEGIN:VCALENDAR' + '\n')
        f.write('PRODID:-//Google Inc//Google Calendar 70.9054//EN' + '\n')
        f.write('VERSION:2.0' + '\n')
        for i in range(2021, 2021 + self.year):
            data = self.jsondata[str(i)][str(month)][str(day)]
            self.writefile(f, name, data)
        f.write('END:VCALENDAR' + '\n')
        f.close()

    def writefile(self, f, name, data):
        f.write('BEGIN:VEVENT' + '\n')
        f.write('DTSTART;VALUE=DATE:' + data + '\n')
        f.write('DTEND;VALUE=DATE:' + str(int(data) + 1) + '\n')
        f.write('CLASS:PRIVATE' + '\n')
        f.write('DESCRIPTION:' + '\n')
        f.write('LOCATION:' + '\n')
        f.write('SEQUENCE:0' + '\n')
        f.write('STATUS:CONFIRMED' + '\n')
        f.write('SUMMARY:' + name + '生日' + '\n')
        f.write('TRANSP:TRANSPARENT' + '\n')
        f.write('END:VEVENT' + '\n')


if __name__ == '__main__':
    ics = Icswriter(10)
    ics.run('自己', 1, 9)
