#!/bin/bash
# outputディレクトリ内のファイルをrsync over SSHで転送
rsync -acvz --delete ./ ${{ secrets.SERVER_USERNAME }}@${{ secrets.SERVER_HOST}}:/${{ secrets.DEST_DIR }}
# サービスを再起動
ssh ${{ secrets.SERVER_USERNAME }}@${{ secrets.SERVER_HOST}} "python3 discord.py/examples/basic_bot.py"
