# -*- coding: UTF-8 -*-
import os
import click
import shutil

import PyInstaller.__main__

############################################

EXEC_NAME = "word_question"
RESOURCE_PATH = [
    ["src/resource", "src/resource"],
    ["question_word/初上", "question_word/初上"],
    ["question_word/初下", "question_word/初下"],
]
MAIN_FILE = os.path.join("src", "main.py")
ICON_PATH = "src/resource/favicon.ico"
############################################


@click.group()
def cli():
    pass


@cli.command()
def build():
    build_args = []
    build_args.append(f"--name={EXEC_NAME}")

    build_args.append("--onefile")

    if os.name == "nt":
        split = ";"
    else:
        split = ":"
    for resource_path in RESOURCE_PATH:
        build_args.append(f"--add-data={split.join(resource_path)}")

    build_args.append(f"--icon={ICON_PATH}")

    build_args.append("--windowed")

    build_args.append("--noconsole")

    build_args.append(MAIN_FILE)

    PyInstaller.__main__.run(build_args)


@cli.command()
def clean():
    clean_list = []
    clean_list.append("./build")
    clean_list.append("./dist")
    clean_list.append(EXEC_NAME + ".spec")

    for i in clean_list:
        if os.path.exists(i):
            if os.path.isdir(i):
                shutil.rmtree(i)
            else:
                os.remove(i)


if __name__ == "__main__":
    cli()
