git config --global user.name “Billy-Liu-12”
git config --global user.email “liuhz9903@163.com”

\




git push --set-upstream origin master的原因以及解决方法
我们在首次创建远程仓库，提交代码的时候一般有如下步骤：
1. git init
2. git remote add origin https://XX
3. git add .
4. git remote add origin
5. git push





1.在本地初始化（建立暂存区）
  git init   

2.工作区 => 暂存区
  git add * 
  git commit -m “”

3.从暂存区恢复到工作区
  git checkout readme.md

4.查看工作区和暂存区的版本差异
  git diff

5.清屏
  clear

6.查看已经提交到暂存区的历史版本
  git log

7.恢复文件到指定的一个历史版本
  git reset --hard
  git reset --hard=^^

8.生成ssh密钥
  ssh-keygen -t rsa -C "liuhz9903@163.com"
  .pub
  Github配置密钥

9.暂存区 => 远程仓库
  git remote add origin https://github.com/Billy-Liu-12/dsp-files.git
  git push -u origin master

10.从远程仓库克隆到本地
  git clone

11.从远程仓库同步到本地（更新）
  git pull   
