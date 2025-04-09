用法：
- 打开 exportMarkdownBase64ImageToLocal.py
设置文件夹路径: exportMarkdownBase64ImageToLocal.py 所在的路径
path = "文件夹目录"

- 把需要处理的 Markdown 文件放置在 path 下
- 把需要处理的文件的文件名登记到 targets.txt 
- 运行 exportMarkdownBase64ImageToLocal.py

生成的文件：
- 图片导出到 images 文件夹中
- 导出图片后的文件：target1.md 
- 导出图片后去除空行的文件：nb-target1.md 

注意事项：
导出文件后，目标文件嵌入图片的默认格式如下：
```text
![[图片]]
```
如果不符合需求，请根据自己的需要修改 python 脚本。


