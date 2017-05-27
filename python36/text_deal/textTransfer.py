# -*- coding: utf-8 -*-
import os
import re

class TextAnalysis:
	"文本解析类"
	def __init__(self, content):
		super(TextAnalysis, self).__init__()
		self.content = content
	def deal(self):
		# 查找顺序1.一级标题，2.二级标题，3.三级标题，4.加粗文本，5.普通文本，6.居中图片 7.居中加粗文字 8.居中图片下方解释文字
		pattern_title01 = re.compile(r'#\s')    # 一级标题匹配:'# '
		pattern_title02 = re.compile(r'##\s')   # 二级标题匹配:'## '
		pattern_title03 = re.compile(r'###\s')  # 三级标题匹配:'### '
		pattern_contentB = re.compile(r'#b\s')  # 加粗文本:'#b '
		pattern_contentCustom = re.compile(r'#p\s') #普通文本: '#p '
		pattern_imgCenter = re.compile(r'#i\s')   #居中图片: '#i '
		pattern_textCenter = re.compile(r'#c\s')  #居中加粗文字: '#c '
		pattern_textImgC = re.compile(r'#ci\s')   #居中图片解释: '#ci '

		m_title01 = pattern_title01.match(self.content)
		m_title02 = pattern_title02.match(self.content)  
		m_title03 = pattern_title03.match(self.content)  
		m_contentB = pattern_contentB.match(self.content)
		m_contentCustom= pattern_contentCustom.match(self.content)
		m_imgCenter = pattern_imgCenter.match(self.content)
		m_textCenter = pattern_textCenter.match(self.content)
		m_textImgC = pattern_textImgC.match(self.content)

		if m_title01:
			content_deal = self.content[2:]
			content_final = '<div class="title_01">' + content_deal + '</div>'
			return content_final

		if m_title02:
			content_deal = self.content[3:]
			content_final = '<div class="title_02">' + content_deal + '</div>'
			return content_final

		if m_title03:
			content_deal = self.content[4:]
			content_final = '<div class="title_03">' + content_deal + '</div>'
			return content_final

		if m_contentB:
			content_deal = self.content[3:]
			content_final = '<div class="content_bold">' + content_deal + '</div>'
			return content_final

		if m_contentCustom:
			content_deal = self.content[3:]
			content_final = '<div class="content_custom">' + content_deal + '</div>'
			return content_final

		if m_imgCenter:
			s = self.content
			array = s.split('[]')
			img = '<img class="center_img" src="%s" alt="%s">' % (array[0][3:],array[1])
			return img	

		if m_textCenter:
			content_deal = self.content[3:]
			content_final = '<div class="content_center">' + content_deal + '</div>'
			return content_final

		if m_textImgC:
			content_deal = self.content[4:]
			content_final = '<div class="content_img_center">' + content_deal + '</div>'
			return content_final


html_head_content = open("temp.html")
html_head = html_head_content.read();

files = os.listdir(os.getcwd() + '/' + 'source')
for file in files: #遍历文件夹  
	result_name = file[:-3]
	file_analysis = open(os.getcwd() + '/' + 'source' + '/' + file)
	while 1:
	    line = file_analysis.readline()
	    if not line:
	        break
	    else:
	    	Text = TextAnalysis(line)
	    	content_write = Text.deal()
	    	if content_write is not None:
	    		currentDir = os.getcwd() + '/' + 'result'
	    		if not os.path.exists(currentDir):
	    			os.makedirs(currentDir)
	    		# html_head = r'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>xxxxxx</title><style type="text/css">div.title_01 {font-size:32px;}div.title_02 {font-size:28px;}div.title_03 {font-size:22px; background-color: red;}div.content_bold {margin-bottom: 10px;font-size: 18px;font-weight: bold;}div.content_custom {}div.center_img {width:100%}</style></head><body>'
	    		html_foot = r'</body></html>'
	    		f = open(currentDir + '/' + result_name + '.html','a')
	    		f.write(html_head)
	    		f.write(content_write)
	    		f.write(html_foot)
f.close()
html_head_content.close()





    
