#可以双击直接运行以更新
nowtime=`date +%F_%H:%M`
git init
git add -A
git commit -m "这是${nowtime}的维护日志，由wqy88程序自动创建"
git remote rm mylink
git remote add mylink git@gitee.com:wqy88/links.git
#强制更新到远程 git push -f mylink master
git push mylink master
git remote rm link
git remote add link git@github.com:wqy88/links.git
git push link master 
#read -p "Press [Enter] key to continue."
