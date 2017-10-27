####Python3.5 - 自动化打包
---

1.打开文件后需要配置6个参数

	# 项目文件夹路径（/Users/xxx/Desktop/xxx）
	project_path = 'xxx'
	# 项目名称
	project_name = 'xxx.xcodeproj'
	# ipa文件夹(/Users/xxx/Desktop)
	IPA_dir = 'xxx'
	# 项目TARGETS名称
	set_target_name = ''
	# provisioning profile uuid
	set_provisioning_profile_UUID = ''
	# 证书的teamID
	teamID = ''

2.打开终端运行命令

	$ python3.5 archiveipa.py
	
