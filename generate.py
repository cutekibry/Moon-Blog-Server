#!/usr/bin/python3
import config
from classes import env, markdown, Solution, Solution_list, Article, Article_list
import argparse
import datetime
import json
import pathlib
import shutil

env.globals.update({
    "BUILD_TIME": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC+8")
})

# Add argparse
parser = argparse.ArgumentParser()
parser.add_argument("src")
parser.add_argument("dest")
args = parser.parse_args()

# Init directories
src = pathlib.Path(args.src).absolute()
if not src.exists():
    raise RuntimeError("The source path \"%s\" does not exists" % args.src)
elif not src.is_dir():
    raise RuntimeError("The source path \"%s\" is not a directory" % args.src)
dest = pathlib.Path(args.dest).absolute()
lib = pathlib.Path().absolute().parent

content = src / "content"

# Remove directories
remove_list = ["about", "article", "articles",
               "static", "solution", "solutions", "index.html"]

for x in remove_list:
    if dest.joinpath(x).exists():
        if dest.joinpath(x).is_dir():
            shutil.rmtree(str(dest / x))
        else:
            dest.joinpath(x).unlink()

# Make directories
mkdir_list = ["article", "articles", "solution", "solutions"]

for x in mkdir_list:
    dest.joinpath(x).mkdir()

# Copy static files
shutil.copytree(src / "static", dest / "static")

# Generate home page
notice = markdown(content.joinpath("notice.md").read_text(encoding="utf-8"))
comments = json.loads(
    src.joinpath("comments.json").read_text(encoding="utf-8")
)
dest.joinpath("index.html").write_text(env.get_template("home.j2").render(
    notice=notice,
    comments=comments,
    sentences=config.sentences,
    links=config.links,
), encoding="utf-8")

# Get solution set && Generate solution page
solutions = dict()
solutions[0] = Solution_list("solutions")

for x in content.joinpath("solutions").iterdir():
    filename = x.with_suffix("").name
    oj, id_, name = filename.split(" ", 2)
    text = x.read_text(encoding="utf-8")
    solution = Solution(oj, id_, name, text)

    dir = dest.joinpath("solution/%s %s" % (oj, id_))
    dir.mkdir()
    dir.joinpath("index.html").touch()
    dir.joinpath("index.html").write_text(solution.parse())

    solutions[0].append(solution)
    for tag in solution.tags:
        if not solutions.get(tag.id):
            solutions[tag.id] = Solution_list("solutions/tag/%d" % tag.id)
        solutions[tag.id].append(solution)

# Generate solution list page
for i, a in solutions.items():
    a.sort()

    pages = a.parse()
    dir = dest.joinpath(a.baseurl)
    dir.mkdir(parents=True, exist_ok=True)
    for j, x in enumerate(pages, 1):
        dir.joinpath("%d" % j).mkdir()
        dir.joinpath("%d/index.html" % j).touch()
        dir.joinpath("%d/index.html" % j).write_text(x, encoding="utf-8")
    dir.joinpath("index.html").touch()
    dir.joinpath("index.html").write_text(pages[0], encoding="utf-8")

# Get article set && Generate article page
# Note: I just copy the codes above again
articles = dict()
articles[0] = Article_list("articles")

for x in content.joinpath("articles").iterdir():
    filename = x.with_suffix("").name
    name = filename
    text = x.read_text(encoding="utf-8")
    article = Article(name, text)

    dir = dest.joinpath("article/%s" % name)
    dir.mkdir()
    dir.joinpath("index.html").touch()
    dir.joinpath("index.html").write_text(article.parse())

    articles[0].append(article)
    for tag in article.tags:
        if not articles.get(tag.id):
            articles[tag.id] = Article_list("articles/tag/%d" % tag.id)
        articles[tag.id].append(article)

# Generate article list page
for i, a in articles.items():
    a.sort()

    pages = a.parse()
    dir = dest.joinpath(a.baseurl)
    dir.mkdir(parents=True, exist_ok=True)
    for j, x in enumerate(pages, 1):
        dir.joinpath("%d" % j).mkdir()
        dir.joinpath("%d/index.html" % j).touch()
        dir.joinpath("%d/index.html" % j).write_text(x, encoding="utf-8")
    dir.joinpath("index.html").touch()
    dir.joinpath("index.html").write_text(pages[0], encoding="utf-8")

# Generate about page
text = markdown(content.joinpath("about.md").read_text(encoding="utf-8"))
dir = dest.joinpath("about")
dir.mkdir()
dir.joinpath("index.html").touch()
dir.joinpath("index.html").write_text(env.get_template("about.j2").render(text=text))