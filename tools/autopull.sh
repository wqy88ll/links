git init
git remote rm mylink
git remote add mylink https://gitee.com/wqy88/links.git
git pull mylink master

## 从远程仓库强制下载最新版本
#git fetch -all 
# 将本地设为刚获取的最新的内容
#git reset --hard mymk/master