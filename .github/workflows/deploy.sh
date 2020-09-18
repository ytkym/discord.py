#!/bin/bash
# outputディレクトリ内のファイルをrsync over SSHで転送
rsync -acvz --delete ./ ${{ secrets.SERVER_HOST }}@${{ secrets.SERVER_USERNAME }}:/${{ secrets.DEST_DIR }}
# サービスを再起動
ssh user@remote "python3 discord.py/examples/basic_bot.py"
