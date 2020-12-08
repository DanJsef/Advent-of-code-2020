import re
import sys

sys.setrecursionlimit(1500)


class DFS():
    def __init__(self, data):
        self.rules = self.parse_rules(data)
        self.stack = list()
        self.count = -1
        self.bags = 0

    def parse_rules(self, data):
        rules = dict()
        data = data.split('\n')
        for rule in data:
            rule = re.sub(r' bags| bag|\s|\.', "", rule)
            rule = re.split('contain|,', rule)
            name = rule.pop(0)
            contains = list()
            if rule[0] != 'noother':
                for item in rule:
                    contains.append(tuple((item[1:], int(item[:1]))))
            else:
                contains.append(False)
            rules[name] = contains
        return rules

    # NOTE: very ineffective can be optimized by saving state of already scanned components
    def can_contain(self, rule, searched):
        if rule == searched:
            self.count += 1
            self.stack.clear()

        for item in self.rules[rule]:
            if item != False:
                self.stack.append(item)

        if len(self.stack) > 0:
            item = self.stack.pop()
            self.can_contain(item[0], searched)

    def bag_contains(self, search, multiply):

        for item in self.rules[search]:
            if item != False:
                self.bags += multiply * item[1]
                self.bag_contains(item[0], multiply*item[1])


dfs = DFS(open('input.txt', 'r').read())

for rule in dfs.rules:
    dfs.can_contain(rule, 'shinygold')

dfs.bag_contains('shinygold', 1)

print(dfs.count, dfs.bags)
