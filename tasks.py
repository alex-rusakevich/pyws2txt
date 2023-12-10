import os

from invoke import run, task


@task()
def build(context, folder_mode=False, upx_disabled=False):
    upx = ""

    if os.path.exists("./.upx") and os.path.isdir("./.upx") and not upx_disabled:
        print("upx found at ./.upx!")
        upx = "--upx-dir=.upx/"

    run(
        f'pyinstaller \
--name=pyws2txt \
--noconfirm {"--onefile" if not folder_mode else ""} {upx} \
-i "NONE" \
"./pyws2txt.py"'
    )
