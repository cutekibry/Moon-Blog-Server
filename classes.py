#!/usr/bin/python3
import config
import yaml
import mistune
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('layout'))
env.globals.update(config.globals)


markdown = mistune.Markdown()


# Init tag dict
tagdict = dict()
for i, x in enumerate(config.tags):
    tagdict[x[0]] = i


def getmeta(text):
    if text[:3] == '---' and text.find('---', 3) != - 1:
        p = text.find('---', 3)
        meta = yaml.load(text[3: p].strip())
        text = text[p + 3:].strip()
    else:
        meta = dict()
    return [text, meta]


class Tag():
    """Tag class."""

    def __init__(self, name, type):
        if not tagdict.get(name):
            tagdict[name] = len(config.tags)
            config.tags.append([name, "white"])
        self.id = tagdict[name]
        self.color, self.name = config.tags[self.id]
        self.type = type

    def parse(self):
        return "<a href=\"/%s/tag/%d\" class=\"ui tiny %s label\">%s</a>" % (self.type, self.id, self.name, self.color)


class Article():
    """Article class."""

    def __init__(self, name, text):
        self.name = name
        text, self.meta = getmeta(text)

        self.codename = self.meta['codename']
        self.text = markdown(text)

        self.tags = sorted(
            [Tag(str(x).strip(), 'articles') for x in self.meta.get('tags', [])], key=lambda x: x.id)
        self.top = self.meta.get('top', False)

    def parse(self):
        return env.get_template('article.j2').render(article=self)


class Solution():
    """Article class."""

    def __init__(self, oj, id, name, text):
        self.oj = oj
        self.id = id
        self.name = name
        text, self.meta = getmeta(text)

        self.text = markdown(text)

        self.link = config.ojlink_patterns[self.oj](self.id)

        self.tags = sorted(
            [Tag(str(x).strip(), 'solutions') for x in self.meta.get('tags', [])], key=lambda x: x.id)

        p1 = text.find('## 题目描述')
        p2 = text.find('## 输入格式')
        p3 = text.find('## 输出格式')
        p4 = text.find('## 样例')
        p5 = text.find('## 数据范围与提示')
        p6 = text.find('## 题解')
        p7 = text.find('## 代码')
        self.description = markdown(text[p1 + len('## 题目描述'):p2].strip())
        self.input_format = markdown(text[p2 + len('## 输入格式'):p3].strip())
        self.output_format = markdown(text[p3 + len('## 输出格式'):p4].strip())
        self.example = markdown(text[p4 + len('## 样例'):p5].strip())
        self.hint = markdown(text[p5 + len('## 数据范围与提示'):p6].strip())
        self.solution = markdown(text[p6 + len('## 题解'):p7].strip())
        self.code = markdown(text[p7 + len('## 代码'):].strip())

        self.memory_limit = self.meta.get('memory_limit', 256)
        self.time_limit = self.meta.get('time_limit', 1000)
        self.input_file = self.meta.get('input_file', '')
        self.output_file = self.meta.get('output_file', '')

        self.special_judge = self.meta.get('special_judge', False)
        self.upload_answer = self.meta.get('upload_answer', False)

    def parse(self):
        return env.get_template('solution.j2').render(solution=self)


class Article_list():
    """Article list class."""

    def __init__(self, baseurl):
        self.articles = []
        self.baseurl = baseurl

    def sort(self, key=lambda x: ('0' if x.top else '1') + x.codename):
        self.articles = sorted(self.articles, key=key)

    def append(self, article):
        self.articles.append(article)

    def parse(self):
        n = len(self.articles)
        pages = n // config.globals["ARTICLES_PER_PAGE"]
        if n % config.globals["ARTICLES_PER_PAGE"]:
            pages += 1

        res = []
        l = 0
        r = min(config.globals["ARTICLES_PER_PAGE"], n)
        for i in range(1, pages + 1):
            a = self.articles[l: r]
            html = env.get_template('article_list.j2').render(
                articles=a,
                no=i,
                tot=pages,
                baseurl=self.baseurl,
            )
            res.append(html)

            l += config.globals["ARTICLES_PER_PAGE"]
            r = min(r + config.globals["ARTICLES_PER_PAGE"], n)
        return res


class Solution_list():
    """Solution list class."""

    def __init__(self, baseurl):
        self.solutions = []
        self.baseurl = baseurl

    def sort(self, key=lambda x: x.oj + (" %05s" % x.id)):
        self.solutions = sorted(self.solutions, key=key)

    def append(self, solution):
        self.solutions.append(solution)

    def parse(self):
        n = len(self.solutions)
        pages = n // config.globals["ARTICLES_PER_PAGE"]
        if n % config.globals["ARTICLES_PER_PAGE"]:
            pages += 1

        res = []
        l = 0
        r = min(config.globals["ARTICLES_PER_PAGE"], n)
        for i in range(1, pages + 1):
            a = self.solutions[l: r]
            html = env.get_template('solution_list.j2').render(
                solutions=a,
                no=i,
                tot=pages,
                baseurl=self.baseurl,
            )
            res.append(html)

            l += config.globals["ARTICLES_PER_PAGE"]
            r = min(r + config.globals["ARTICLES_PER_PAGE"], n)
        return res
